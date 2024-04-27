import random

# TrueNum = random.randint(1,10)
# if int(input("请猜测一个数字：")) == TrueNum:
#     print("恭喜你，天选之子！")
# elif int(input("再接再厉：")) == TrueNum:
#     print("恭喜你，猜对了！")
# elif int(input("你还有最后一次机会：")) == TrueNum:
#     print("猜对了，真不容易！")
# else :
#     print("很抱歉，机会用完了！")

TrueNum = random.randint(1, 100)
TestNum = input("请猜测一个数字(1~100)：")
while int(TestNum) != TrueNum:
    if int(TestNum) > TrueNum:
        print("猜大了！")
    elif int(TestNum) < TrueNum:
        print("猜小了！")
    TestNum = input("再来一次:")
print("恭喜你，猜对了！")