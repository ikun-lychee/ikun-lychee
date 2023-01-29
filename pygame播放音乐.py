"""
pygame.mixer.music.load() 加载音乐。参数为filename，以字符串传入音频文件地址；
pygame.mixer.music.unload() 卸载已经加载的音乐。无参数；
pygame.mixer.music.play() 播放加载的音乐。三个可选参数，loops循环次数（int）；start开始播放时间（float）有的文件类型可能不支持（我试验过的Ubuntu环境下wav文件不支持设置）mp3文件的时间定位可能不准确；fade_ms音量渐变的时间间隔（int）我没有听出啥区别。。。；这三个参数默认为0
pygame.mixer.music.rewind() 重新开始音乐。
pygame.mixer.music.stop() 停止音乐播放。
pygame.mixer.music.pause() 暂停音乐播放。
pygame.mixer.music.unpause() 恢复暂停的音乐。
pygame.mixer.music.fadeout() 淡出后停止音乐播放。
pygame.mixer.music.set_volume() 设置音量。参数0~1之间的浮点数；
pygame.mixer.music.get_volume() 获得音量。返回一个浮点数（0~1之间）；
pygame.mixer.music.get_busy() 音乐是否播放。返回一个bool类型的值（文档的说明）我实际测试返回的是0和1不过无所谓当需要传bool值是python会将1看成True0，看成False的（Ubuntu环境）。我的测试程序及结果如下：
————————————————
版权声明：本文为CSDN博主「Lmx!」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hskjshs/article/details/114001554
"""