"""
1. 需要的包
"""

import gym
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple
from itertools import count
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T

import warnings
warnings.filterwarnings("ignore", category=UserWarning) # 用于过滤掉一种警告

env = gym.make('CartPole-v0').unwrapped # 定义使用gym库中的某一个环境，'CartPole-v0'可以改为其它环境 # 据说不做这个动作会有很多限制，unwrapped是打开限制的意思
# set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()   # get_backend() Return the name of the current backend.
if is_ipython:
    from IPython import display

plt.ion()   # plt.ion()这个函数，使matplotlib的显示模式转换为交互（interactive）模式。即使在脚本中遇到plt.show()，代码还是会继续执行。
# if gpu is to be used
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

"""
2. 复现记忆
"""

Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))


# * ReplayMemory ：有界大小的循环缓冲区，用于保存最近观察到的过渡。
class ReplayMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity    # 10000
        self.memory = []
        self.position = 0

    def push(self, *args):
        """Saves a transition."""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)  # 参数前面加上* 号 ，意味着参数的个数不止一个，另外带一个星号（*）参数的函数传入的参数存储为一个元组（tuple），带两个（*）号则是表示字典（dict）
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


""" 
3. Q 网络
"""


class DQN(nn.Module):

    def __init__(self, h, w, outputs):
        super(DQN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=5, stride=2)  # in_channels：输入的通道数目,out_channels： 输出的通道数目,kernel_size：卷积核的大小，类型为int 或者元组，当卷积是方形的时候，只需要一个整数边长即可，卷积不是方形，要输入一个元组表示 高和宽。stride： 卷积每次滑动的步长为多少
        self.bn1 = nn.BatchNorm2d(16)   # 在卷积神经网络的卷积层之后总会添加BatchNorm2d进行数据的归一化处理,num_features：一般输入参数为batch_sizenum_featuresheight*width，即为其中特征的数量
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=2)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=5, stride=2)
        self.bn3 = nn.BatchNorm2d(32)

        # 线性输入连接的数量取决于conv2d层的输出，因此取决于输入图像的大小，因此请对其进行计算。
        def conv2d_size_out(size, kernel_size=5, stride=2):
            return (size - (kernel_size - 1) - 1) // stride + 1
        convw = conv2d_size_out(conv2d_size_out(conv2d_size_out(w)))
        convh = conv2d_size_out(conv2d_size_out(conv2d_size_out(h)))
        linear_input_size = convw * convh * 32
        self.head = nn.Linear(linear_input_size, outputs)

    # 使用一个元素调用以确定下一个操作，或在优化期间调用batch。返回 tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        return self.head(x.view(x.size(0), -1)) # x.view(x.size(0), -1) 将前面多维度的tensor展平成一维


"""
4. 输入提取
"""
# 用Compose把多个步骤整合到一起
resize = T.Compose([T.ToPILImage(), # convert a tensor to PIL image
                    T.Resize(40, interpolation=Image.CUBIC),    # 图像变换
                    T.ToTensor()])  # convert a PIL image to tensor (H*W*C) in range [0,255] to a torch.Tensor(C*H*W) in the range [0.0,1.0]

# 获得小车的位置（cart 小车）
def get_cart_location(screen_width):
    world_width = env.x_threshold * 2   # 宽度，x_threshold = 2.4,表示小车距离中心位置不超过2.4
    scale = screen_width / world_width
    return int(env.state[0] * scale + screen_width / 2.0)  # MIDDLE OF CART


def get_screen():
    # gym要求的返回屏幕是400x600x3，但有时更大，如800x1200x3。 将其转换为torch order（CHW）。
    screen = env.render(mode='rgb_array').transpose((2, 0, 1))
    # cart位于下半部分，因此不包括屏幕的顶部和底部
    _, screen_height, screen_width = screen.shape
    screen = screen[:, int(screen_height * 0.4):int(screen_height * 0.8)]
    view_width = int(screen_width * 0.6)
    cart_location = get_cart_location(screen_width)
    if cart_location < view_width // 2:
        slice_range = slice(view_width)
    elif cart_location > (screen_width - view_width // 2):
        slice_range = slice(-view_width, None)
    else:
        slice_range = slice(cart_location - view_width // 2,
                            cart_location + view_width // 2)
    # 去掉边缘，使得我们有一个以cart为中心的方形图像
    screen = screen[:, :, slice_range]
    # 转换为float类型，重新缩放，转换为torch张量
    # (this doesn't require a copy)
    screen = np.ascontiguousarray(screen, dtype=np.float32) / 255
    screen = torch.from_numpy(screen)   # torch.from_numpy()方法把数组转换成张量，且二者共享内存，对张量进行修改比如重新赋值，那么原始数组也会相应发生改变。
    # 调整大小并添加batch维度（BCHW）
    return resize(screen).unsqueeze(0).to(device)


env.reset()
plt.figure()    # #新建figure
plt.imshow(get_screen().cpu().squeeze(0).permute(1, 2, 0).numpy(), interpolation='none')    # plt.imshow()函数负责对图像进行处理，并显示其格式，但是不能显示。其后跟着plt.show（）才能显示出来
plt.title('Example extracted screen')
plt.show()

"""
5. 训练
"""
BATCH_SIZE = 128    # size of minibatch
GAMMA = 0.999   # discount factor for target Q
# 选择随机操作的概率将从EPS_START 开始，并将以指数方式向EPS_END 衰减。EPS_DECAY 控制衰减的速度
EPS_START = 0.9 # starting value of epsilon
EPS_END = 0.05  # final value of epsilon
EPS_DECAY = 200
TARGET_UPDATE = 10

# 获取屏幕大小，以便我们可以根据AI gym返回的形状正确初始化图层。
# 此时的典型尺寸接近3x40x90
# 这是get_screen（）中的限幅和缩小渲染缓冲区的结果
init_screen = get_screen()
_, _, screen_height, screen_width = init_screen.shape

# 从gym行动空间中获取行动数量
n_actions = env.action_space.n  # 动作空间是离散空间:0: 表示小车向左移动，1: 表示小车向右移动

policy_net = DQN(screen_height, screen_width, n_actions).to(device)
target_net = DQN(screen_height, screen_width, n_actions).to(device)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()   # net.train():模型训练时的特征。net.eval()：测试时的网络特征。

optimizer = optim.RMSprop(policy_net.parameters())  # RMSProp算法在经验上已经被证明是一种有效且实用的深度神经网络优化算法。目前它是深度学习从业者经常采用的优化方法之一。
memory = ReplayMemory(10000)
# 记录全局步骤
steps_done = 0


# 根据输入状态选择动作
def select_action(state):
    global steps_done
    sample = random.random()    # random()方法返回随机生成的一个实数,它在[0,1)范围内
    # 阈值 eps_threshold 由0.9 不断下降
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
                    math.exp(-1. * steps_done / EPS_DECAY)
    # print(steps_done, "eps_threshold:", eps_threshold)
    steps_done += 1
    if sample > eps_threshold:
        with torch.no_grad():
            # t.max(1)将返回每行的最大列值。
            # 最大结果的第二列是找到最大元素的索引，因此我们选择具有较大预期奖励的行动。
            return policy_net(state).max(1)[1].view(1, 1)
    else:
        return torch.tensor([[random.randrange(n_actions)]], device=device, dtype=torch.long)   # 随机动作


#记录 duration（持续时间），即纵坐标的值
episode_durations = []


# 绘制曲线图， x：episode  y: duration
def plot_durations():
    plt.figure(2)
    plt.clf()
    durations_t = torch.tensor(episode_durations, dtype=torch.float)
    plt.title('Training...')
    plt.xlabel('Episode')
    plt.ylabel('Duration')  # 持续时间
    plt.plot(durations_t.numpy())
    # print(durations_t.numpy())
    # 取100个episode的平均值并绘制它们
    if len(durations_t) >= 100:
        means = durations_t.unfold(0, 100, 1).mean(1).view(-1)
        means = torch.cat((torch.zeros(99), means))
        plt.plot(means.numpy())
    plt.pause(0.001)  # 暂停一下，以便更新图表
    if is_ipython:
        display.clear_output(wait=True)
        display.display(plt.gcf())


"""
训练循环
"""


# 优化的单个步骤
def optimize_model():

    if len(memory) < BATCH_SIZE:
        return

    transitions = memory.sample(BATCH_SIZE)
    # 转置batch（有关详细说明，请参阅https://stackoverflow.com/a/19343/3343043）。
    # 这会将过渡的batch数组转换为batch数组的过渡。
    batch = Transition(*zip(*transitions))
    # print("batch:", batch)
    # 计算非最终状态的掩码并连接batch元素（最终状态将是模拟结束后的状态）
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None, batch.next_state)), device=device, dtype=torch.uint8)
    non_final_next_states = torch.cat([s for s in batch.next_state if s is not None])   # torch.cat是将两个张量（tensor）拼接在一起
    state_batch = torch.cat(batch.state)
    action_batch = torch.cat(batch.action)
    reward_batch = torch.cat(batch.reward)
    # 计算Q(s_t，a) - 模型计算Q(s_t)，然后我们选择所采取的动作列。
    # 这些是根据policy_net对每个batch状态采取的操作
    state_action_values = policy_net(state_batch).gather(1, action_batch)
    # 计算所有下一个状态的V(s_{t+1})
    # non_final_next_states的操作的预期值是基于“较旧的”target_net计算的;
    # 用max(1)[0]选择最佳奖励。这是基于掩码合并的，这样我们就可以得到预期的状态值，或者在状态是最终的情况下为0。
    next_state_values = torch.zeros(BATCH_SIZE, device=device)
    next_state_values[non_final_mask] = target_net(non_final_next_states).max(1)[0].detach()
    # 计算预期的Q值
    expected_state_action_values = (next_state_values * GAMMA) + reward_batch
    # 计算Huber损失
    loss = F.smooth_l1_loss(state_action_values, expected_state_action_values.unsqueeze(1)) # torch.unsqueeze()这个函数主要是对数据维度进行扩充。需要通过dim指定位置，给指定位置加上维数为1的维度。
    # 优化模型
    optimizer.zero_grad()   # optimizer.zero_grad()意思是把梯度置零，也就是把loss关于weight的导数变成0.
    loss.backward()
    for param in policy_net.parameters():
        param.grad.data.clamp_(-1, 1)   # 可能出现梯度爆炸，训练时，加上梯度截断,param.grad.data.clamp_(-grad_clip, grad_clip)

    optimizer.step()


# 训练的主过程
num_episodes = 200
for i_episode in range(num_episodes):
    # 初始化环境和状态
    env.reset()
    last_screen = get_screen()
    current_screen = get_screen()
    state = current_screen - last_screen
    for t in count():
        # 选择动作并执行
        action = select_action(state)
        _, reward, done, _ = env.step(action.item())    # 将选择的action输入给env，env 按照这个动作走一步进入下一个状态
        reward = torch.tensor([reward], device=device)
        # 观察新的状态
        last_screen = current_screen
        current_screen = get_screen()
        if not done:
            next_state = current_screen - last_screen
        else:
            next_state = None
        # 在记忆中存储过渡
        memory.push(state, action, next_state, reward)
        # 移动到下一个状态
        state = next_state
        # 执行优化的一个步骤（在目标网络上）
        optimize_model()
        if done:
            episode_durations.append(t + 1)
            plot_durations()
            break
    # 更新目标网络，复制DQN中的所有权重和偏差
    if i_episode % TARGET_UPDATE == 0:  # 每10个episode更新一次
        target_net.load_state_dict(policy_net.state_dict())

print('Complete')
env.render()    # 渲染环境，即可视化看看环境的样子
env.close()
plt.ioff()  # 如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像会一闪而过，并不会常留。要想防止这种情况，需要在plt.show()之前加上ioff()命令。
plt.show()
