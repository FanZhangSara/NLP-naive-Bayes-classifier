# coding=utf-8
import sys
file = sys.argv[1]
import json
array = []
# fakenumber = 0
# truenumber = 0
# negnumber = 0
# posnumber = 0
number=[0,0,0,0]
total = 0
true={}
fake={}
neg={}
pos={}
def trueOrFake(word):
    if word[1]=='Fake':
        number[0]+=1
        for x in range(3,len(word)):
            if word[x] in fake:
                fake[word[x]]+=1
            else:
                fake[word[x]]=1

    else:
        number[1] += 1
        for x in range(3,len(word)):
            if word[x] in true:
                true[word[x]]+=1
            else:
                true[word[x]]=1


    if word[2]=='Neg':
        number[2] += 1
        for x in range(3,len(word)):
            if word[x] in neg:
                neg[word[x]]+=1
            else:
                neg[word[x]]=1
    else:
        number[3] += 1
        for x in range(3,len(word)):
            if word[x] in pos:
                pos[word[x]]+=1
            else:
                pos[word[x]]=1


# with open("train-labeled.txt","r") as f:
with open(file, "r") as f:
    content = f.readlines()
    for x in content:
        total += 1
        x = x.strip('\n')
        word = x.split(" ")
        array.append(word[0]);
        trueOrFake(word);
    print(number)
    print(total)
    print(true)
    print(fake)
    print(neg)
    print(pos)


import json
listdic={}
listdic["number"]=number
jsObj1 = json.dumps(true)
jsObj2= json.dumps(fake)
jsObj3 = json.dumps(neg)
jsObj4 = json.dumps(pos)
jsObj5 = json.dumps(listdic)

fileObject = open("nbmodel.txt","w")
#fileObject = open("dict_f.json","w")
fileObject.write(jsObj1)
fileObject.write('\n')
fileObject.write(jsObj2)
fileObject.write('\n')
fileObject.write(jsObj3)
fileObject.write('\n')
fileObject.write(jsObj4)
fileObject.write('\n')
fileObject.write(jsObj5)