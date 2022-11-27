from workflow.parse_mode import ParseSites
from random import randint



class QuoteGeneration:
    def __init__(self) -> None:
        ... 

    def generation(self):
        self.parse_data = ParseSites("https://citaty.info/movie/dzhentlmeny-the-gentlemen")
        self.quote_generation = self.parse_data.parse()
        self.summ = len(self.quote_generation)     
        self.number_random = randint(0, self.summ)
        
        print(self.quote_generation[self.number_random])        
