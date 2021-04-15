import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()    # 用于渲染出当前的智能体以及环境的状态。
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(i_episode,"*" * 50)
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()