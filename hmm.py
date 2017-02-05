
data_train = "pos.train.txt"
data_test = "pos.test.txt"
list_tag = [
    ["<s>", "<e>"], #tags
    [{},{}], #transition prob
    [{},{}] #emmision prob
]

with open(data_train) as data :
    backpointer = "<s>"
    for datum in data :
        word = datum.rsplit(' ',-1)[0] # ngambil word dari line
        tag = datum.rsplit(' ',-1)[-1] # ngambil tag dari line
        tag = tag.replace("\n","")
        if datum != "" :
            if not tag in list_tag[0] :
                list_tag[0].append(tag)
                list_tag[1].append({})
                list_tag[2].append({})

            x = list_tag[0].index(backpointer)
            if tag in list_tag[1][x]:
                list_tag[1][x][tag] += 1
            else:
                list_tag[1][x][tag] = 1

            if word in list_tag[2] :
                y = list_tag[2][x][word]
                if backpointer in y :
                    y[backpointer] += 1
                else :
                    y[backpointer] = 1
            else :
                list_tag[2][x][backpointer] = {}

            backpointer = tag

    #print(list_tag)
    for x in list_tag[1] :
        print(x)

