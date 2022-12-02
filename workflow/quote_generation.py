from workflow.parse_mode import ParseSites
from random import randint



class QuoteGeneration:
    def __init__(self, qSITES) -> None:
        self.parse_data = ParseSites(qSITES)

    def generation(self):
        self.quote_generation = self.parse_data.parse()
        self.summ = len(self.quote_generation)     
        self.number_random = randint(1, self.summ - 1)
        
        return self.quote_generation[self.number_random]     
