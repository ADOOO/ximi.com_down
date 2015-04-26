#coding=utf-8
import urllib
import urllib2
import re

def connect(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
	req = urllib2.Request(url,headers=headers)
	socket = urllib2.urlopen(req)
	content = socket.read()
	socket.close()
	#print content
	p = re.findall('<location>(.*)</location>',content)
	name = re.findall('<title>(.*)</title>',content)
	#print 'Read content success!'
	return p,name

def caesar(location):
    num = int(location[0])
    avg_len, remainder = int(len(location[1:]) / num), int(len(location[1:]) % num)
    result = [location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1] for i in range(remainder)]
    result.extend([location[(avg_len + 1) * remainder:][i * avg_len + 1: (i + 1) * avg_len + 1] for i in range(num-remainder)])
    url = urllib.unquote(''.join([''.join([result[j][i] for j in range(num)]) for i in range(avg_len)]) + \
                        ''.join([result[r][-1] for r in range(remainder)])).replace('^','0')
    return url

def downurl():
	num = len(p[0])
	#n = len(name[0])
	#print num,n
	for i in range(len(p[0])):
		location = p[0][i]
		#print location
		url = caesar(location)
		down.append(url)
	#print 'Crack url success!'
		
	file = open('xiami_down.txt','w')
	file.close()
	
	for i in range(len(p[0])):
		file = open('xiami_down.txt','a+')
		file.write(p[1][i][9:-3]+'\n'+down[i]+'\n')
		file.close
		urllib.urlretrieve(down[i],p[1][i][9:-3]+'.mp3')
	print 'Save downurl success! :)'
	
if __name__ == '__main__':
	location = []
	down = []
	name = []
	print 'Example http://www.xiami.com/play?ids=/song/playlist/id/38578398/type/3#loaded'
	urlin = raw_input('Please enter url:')
	url = urlin[:20]+urlin[30:]
	p = connect(url)
	#name = connect(url)[1]
	downurl()
