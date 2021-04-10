import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


class Solution:

    """测试 torch """
    def test_torch(self):
        print(torch)
        x = torch.rand(5, 3)
        print(x)

    """测试 仿射变换"""
    def test_lin(self):
        torch.manual_seed(1)
        lin = nn.Linear(5, 3)
        data = torch.rand(2, 5)
        print(data)
        print(lin(data))

    """测试 非线性函数"""
    def test_feixianxing(self):
        data = torch.rand(2, 2)
        print(data)
        print(F.relu(data))

    """测试 Softmax"""
    def test_Softmax(self):
        data = torch.rand(5)
        print(data)
        print(F.softmax(data, dim=0))
        print(F.softmax(data, dim=0).sum())
        print(F.log_softmax(data, dim=0))

s = Solution()

# s.test_torch()
# s.test_lin()
# s.test_feixianxing()
s.test_Softmax()
