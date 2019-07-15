def getText():
    txt=open("text.txt","r",encoding="UTF-8").read()
    txt.lower()
    for each in txt:
        if each in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            each=" "
    return txt
target=getText()
words=target.split()
print("words 's type is:",type(words))
print("words 's number is:",len(words))
countDict={}
for word in words:
    #get(key,default value),default value is a value when the return value corresponding to a key is non-existential
    countDict[word]=countDict.get(word,0)+1
#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
items=list(countDict.items())

items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))