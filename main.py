from scrapy import cmdline
#导入cmdline模块,可以实现控制终端命令行。


import os  # 用来设置路径
import sys   # 调用系统环境，就如同cmd中执行命令一
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
# 添加环境变量
sys.path.append(dirpath)
print(sys.path)

cmdline.execute(['scrapy','crawl','douban'])
#用execute（）方法，输入运行scrapy的命令。