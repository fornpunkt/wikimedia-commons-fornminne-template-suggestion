import csv
import datetime

results = list()
with open('data/image_site.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        title = row[0]
        description_page = row[1]
        thumbnail = row[2]
        snippet = row[3]
        uuid = row[4].split('/')[-1]

        row_template = f'''<tr class="align-middle">
                    <td><img src="{thumbnail}" decoding="async" loading="lazy"></td>
                    <td class="w-25"><a href="{description_page}">{title}</a></td>
                    <td><a href="https://fornpunkt.se/raa/lamning/{uuid}">{uuid}</a></td>
                    <td class="w-25">{snippet}</td>
                    <td>
                        <div class="input-group">
                            <input type="text" readonly class="form-control" value="{'{{{{'}Fornminne|{uuid}{'}}}}'}">
                            <button class="btn btn-secondary clipboardButton" type="button">Kopiera</button>
                        </div>
                    </td>
                </tr>'''

        results.append(row_template.format(**locals()))

with open('template.html', 'r') as file:
    html = file.read()
    html = html.replace('{timestamp}', datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    html = html.replace('{table}', '\n'.join(results))

with open('output/index.html', 'w') as file:
    file.write(html)

print('Done!')
