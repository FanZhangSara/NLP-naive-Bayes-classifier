# coding=utf-8
# coding=utf-8
import sys
file1 = sys.argv[1]

# fakenumber = 0
# truenumber = 0
# negnumber = 0
# posnumber = 0

import json
import math
with open("nbmodel.txt","r") as f:
    data = f.read()
    model = data.split('\n')
    true = json.loads(model[0])
    fake = json.loads(model[1])
    neg = json.loads(model[2])
    print(true)
    print(fake)
    print(neg)
    pos = json.loads(model[3])
    num = json.loads(model[4])
number = num['number'];
print(number)

file=open("nboutput.txt","w")
# with open("dev-text.txt") as f:
with open(file1) as f:


    # totaltruefake = []
    # totaltruefake.append(true.keys())
    # totaltruefake.append(fake.keys())
    truefakelen = len(set(list(true.keys())+list(fake.keys())))

    posneglen = len(set(list(pos.keys())+ list(neg.keys())))

    truetotal = 0
    for key in true:
        truetotal += true[key]

    faketotal = 0
    for key in fake:
        faketotal += fake[key]

    postotal = 0
    for key in pos:
        postotal += pos[key]

    negtotal = 0
    for key in neg:
        negtotal += neg[key]

    content = f.readlines();
    for x in content:
        x = x.strip('\n')
        word = x.split(" ")
        trueValue = math.log(float(number[1]) / float(number[1] + number[0]))
        fakeValue = math.log(float(number[0]) / float(number[1] + number[0]))
        posValue = math.log(float(number[3]) / float(number[2] + number[3]))
        negValue = math.log(float(number[2]) / float(number[2] + number[3]))

        for i in range(1,len(word)):
            # trueValue = math.log(float(number[1])/ float(number[1] + number[0]))
            # fakeValue = math.log(float(number[0]) / float(number[1] + number[0]))
            if word[i] in true or word[i] in fake:
                if word[i] not in true:
                    true[word[i]] = 0
                if word[i] not in fake:
                    fake[word[i]] = 0
                trueValue += math.log(float(true[word[i]]+1) / float(truetotal + truefakelen ))
                fakeValue += math.log(float(fake[word[i]]+1) / float(faketotal + truefakelen ))
            else:
                trueValue += 0
                fakeValue += 0
        file.write(word[0])
        file.write(" ")
        if fakeValue > trueValue:
            file.write("Fake")
        else:
            file.write("True")
        file.write(" ")

        for i in range(1, len(word)):
            if word[i] in pos or word[i] in neg:
                if word[i] not in pos:
                    pos[word[i]] = 0
                if word[i] not in neg:
                    neg[word[i]] = 0
                posValue += math.log(float(pos[word[i]] + 1) / float(postotal + posneglen))
                negValue += math.log(float(neg[word[i]] + 1) / float(negtotal + posneglen))
            else:
                posValue += 0
                negValue += 0

        if posValue > negValue:
            file.write("Pos")
            file.write('\n')
        else:
            file.write("Neg")
            file.write('\n')
file.close()




