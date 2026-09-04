def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return True
            else:
                return False

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)
import random

print("""
============================
        Python工具箱
============================
""")
print("1.判断质数")
print("2.计算阶乘")
print("3.猜数字游戏")
print("4.简单计算器")
print("5.成绩统计")
print("6.温度转换")
print("0.退出程序")
choice = input("请输入你的选择（0-6）：")
if choice == "0":
    print("退出程序")
elif choice == "1":
    print("判断质数")
    num = int(input("请输入一个整数："))
    if is_prime(num):
        print(f"{num}不是质数")
    else:
        print(f"{num}是质数")
elif choice == "2":
    print("计算阶乘")
    num = int(input("请输入一个整数："))
    # factorial = 1
    # for i in range(1, num + 1):
    #     factorial *= i
    # print(f"{num}的阶乘是{factorial}")
    print(f"{num}的阶乘是{f(num)}")
elif choice == "3":
    print("猜数字游戏")
    number = random.randint(1, 100)
    while True:
        guess = int(input("请输入你的数字（1-100）："))
        if guess < number:
            print("小了")
        elif guess > number:
            print("太大了")
        else:
            print("恭喜你猜对了")
            break
elif choice == "4":
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    m = input("请输入运算符：")
    if m == "+":
        print(f"{num1} + {num2} ={num1 + num2}")
    if m == "-":
        print(f"{num1} - {num2} ={num1 - num2}")
    if m == "*":
        print(f"{num1} * {num2} ={num1 * num2}")
    if m == "/":
        print(f"{num1} / {num2} ={num1 / num2}")
    else:
        print("错误")
elif choice == "5":
    scores = []
    count = int(input("请输入数量："))
    for i in range(count):
        score = int(input("请输入成绩："))
        scores.append(score)
    print(f"平均分是：{sum(scores)/len(scores)}")
    print(f"最高分是：{max(scores)}")
    print(f"最低分是：{min(scores)}")
elif choice == "6":
    k = int(input("请选择要转换的温度单位：1.摄氏度；2.华氏度"))
    if k == 1:
        m = int(input("请输入摄氏度："))
        print(f"华氏度为：{m + 273}K")
    elif k == 2:
        n = int(input("请输入华氏度"))
        print(f"摄氏度为：{n - 273}K")




    




