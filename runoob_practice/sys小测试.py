import sys
if __name__ == '__main__':
    print('================Python import mode==========================')
    print('命令行参数为:')
    for i in sys.argv:
        print(i)
    print ('\n python 路径为',sys.path)