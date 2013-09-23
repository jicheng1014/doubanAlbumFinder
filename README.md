豆瓣活动相册的找人工具
===============================
	当你进入某人豆瓣，看到此人在某活动上上传过照片
	则可使用此工具自动化的找到这个人上传的那个照片


### 使用条件
	python 2.7
	使用了pyquery  所以，可能需要你安装[python-lxml](http://lxml.de/installation.html)

### 使用方法
	在程序目录下运行
	python fetch.py     
	例如
		atpking@atpking-ThinkPad-E425:~/pythonCode/doubanAlbumFinder.git$ python fetch.py 
		输入豆瓣活动相册地址:http://www.douban.com/online/11522226/album/100710344/
		输入豆瓣的uid:77508437
		正在访问页面 http://www.douban.com/online/11522226/album/100710344/?start=0
		.

		人已经找到 http://www.douban.com/online/11522226/album/100710344/?start=0
		http://www.douban.com/online/11522226/photo/2149524523/

	返回的第一个为当前页，最后的地址为具体的照片地址


特别强调
================================
	是活动照片地址，而不是其他的地址
	是用户的UID，不是昵称,UID 一般显示在个人主页右侧，"常居"下面那个,有可能是数字有可能是英文	
