import xml.etree.ElementTree as ET
tree = ET.parse('./input/kowiki-20180401-pages-articles-multistream.xml')
print('opend')
root = tree.getroot()
print('parsed')

count = 0
for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'):
    title = page.find('{http://www.mediawiki.org/xml/export-0.10/}title')
    page = page.find('{http://www.mediawiki.org/xml/export-0.10/}id')
    revision = page.find('{http://www.mediawiki.org/xml/export-0.10/}revision')
    allText = revision.find('text')
    if '{{축구 선수 정보' in allText:
        print(title.text)
        print(page.text)
        count = count+1
print(count)
