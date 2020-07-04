import os
from shutil import copyfile
import sys

rootDir="/Users/liutim/Downloads/知识付费/【完结】傅佩荣的西方哲学课"
destDir="output"
tempo="2.3"
filenamePre="_"

#保留原音频文件的名字，不把文件夹纳入到音频文件名中，也不用pdf/jpg文件名替换音频文件名.当音频文件名本身信息足够（概括内容和用于排序）时，建议使用True，否则取False
trytoCorrectFilename=False  #True
useShortFilename=False


escapeStringArray=["请加微信36903863","曾鸣"]


if __name__=="__main__":
    os.system("python3 _1_flatize.py "+' \"'+rootDir+'\"' +' \"'+destDir+'\"' +' \"'+str(trytoCorrectFilename)+'\"'+' \"'+str(useShortFilename)+'\"' +' \"'+str(escapeStringArray)+'\"' )
    os.system("./_2_conv.sh " + ' \"' + rootDir + '\"' + ' \"' + destDir + '\" ' + tempo+" "+filenamePre)
    os.system("python3 _3_normalize.py " + ' \"' + rootDir + '\"' + ' \"' + destDir + '\"')




