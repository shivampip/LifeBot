import requests as req
from bs4 import BeautifulSoup as bs

class Book():
	def __init__(self):
		pass

	def search(self, query):
		url= "https://www.google.co.in/search?q=filetype%3Apdf+"
		self.query= query
		self.url= url+ query
		res= req.get(self.url)
		self.soup= bs(res.content, 'html.parser')
		#print(self.soup)

	def match_class(self, target):                                                        
		classes = self.soup.get('class', [])                                          
		return all(c in classes for c in target)                                
		

	def process(self):
		links= self.soup.find_all('a', href=True)
		self.results=[]
		for link in links:
			print(link.get_text())
			tx= link['href']
			try:
				data= tx[tx.index('?q=')+3: tx.index('.pdf')+4]	
				self.results.append({link.get_text(): data})		
			except Exception as e:
				data= "OK"
		print("\n\nTotal "+str(len(self.results))+" found\n")
		for aa in self.results:
			print(str(aa)+"\n")

bk= Book()
bk.search("python")
bk.process()