
data_train = "pos.train.txt"
data_test = "pos.test.txt"
list_tag = [
    ["<s>", "<e>"], #tags
    [{},{}], #transition prob
    [{},{}] #emmision prob
]

with open(data_train) as data :
    backpointer = "<s>"
    #print(list_tag[1][0])
    for datum in data :
        word = datum.rsplit(' ',1)[0]
        tag = datum.rsplit(' ',1)[-1]
        if tag in list_tag[0] :
            x = list_tag[0].index(backpointer)
            if tag in list_tag[1][x] :
                list_tag[1][x][tag] += 1
            else :
                list_tag[1][x][tag] = []
        else :
            list_tag[0].append(tag)
            list_tag[1].append({})
            list_tag[2].append({})
        backpointer = tag


    print(list_tag)