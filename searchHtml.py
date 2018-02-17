import re
from collections import Counter

pattern = re.compile('(aws|cloud|devops|virtualization|visualization|xml|scraping|webpage|html|jira)')
pages = {}
wordList = []
class PageDetails():

    def getPages(self):
        for i in range(1,101):
            f=open('./contentHTML/file'+str(i)+'.txt')
            data = f.read()
            words = pattern.findall(data)
            global wordList
            wordList = wordList + words
            pages['page'+str(i)] = {'count': len(words), 'keys': words}
        print(pages)
        return pages

    def avg(self):
        pages = self.getPages()
        sum =0
        for i in range(1,101):
            sum = sum+ pages['page'+str(i)]['count']
        
        average = round(sum/100)
        return average

    def pagesEqualstoAvg(self,average):
        files = []
        for i in range(1,101):
            if(pages['page'+str(i)]['count']==average):
                files.append(i)
        return files

page = PageDetails()
avg = page.avg()
print("Average keys per Page is %d"%avg)
files = page.pagesEqualstoAvg(avg)
print("Below are the pages that has count of keywords equals to average")
for i in files:
    print("file"+str(i)+'.html')

print('Below are the keywords occurs maximum and minimum:')
occurance = Counter(wordList)
items = list(occurance.items())
frequency =list(occurance.values())
max_key = items[frequency.index(max(frequency))]
min_key = items[frequency.index(min(frequency))]
print(max_key, min_key)