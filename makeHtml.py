import os
from faker import Faker
from random import choice, randint
fake = Faker()

class Pages():
    def keywords(self):
        keys = ['cloud', 'devops', 'virtualization', 'visualization', 'aws', 'xml', 'scraping', 'webpages', 'html', 'jira']
        count = [6,7,8]
        words = []
        iteration = choice(count)
        i =0
        while (i<iteration):
            k = choice(keys)
            if k not in words:
                words.append(k)
                i+=1
        return words
    def getIndex(self,l):
        total = l
        windex = []
        i = 1
        j =0
        while(i<total):
            windex.append(randint(j,j+99))
            j+=100
            if(i%5==0 and i>0):
                j =0
            i+=1
        return windex
    
    def insert(self):
        words = self.keywords()
        index = self.getIndex(len(words)+1)
        lines = []
        print(len(words),index)
        for i in range(500):
            line = []
            for j in range(7):
                line.append(fake.word())
            text = ' '.join(line)
            if i in index:
                f.write(words.pop()+" ")
            f.write(text+"<br>")


for i in range(1,101):
    os.makedirs('./plainHtml', exist_ok=True)
    f = open('./plainHtml/file'+str(i)+'.html','w')
    f.write("""<html>
    <head></head>
    <body><p>""")
    page = Pages()
    page.insert()
    f.write("</p></body></html>")