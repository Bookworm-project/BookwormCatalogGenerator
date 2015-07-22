import requests
import json
import sys
import time
import random
import os.path
from bs4 import BeautifulSoup
for j in range(0,10):
	i=1
	while i<=1000:
		name = random.randint(0,999999)
		
		name = str((j*1000000)+name)
		file = '/home/ubuntu/HN/HackerNews/' +str(j)+ '/' +name+ '.json'
		if os.path.exists(file)==False:
			continue
		raw = open('/home/ubuntu/BookwormDB/files/texts/raw/'+name+'.txt', 'w+')
		meta = open('/home/ubuntu/BookwormDB/files/metadata/jsoncatalog.txt', 'a')

		with open(file) as data_file:
			data = json.load(data_file)
	
		item = {'id':'','deleted':'','type':'','author':'','date':'','dead':'','parent':'','kids':'','num_kids':'','url':'','score':'','title':'','descendants':'','parts':''}	
		if data is None:
			print file
			continue
		for k,v in data.iteritems():
			if k=='id':
				item['id'] = str(v)
			elif k=='deleted':
				z+=1
				item['deleted'] = str(v)
			elif k=='type':
				item['type'] = str(v)
			elif k=='by':
				item['author'] = str(v)
			elif k=='time':
				v = time.strftime('%Y-%m-%d', time.localtime(v))
				item['date'] =  str(v)
			elif k=='text':
				w+=1
				#print data['id']
				soup = BeautifulSoup(v, 'html.parser')
				#soup = BeautifulSoup(open(v))
				v = soup.get_text()
				raw.write(unicode(v).encode('utf-8')+'\n')
				#raw.write(unicode(v)+'\n')
				sample_text = unicode(v)
				#raw.write(sample_text+'\n')
			elif k=='dead':
				item['dead'] = str(v)
			elif k=='parent':
				item['parent'] = str(v)
			elif k=='kids':
				item['num_kids'] = str(len(v))
				item['kids'] = []
				for a in v:
					item['kids'].append(str(a))
			elif k=='url':
				item['url'] = unicode(v).encode('utf-8')
			elif k=='score':
				item['score'] = str(v)
			elif k=='title':
				item['title'] = unicode(v).encode('utf-8')
				raw.write(unicode(v).encode('utf-8')+'\n')
			elif k =='parts':
				item['parts'] = []
				for b in v:
					item['parts'].append(str(b))
			elif k=='descendants':
				item['descendants'] = str(v)
	
		loc = 'https://news.ycombinator.com/item?id='+item['id']
		if item['title']!='':
			searchstring = '<a href='+loc+' target=_blank> Comment ID:' +item['id']+", "+item['title']+ '</a>' 
		else:
			new_text = sample_text.split()
			sample = ''
			if len(new_text)<10:
				for j in range(0, len(new_text)):
					sample+=new_text[j]+' '
			else:
				for k in range(0,10):
					sample+=new_text[k]+' '	
			searchstring = '<a href='+loc+' target=_blank> Comment ID: ' +item['id']+", "+unicode(sample)+ '</a>'
		item['searchstring'] = searchstring
		item['filename'] = name
		item = json.dumps(item)
		meta.write(item +'\n')
		raw.close()
		i+=1
meta.close()
