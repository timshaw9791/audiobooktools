# audiobooktools
## 环境准备(安装id3lib/ffmpeg/python3/bash)
 - brew install id3lib,便于使用id3tag修改音频元数据。可以查看id3tag --help。参照http://id3lib.sourceforge.net
 - brew install ffmpeg,用于对mp3/m4a进行倍数转换。
 - 使用pyenv设置python3最新版本。brew install pyenv && pyenv install 3.8.3 && pyenv global 3.8.3 && pyenv version 。
 最后设置echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
   最后看python -V && pip -V
 
## 完成后处理
 - 运用Audiobook Binder程序完成输出。
 
 
#TODO
- 在网络上获取封面图片
- 设置Audiobook Binder的自动化
- 在标题去掉功能中支持正则表达式查找和替换


 
  

