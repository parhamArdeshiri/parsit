from io import StringIO
from abstracted.abstracted_parser import AbstractedBaseParser

import csv
import json

class CSVParser(AbstractedBaseParser):
    def parse_string(self, data):
        csv_data = StringIO(data)
        output = list(reader = csv.DictReader(csv_data))
        
        return json.dumps(output, indent=4)
        