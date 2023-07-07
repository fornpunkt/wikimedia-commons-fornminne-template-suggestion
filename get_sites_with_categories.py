import csv

import requests

def get_query(article):
 return f'SELECT ?category WHERE {{ <{article}> schema:about ?item . ?item wdt:P373 ?category . }}'''

url = 'https://query.wikidata.org/sparql'
headers = {
    'User-Agent': 'Commons image suggester'
}

results = list()
with open('data/wikipedia_site.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        wikipedia = row[0]
        site = row[1]
        
        params = {
            'query': get_query(wikipedia),
            'format': 'json'
        }
        
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        bindings = data['results']['bindings']
        if len(bindings):
            results.append([bindings[0]['category']['value'], site])

csv_file = 'data/category_site.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['category', 'site'])
    for item in results:
        writer.writerow(item)

