import numpy as np

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

if __name__ == '__main__':
    x = 0.7457084468
    s = sigmoid(x)
    print(s)

    a = 0.35
    b = 0.9
    w3 = 0.09916
    w4 = 0.7978
    w5 = 0.3972
    w6 = 0.5928
    w1 = 0.272392
    w2 = 0.87305
    h1 = a * w3 + b * w4
    h2 = a * w5 + b * w6
    o1 = sigmoid(h1)
    o2 = sigmoid(h2)
    y = o1 * w1 + o2 * w2
    out = sigmoid(y)
    print(out)

# 0.6782428730458362