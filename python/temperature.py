#!/usr/bin/evn python3
fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 #华氏转摄氏
    print("{:5d} {:7.2f}".format(fahrenheit,celsius)) #5d替换5个字符的整数，不足补空格，7.2替换7个字符宽度保留两位的小数。
    fahrenheit = fahrenheit + 25
