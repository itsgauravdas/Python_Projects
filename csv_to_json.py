import csv 
import json
import os 

def csv_to_json(csv_file , json_file):
    #open the json file 
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        
        #covert csv to json 
        json_data = json.dumps(list(csv_data))

        #write the json data to file 
        with open(json_file,'w') as json_file:
            json_file.write(json_data)
            
# specify the csv to json file path 

csv_file='input.csv'
json_file = 'output.text'

# convert csv to json 
csv_to_json(csv_file,json_file)

print(f"csv file {csv_file} has been converted to json file {json_file}")