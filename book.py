import requests as req
from bs4 import BeautifulSoup as bs
import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
#log.info('Logging Started')

class Book():
	def __init__(self):
		pass

	def search(self, query):
		url= "https://www.google.co.in/search?q=filetype%3Apdf+"
		self.query= query
		self.url= url+ query
		res= req.get(self.url)
		self.soup= bs(res.content, 'html.parser')
		links= self.soup.find_all('a', href=True)
		self.results=[]
		for link in links:
			#print(link.get_text())
			tx= link['href']
			try:
				data= tx[tx.index('?q=')+3: tx.index('.pdf')+4]	
				self.results.append({link.get_text(): data})		
			except Exception as e:
				data= "OK"
		log.info("Total "+str(len(self.results))+" found\n")
		#print(self.soup)

	def match_class(self, target):                                                        
		classes = self.soup.get('class', [])                                          
		return all(c in classes for c in target)                                
		
	def download(self,name, url):
		uri= "Files/"+name+".pdf"
		r= req.get(url)
		with open(uri, 'wb') as f:
			f.write(r.content)
		return uri

	def process(self, n=1):
		ans=[]
		for aa in self.results:
			if(n<0):
				break
			n-=1
			key= list(aa.keys())[0]
			value= aa[key]
			if(key=='Cached'):
				continue
			name= key
			url= value
			log.info('Downloading '+str(n)+'th book: '+name)
			ans.append(self.download(name, url))
		return ans




if(__name__=='__main__'):
	bk= Book()
	bk.search("python")
	bk.process()