import time


def main_info():
    print("""
        -----------------------------
                欢迎来到丰巢快递
                请选择您想做的操作：
                输入1--->存
                输入2--->取
                输入0--->返回主页
        -----------------------------
        """)
    access = input('请输入：')
    return access


def show_info(access):
    while 1:
        if access == '1':
            print('进入存的界面')
            break
        elif access == '2':
            print('取的界面')
            break
        elif access == '0':
            print('返回主页...')
            time.sleep(3)
            main_info()
            break
        else:
            print('开发中.....')
            break


if __name__ == '__main__':
    access = main_info()
    show_info(access)
