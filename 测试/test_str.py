# 测试字符串操作

# 定义一个字符串
my_string = "Hello, World!"
# 访问字符串中的字符
print(my_string[0])  # 输出: H
# 获取字符串的长度
print(len(my_string))  # 输出: 13
# 切片操作
print(my_string[0:5])  # 输出: Hello
# 字符串连接
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # 输出: Hello, Alice!
# 字符串格式化
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)  # 输出: Alice is 30 years old.
# 字符串方法
print(my_string.lower())  # 输出: hello, world!
print(my_string.upper())  # 输出: HELLO, WORLD!
print(my_string.replace("World", "Python"))  # 输出: Hello, Python!
print(my_string.split(", "))  # 输出: ['Hello', 'World!']
# 检查子字符串
print("Hello" in my_string)  # 输出: True
print("Python" in my_string)  # 输出: False
# 去除字符串两端的空格
my_string_with_spaces = "   Hello, World!   "
print(my_string_with_spaces.strip())  # 输出: Hello, World!
# 字符串反转
print(my_string[::-1])  # 输出: !dlroW ,olleH
# 多行字符串
multi_line_string = """This is a multi-line
string that spans multiple lines."""
print(multi_line_string)  
# 字符转换为ASCII码
print(ord('A'))  # 输出: 65
# ASCII码转换为字符
print(chr(65))  # 输出: A
# 字符串的迭代
for char in my_string:
    print(char)
# 字符串的比较
print("apple" < "banana")  # 输出: True
print("apple" == "Apple")  # 输出: False
# 字符串的分割和连接
words = my_string.split(", ")
print(words)  # 输出: ['Hello', 'World!']
joined_string = " - ".join(words)
print(joined_string)  # 输出: Hello - World!
# .join()方法的使用
hobbies = ["basketball", "football", "swimming"]
print("My hobbies are: " + ", ".join(hobbies))  # 输出: My hobbies are: basketball, football, swimming
# 字符串的查找
print(my_string.find("World"))  # 输出: 7
print(my_string.find("Python"))  # 输出: -1
