#test for
interviewee = [26, 28, 30, 32, 26, 35, 40]
for age in interviewee:
    if 30 < age < 35:
        print(f"{age}岁可能是一个高级工程师")
    elif age >= 35:
        print(f"{age}岁可能是一个测试专家或者测试管理")
    else:
        print(f"{age}岁可能是一个初中级工程师")