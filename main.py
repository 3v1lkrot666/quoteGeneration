from workflow.parse_mode import ParseSites
from workflow.quote_generation import QuoteGeneration


"""
██████╗░██╗░░░██╗░░███╗░░██╗░░░░░██╗░░██╗██████╗░░█████╗░████████╗░█████╗░░█████╗░░█████╗░
╚════██╗██║░░░██║░████║░░██║░░░░░██║░██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══╝░██╔═══╝░██╔═══╝░
░█████╔╝╚██╗░██╔╝██╔██║░░██║░░░░░█████═╝░██████╔╝██║░░██║░░░██║░░░██████╗░██████╗░██████╗░
░╚═══██╗░╚████╔╝░╚═╝██║░░██║░░░░░██╔═██╗░██╔══██╗██║░░██║░░░██║░░░██╔══██╗██╔══██╗██╔══██╗
██████╔╝░░╚██╔╝░░███████╗███████╗██║░╚██╗██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝╚█████╔╝
╚═════╝░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░

Генератор цитат из фильмов с игрфическим интерфейсом

v.0.0.1(no GUI)

Сайт с цитатами: https://citaty.info/

"""




if __name__ == "__main__":
    app = QuoteGeneration()
    app.generation()