from workflow.parse_mode import ParseSites
from random import randint



class QuoteGeneration:
    def __init__(self, qSITES) -> None:
        self.parse_data = ParseSites(qSITES)

    def generation(self):
        self.dzhentelmens = "dzhentlmeny-the-gentlemen"
        self.krestnyi_otec_the_godfather = "krestnyi-otec-the-godfather"
        self.dzhoker_joker_2012 = "dzhoker-joker-2012"
        self.neprikasaemye = "1-1-neprikasaemye-the-intouchables"
        self.matrica_the_matrix = "matrica-the-matrix"
        self.boicovskii_klub = "boicovskii-klub-fight-club"
    


        
        self.quote_generation = self.parse_data.parse()
        self.summ = len(self.quote_generation)     
        self.number_random = randint(1, self.summ - 1)
        
        return self.quote_generation[self.number_random]     
