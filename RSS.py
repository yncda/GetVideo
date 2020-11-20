import time
def getmessage():
    num = 1
    while num < 3:
        message = input("请选择引擎(输入序号)：1、西瓜视频\t2、香蕉视频:\n")
        if message == str(1):
            print("已选择西瓜视频。")
            return 1
        elif message == str(2):
            print("已选择香蕉视频。")
            return 2
        else:
            if num == 1:
                print('看来你是玩不起！再给你一次机会')
            else:
                print('看来你就是玩不起！！！即将在3秒后退出')
                time.sleep(3)
            num+=1
    return message