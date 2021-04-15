import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

data = [("me gusta comer en la cafeteria".split(), "SPANISH"),
        ("Give it to me".split(), "ENGLISH"),
        ("No creo que sea una buena idea".split(), "SPANISH"),
        ("No it is not a good idea to get lost at sea".split(), "ENGLISH")]
test_data = [("Yo creo que si".split(), "SPANISH"),
             ("it is lost on me".split(), "ENGLISH")]
# word_to_ix maps each word in the vocab to a unique integer, which will be its
# index into the Bag of words vector
word_to_ix = {}
for sent, _ in data + test_data:
    for word in sent:
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)
print(word_to_ix)
VOCAB_SIZE = len(word_to_ix)
NUM_LABELS = 2


class BoWClassifier(nn.Module):  # inheriting from nn.Module!

    def __init__(self, num_labels, vocab_size):
        # calls the init function of nn.Module. Dont get confused by syntax,
        # just always do it in an nn.Module
        super(BoWClassifier, self).__init__()
        # Define the parameters that you will need. In this case, we need A and b,
        # the parameters of the affine mapping.
        # Torch defines nn.Linear(), which provides the affine map.
        # Make sure you understand why the input dimension is vocab_size
        # and the output is num_labels!
        self.linear = nn.Linear(vocab_size, num_labels)

    # NOTE! The non-linearity log softmax does not have parameters! So we don't need

    # to worry about that here
    def forward(self, bow_vec):
        # Pass the input through the linear layer,
        # then pass that through log_softmax.
        # Many non-linearities and other functions are in torch.nn.functional
        return F.log_softmax(self.linear(bow_vec), dim=1)


def make_bow_vector(sentence, word_to_ix):
    vec = torch.zeros(len(word_to_ix))
    for word in sentence:
        vec[word_to_ix[word]] += 1
    return vec.view(1, -1)


def make_target(label, label_to_ix):
    return torch.LongTensor([label_to_ix[label]])


model = BoWClassifier(NUM_LABELS, VOCAB_SIZE)
# 模型知道它的参数。 下面的第一个输出是A，第二个输出是b。
# 无论何时将组件分配给模块的__init__函数中的类变量，都是使用self.linear = nn.Linear（...）行完成的。
# 然后通过PyTorch，你的模块（在本例中为BoWClassifier）将存储nn.Linear参数的知识
for param in model.parameters():
    print("param:", param)
    # 要运行模型，请传入BoW矢量
    # 这里我们不需要训练，所以代码包含在torch.no_grad（）中
with torch.no_grad():
    sample = data[0]
bow_vector = make_bow_vector(sample[0], word_to_ix)
log_probs = model(bow_vector)
print("log_probs:", log_probs)
label_to_ix = {"SPANISH": 0, "ENGLISH": 1}

"""开始训练"""
print("以下是训练部分********************************************************")
# 在我们训练之前运行测试数据，只是为了看到之前-之后
with torch.no_grad():
    for instance, label in test_data:
        bow_vec = make_bow_vector(instance, word_to_ix)
        log_probs = model(bow_vec)
        print("log_probs:", log_probs)
# 打印与“creo”对应的矩阵列
print("creo:", next(model.parameters())[:, word_to_ix["creo"]])
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)
# 通常，您希望多次传递训练数据.
# 100比实际数据集大得多，但真实数据集有两个以上的实例。
# 通常，在5到30个epochs之间是合理的。
for epoch in range(100):
    for instance, label in data:
        # 步骤1： 请记住，PyTorch会累积梯度。
        # We need to clear them out before each instance
        model.zero_grad()
        # 步骤2：制作我们的BOW向量，并且我们必须将目标作为整数包装在Tensor中。
        # 例如，如果目标是SPANISH，那么我们包装整数0.
        # 然后，loss函数知道对数概率的第0个元素是对应于SPANISH的对数概率
        bow_vec = make_bow_vector(instance, word_to_ix)
        target = make_target(label, label_to_ix)
        # 步骤3：运行我们的前向传递.
        log_probs = model(bow_vec)
        # 步骤4： 通过调用optimizer.step()来计算损失，梯度和更新参数
        loss = loss_function(log_probs, target)
        loss.backward()
        optimizer.step()

with torch.no_grad():
    for instance, label in test_data:
        bow_vec = make_bow_vector(instance, word_to_ix)
        log_probs = model(bow_vec)
        print("log_probs", log_probs)

# 对应西班牙语的指数上升，英语下降！
print("creo:", next(model.parameters())[:, word_to_ix["creo"]])
