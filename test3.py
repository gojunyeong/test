import xml.etree.ElementTree as ET



tree = ET.parse('./input/kowiki-20180401-pages-articles-multistream.xml')
print('opend')
root = tree.getroot()
print('parsed')



    

    
def getInfobox(text):
    startStatus = False
    startIndex = 0
    lastIndex = 0
    braketCount = 0
    template = list()
    infoBox = ''
    for index, char in enumerate(text):
        if '{' == char:
            braketCount += 1
            if not startStatus:
                startIndex = index
                startStatus = True
        elif '}' == char:
            braketCount -= 1
            if startStatus and braketCount == 0:
                lastIndex = index+1
                template.append(text[startIndex:lastIndex])
                startStatus = False
    for text in template:
        if '축구 선수 정보' in text:
            infoBox = text
    return infoBox





count = 0
for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'):
    title = page.find('{http://www.mediawiki.org/xml/export-0.10/}title')
    id = page.find('{http://www.mediawiki.org/xml/export-0.10/}id')
    allText = page.find('{http://www.mediawiki.org/xml/export-0.10/}revision').find(
        '{http://www.mediawiki.org/xml/export-0.10/}text')

    if allText.text is not None and'축구 선수 정보' in allText.text:
        print(title.text)
        print(id.text)
        getInfobox(allText.text)
        count = count+1
print(count)
