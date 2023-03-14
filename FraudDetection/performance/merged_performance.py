"""
This module helps in combining the performance of the supervised and 
unsupervised fraud detection models
"""

import json

with open('./FraudDetection/script/json/models_performance.json',encoding='utf-8') as f1:
    # open the file
    data1 = json.load(f1)

with open('./FraudDetection/script/json/models_performance_supervised.json',encoding='utf-8') as f2:
    # open the file
    data2 = json.load(f2)

per_dict = {}
for d in [data2, data1]:
    per_dict.update(d)


FILENAME = "./FraudDetection/script/json/models_performance_sup_unsup.json"
with open(FILENAME, "w", encoding='utf-8') as outfile:
    json.dump(per_dict, outfile)
