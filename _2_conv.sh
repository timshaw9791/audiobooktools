#!/bin/bash
#https://superuser.com/questions/704493/ffmpeg-convert-m4a-files-to-mp3-without-significant-loss-of-information-quali
#https://gist.github.com/carcdrcons/70dc29702359933bb116ca7eb7cfcf7e
#先执行这句让她可以执行 chmod +x _conv.sh


#指定文件夹

rootDir=$1
workDir=$2 #"output" #默认在根路径下的output
tempo=$3 # 2.3 #可以修改tempo配置转换倍数
pre=$4 #_ #可以修改前缀

#workDir="output" #默认在根路径下的output
#rootDir="/Users/liutim/Downloads/【完结】吴伯凡·认知方法论"
#rootDir=$(pwd)

SOURCE=${rootDir}/$workDir


SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

flist=`ls $SOURCE`
for file in $flist
do
	echo $file

	if [ "${file##*.}"x = "mp3"x ];then
    src=`echo $file |sed 's/\.mp3//'`
		dst=${SOURCE}/${pre}${tempo}_${src}.mp3
		ffmpeg -i "${SOURCE}/${src}.mp3" -filter:a "atempo=$tempo" -vn "$dst" -y
	fi

	if [ "${file##*.}"x = "m4a"x ];then
		src=`echo $file |sed 's/\.m4a//'`
		dst=${SOURCE}/${pre}${tempo}_${src}.mp3
		ffmpeg -i "${SOURCE}/${src}.m4a" -filter:a "atempo=$tempo"  -acodec libmp3lame -ab 128k "$dst"
	fi
	#echo $dst

done


IFS=$SAVEIFS
