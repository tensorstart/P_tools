# argument

# 1.如何读取命令行中传递进来的参数

#


# import sys
#
# print(sys.argv)
#
# # python .\06_argparse.py 5 6
# # ['.\\06_argparse.py', '5', '6']
#
# # 1.获取命令行的所有参数
#
# #       sys.argv获取命令行中的所有参数
#
# #       forrmat：script的路径，其他参数
#
# print(int(sys.argv[1]) * int(sys.argv[2]))
#
# # 2.专门处理命令行的library argparse

import argparse

# 1.创建解释器
parser = argparse.ArgumentParser()

# 需求 实现乘法操作

# 添加a参数

parser.add_argument("-a", type=int, help="operator A")

parser.add_argument("-b", type=int, help="operator B")


#解析命令行
args = parser.parse_args()

print(args.a * args.b)
