#newpm2.5
def main():
    PM = eval(input("输入PM2.5的值"))
    if PM > 250:
        print("严重污染")
    elif PM > 150:
        print("重度污染")
    elif PM > 115:
        print("中度污染")
    elif PM > 75:
        print("轻度污染")
    elif PM > 35:
        print("良")
    else:
        print("优")
main()
