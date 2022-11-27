from bs4 import BeautifulSoup
import requests



class ParseSites:
    def __init__(self, SITES) -> None:
        self.SITES = SITES
        self.quote = []
    def parse(self):
        self.responce = requests.get(self.SITES)
        self.soup = BeautifulSoup(self.responce.text, 'lxml')
        self.data = self.soup.find(class_="view-content").find_all('p')
        for self.text in self.data:
            self.quote.append(self.text.text)
        
        return self.quote

