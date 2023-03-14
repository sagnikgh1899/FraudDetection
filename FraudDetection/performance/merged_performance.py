import json
import pandas as pd

with open('./FraudDetection/script/json/models_performance.json') as f1:               
    # open the file
    data1 = json.load(f1)

with open('./FraudDetection/script/json/models_performance_supervised.json') as f2:                
    # open the file       
    data2 = json.load(f2)
    
per_dict = {}
for d in [data1, data2]:
  per_dict.update(d)


FILENAME = "./FraudDetection/script/json/models_performance_sup_unsup.json"
with open(FILENAME, "w", encoding='utf-8') as outfile:
    json.dump(per_dict, outfile)
