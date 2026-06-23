# 测试字典操作

# 创建一个字典
my_dict = {}

# 添加键值对
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'

# 访问字典中的值
print(my_dict['key1'])  # 输出: value1

# 更新字典中的值
my_dict['key1'] = 'new_value1'
print(my_dict['key1'])  # 输出: new_value1

# 删除字典中的键值对
del my_dict['key2']
print(my_dict)  # 输出: {'key1': 'new_value1'}

# 使用字典的 get 方法访问值
print(my_dict.get('key1'))  # 输出: new_value1
print(my_dict.get('key2', 'default_value'))  # 输出: default_value

# 遍历字典
for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}')  # 输出: Key: key1, Value: new_value1

# 检查键是否在字典中
print('key1' in my_dict)  # 输出: True
print('key2' in my_dict)  # 输出: False

# 清空字典
my_dict.clear()
print(my_dict)  # 输出: {}

# 打印字典所有的键
print(my_dict.keys())  # 输出: dict_keys([])
# 打印字典所有的值
print(my_dict.values())  # 输出: dict_values([])

