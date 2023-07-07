import csv

import requests


def get_images_url(category):
    return f'https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&generator=search&utf8=1&formatversion=2&iiprop=url&gsrsearch=incategory%3A{category}%20-incategory%3AArchaeological_monuments_in_Sweden_with_UUIDs%20-incategory%3AFoP-Sweden%20-incategory%3AExtracted_images&gsrnamespace=6&gsrlimit=500&gsrprop=snippet&iiurlwidth=200'

headers = {
    'User-Agent': 'Commons image suggester'
}

results = list()
with open('data/category_site.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        category = row[0]
        site = row[1]
        
        response = requests.get(get_images_url(category))
        data = response.json()
        if not 'query' in data:
            continue
        data = data['query']['pages']
        for image in data:
            if not 'imageinfo' in image:
                continue
            title = image['title']
            url = image['imageinfo'][0]['descriptionurl']
            thumbnail = image['imageinfo'][0]['thumburl']
            snippet = image['snippet']
            results.append([title, url, thumbnail, snippet, site])

csv_file = 'data/image_site.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'url', 'tumbnail', 'snippet', 'site'])
    for item in results:
        writer.writerow(item)
