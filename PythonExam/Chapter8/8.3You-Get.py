"""8.3 You-Get是一个基于Python3的视频下载工具，支持多数国内外主流视频站点的视
频下载。请查找该项目的主页，安装这个第三方库并编写一个实例
"""

# 注意，这些是在终端里直接运行的代码！
# 以B站视频为例
# 常规下载
you-get http://www.bilibili.com/video/av3567324

# 仅查看视频信息
you-get -i http://www.bilibili.com/video/av3567324

# 将视频保存到特定位置
you-get -o E:/ http://www.bilibili.com/video/av3567324

# 注意！
# 1. 各大视频网站需要登录观看的视频无法直接下载
# 2. 有些网站视频需要设置代理
