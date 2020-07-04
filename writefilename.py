import json
import os
import sys


# 在chorme的console下运行用来加序号的语句，filenames.forEach((item,x,y)=>(y[x]=((x+1001+"").substr(1))+item))
rootDir="/Users/liutim/wzvtc/all-about-st-of-wzvtc/ST-2019-2020-02/仿真项目实践/【20】Vue实战项目：电商管理系统（Element-UI）/"
argvlen=len(sys.argv)
checkOrRename= "check" if argvlen<=1 else sys.argv[1]
namesfile= "filenames.json" if argvlen<=2 else sys.argv[2]

filenamelist = []


#os.rename
#os.rename( "test1.txt", "test2.txt" )
# 遍历文件夹建立keys，也就是那些mp3或者m4a文件名
def walkFileForNames(file):
    for root, dirs, files in os.walk(file):
        dirs.sort()
        files.sort()
        # 遍历文件
        for f in files:
            file_path = os.path.join(root, f)
            if file_path.lower().endswith(".mp4") or file_path.lower().endswith(".m4a"):
                filenamelist.append(file_path)
                print(file_path)

                #print(file_path)
        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))



if __name__ == '__main__':
       # json.load读取文件并将文件内容转为Python对象
    # 数据文件要s.json的内容 --> {"name": "wade", "age": 54, "gender": "man"}
    with open(namesfile, 'r') as f:
        filenames = json.load(f)
        print(len(filenames))
        print("json.load将文件内容转为Python对象: type(json.load(f)) = {}".format(type(filenames)))
        print("json.load将文件内容转为Python对象: json.load(f) = {}".format(filenames))

    walkFileForNames(rootDir)
    print(filenamelist)
    print(len(filenamelist))

    for i,value in enumerate(filenamelist):
        print(filenames[i])
        print(value)
        newfilename=value[:value.rindex("/")+1]+filenames[i]+value[value.rindex("."):]
        print(newfilename)
        os.rename( value, newfilename )
        title=newfilename[newfilename.rindex("/")+1:newfilename.rindex(".")]
        print(title)
        tracknumber=title[:title.index("-")]
        tracknumber=str(int("1"+tracknumber)-10**len(tracknumber));
        print(tracknumber)
        os.system("kid3-cli -c \"set title '"+title+"'\" "+newfilename)
        os.system("kid3-cli -c \"set tracknumber " + tracknumber + "\" " + newfilename);
