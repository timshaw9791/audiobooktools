import os
from shutil import copyfile
import sys

rootDir=sys.argv[1]+"/"#"/Users/liutim/Downloads/test/"
destDir=sys.argv[2]+"/"#"output/"
##保留原音频文件的名字，不把文件夹纳入到音频文件名中，也不用pdf/jpg文件名替换音频文件名
trytoCorrectFilename=bool(sys.argv[3]=='True')  #是否用pdf/jpg上的文件名来覆盖音频名
useShortFilename=bool(sys.argv[4]=='True') #是否用短名，即不包括目录名
##最终要从音频文件中除去的字符串列表，或者是一个空的列表
escapeStringArray=eval(sys.argv[5])

#rootDir="/Users/liutim/Downloads/知识付费/产品思维30讲/"
#destDir="output/"
#trytoCorrectFilename=True #是否用pdf/jpg上的文件名来覆盖音频名
#useShortFilename=False #是否用短名，即不包括目录名
#escapeStringArray=["【防止课程断更新微信：36903863知识众筹群微信：36903863微信公众号：星哥课堂;】","【防断更微信：36903863，微信：36903863，微信公众号：星哥课堂】","【防断更微信：36903863，微信：36903863】","文章/"]






#dict<音频文件路径、音频文件名>
dictForProperfullnameAndNewfullname = {}

#如果不存在则创建destDir文件夹
if(not os.path.exists(rootDir+destDir)):
    os.makedirs(rootDir+destDir)

# 遍历文件夹建立keys，也就是那些mp3或者m4a文件名
def walkFileForKeys(file):
    for root, dirs, files in os.walk(file):
        # 遍历文件
        for f in files:
            file_path = os.path.join(root, f)
            if file_path.lower().endswith(".mp3") or file_path.lower().endswith(".m4a"):
                defaultfullname=file_path
                for escapeString in escapeStringArray:
                    defaultfullname = defaultfullname.replace(escapeString, "")
                dictForProperfullnameAndNewfullname[file_path]=file_path

        # 遍历所有的文件夹
        for d in dirs:
            if (d + "/") != destDir:
                print(os.path.join(root, d))

# 遍历文件夹，来设定最终的mp3文件名，因为mp3文件本身可能是简写比如bf0104，但是一般来说，文档可能是<bf0104 我们是从哪里来的.pdf>
# 因此，我们希望最终的mp3被命名为 <bf0104 我们是从哪里来的.mp3>
def walkFileForValues(file):
    for root, dirs, files in os.walk(file):
        # 遍历文件
        for f in files:
            file_path = os.path.join(root, f)
            #newfilefullname=file_path[len(rootDir):].replace("/", "_")
            if file_path.lower().endswith(".jpg") or file_path.lower().endswith(".pdf"):
                keys=list(dictForProperfullnameAndNewfullname.keys())
                i=0
                #print(keys[i][:-4]);
                for escapeString in escapeStringArray:
                    file_path = file_path.replace(escapeString, "")
                while len(keys)>i and ( not file_path.startswith(keys[i][:-4])) :
                    i=i+1
                print("=="+str(i)+file_path)
                if i<len(dictForProperfullnameAndNewfullname) :
                    properfilename=file_path[len(rootDir):-4] + keys[i][-4:]
                    dictForProperfullnameAndNewfullname[keys[i]] = properfilename
        # 遍历所有的文件夹
        for d in dirs:
            if (d+"/")!=destDir :
                os.path.join(root, d)

# 遍历文件夹
def copyFiles():
    for key in dictForProperfullnameAndNewfullname:
        value=dictForProperfullnameAndNewfullname[key]


        if useShortFilename :#如果用短名，即不包括目录名
            value=value[value.rindex("/")+1:]
        else:
            value=value[len(rootDir):]
        filename=(value[:-4] + key[-4:]).replace("/", "")

        for escapeString in escapeStringArray :
            filename=filename.replace(escapeString,"")
        copyfile(key, rootDir + destDir + filename)


def main():
    walkFileForKeys(rootDir)
    print(dictForProperfullnameAndNewfullname)
    print("=========="+str(trytoCorrectFilename))
    if trytoCorrectFilename:  #如果不保持原有音频文件，则需要再遍历一遍，设定文件名。
        walkFileForValues(rootDir)
    copyFiles()

if __name__ == '__main__':
    main()