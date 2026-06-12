from io import StringIO
from abstracted.abstracted_parser import AbstractedBaseParser
from flatten_json import flatten

import csv
import json
import pandas as pd

class CSVParser(AbstractedBaseParser):
    def to_json(self, input_data):
        csv_data = StringIO(input_data)
        output = list(csv.DictReader(csv_data))
        
        return output
        
    def from_json(self, input_data):
        flatted_data = flatten(input_data)
        
        json_df = pd.json_normalize(flatted_data)
        output = json_df.to_csv(index=False)
        
        # print(json_df.columns)
        # print(json_df)

        return output