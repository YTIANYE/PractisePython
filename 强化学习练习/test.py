import numpy as np
import matplotlib.pyplot as plt
import random


# 测试泊松分布
new_data = []
for i in range(100000):
    new_data.append(np.random.poisson(1000))
print("min", min(new_data))     # 867
print("max", max(new_data))     # 1140
plt.plot(sorted(new_data), linewidth=4)
plt.show()

"""结论"""
# 基本 不存在过大过小的数据