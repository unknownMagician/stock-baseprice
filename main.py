import csv
from re import I
import pandas as pd
from nsetools import Nse
nse = Nse()
with open('trial.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        i = i + 1
        if i <5:
            for item in reader:
                # row[i]= next(reader)
                code = item[0]
                quote = nse.get_quote(code)
                value = quote['basePrice']
                print("Base Price : " + str(value))
        else:
            print("hello")        
        