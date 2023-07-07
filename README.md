# Bilder föreställande kulturlämningar?

Program som genererar en lista över bilder som *kanske* föreställer kulturlämningar men samtidigt saknar mallen `{{Fornminne}}` på Wikimedia Commons.

## Användning

Programmet är uppdelat i flera steg som måste köras i ordning.

Programmet kräver Python 3 och biblioteket `requests`. Installera biblioteket med `pip install requests`. 

```bash
python get_sites_with_wikipedia_articles.py
python get_sites_with_categories.py
python get_sites_with_images.py
python generate_table.py
```