#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys

rootDir=sys.argv[1]
#"/Users/liutim/Downloads/【完结】吴伯凡·认知方法论"
workDir=sys.argv[2]
#"output" #默认在根路径下的output

filename = rootDir+"/"+workDir+"/_00.mp3"
print(filename)
#mode = 0600|stat.S_IRUSR
# 文件系统节点指定不同模式
#os.mknod(filename)


oldDir = os.getcwd()
os.chdir(rootDir+"/"+workDir)
if(not os.path.exists(filename)):
    open(filename, 'w').close()
os.system("id3tag -t _*.mp3")
os.chdir(oldDir)

if(os.path.exists(filename)):
    os.remove(filename)


