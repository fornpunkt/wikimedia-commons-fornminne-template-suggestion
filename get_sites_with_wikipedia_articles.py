import csv
import requests

query = '''
PREFIX schema: <http://schema.org/>
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?target ?site WHERE {
  ?body schema:subjectOf ?target .
  ?annotation oa:hasBody ?body ;
              oa:hasTarget ?site .
  FILTER(STRSTARTS(STR(?target), "https://sv.wikipedia.org/wiki/"))
}
'''

url = 'https://sparql.fornpunkt.se/query'
headers = {
    'User-Agent': 'Commons image suggester'
}

params = {
    'query': query,
    'format': 'json'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
bindings = data['results']['bindings']

csv_file = 'data/wikipedia_site.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['wikipedia', 'site'])

    for result in bindings:
        target = result['target']['value']
        site = result['site']['value']
        writer.writerow([target, site])

