from abstracted.abstracted_factory import AbstractedBaseFactory

from parsers.csv_parser import CSVParser

class CSVParserFactory(AbstractedBaseFactory):
    
    def create_parser(self):
        return CSVParser()
    