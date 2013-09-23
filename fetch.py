#coding:utf-8
from pyquery.pyquery import PyQuery as pq
import urllib

getIt=False
init_url = raw_input("输入豆瓣活动相册类似（http://www.douban.com/online/11463780/album/85256333/）\n地址:")
search_id = raw_input("输入豆瓣的uid:")
#init_url = "http://www.douban.com/online/11463780/album/85256333/";
d = pq(url=init_url)

l = d(".paginator a")

l = [int(i.attrib["href"].split("=")[1]) for i  in l]
max_page = max(l)
for tmp in range(0,max_page,30):
	current_url = init_url + "?start="+str(tmp)
	print "正在访问页面",current_url
	d = pq(url=current_url)
	tmpA = d(".pl > a")
	people_node_list = [node for node in tmpA if node.attrib["href"].find("people")>-1]
	
	print "." 
	for uri_node in people_node_list :
		if uri_node.attrib["href"].split("/")[-2].__contains__(search_id):
			print "\n人已经找到", current_url
			print pq(uri_node.getparent()).prev().attr("href")
			getIt=True		
			break
	if getIt:
		break;

