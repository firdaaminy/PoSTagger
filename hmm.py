
data_train = "pos.train.txt"
data_test = "pos.test.txt"

'''
list_tag = [
    ["<s>", "<e>"], #tags
    [{},{}], #transition prob
    [{},{}] #emmision prob
]
with open(data_train) as data :
    backpointer_word = "<s>"
    for datum in data :
        word = datum.rsplit(' ',-1)[0] # ngambil word dari line
        tag = datum.rsplit(' ',-1)[-1] # ngambil tag dari line
        tag = tag.replace("\n","")
        if datum != "" :
            if not tag in list_tag[0] :
                list_tag[0].append(tag)
                list_tag[1].append({})
                list_tag[2].append({})

            x = list_tag[0].index(backpointer_word)
            if tag in list_tag[1][x]:
                list_tag[1][x][tag] += 1
            else:
                list_tag[1][x][tag] = 1

            if word in list_tag[2] :
                y = list_tag[2][x][word]
                if backpointer_word in y :
                    y[backpointer_word] += 1
                else :
                    y[backpointer_word] = 1
            else :
                list_tag[2][x][word] = {}

            backpointer_word = tag

    #print(list_tag)
    for x in list_tag[2] :
        for y in x :
            print(y , "\n")
        print("\n\n")
'''

list_tag = {
    "." : ["<s>" , "."]
}

transition_prob = {
    "<s>" : {},
    "." : {}
}

emission_prob = {

}

with open(data_train) as data :
    backpointer_tag = "."
    backpointer_word = "<s>"
    for datum in data :
        if datum != "\n" :

            word = datum.rsplit(' ',-1)[0] # ngambil word dari line
            tag = datum.rsplit(' ',-1)[-1] # ngambil tag dari line
            tag = tag.replace("\n","")
            if not (tag in list_tag) :
                list_tag[tag] = []
            if not (word in list_tag[tag]):
                list_tag[tag].append(word)
            if not (word in transition_prob) :
                transition_prob[word] = {}
            if not (word in emission_prob) :
                emission_prob[word] = {}

            if not(word in transition_prob[backpointer_word]) :
                transition_prob[backpointer_word][word] = 1
            else :
                transition_prob[backpointer_word][word] += 1

            if not(backpointer_tag in emission_prob[word]) :
                emission_prob[word][backpointer_tag] = {}

            if not(tag in emission_prob[word][backpointer_tag]) :
                emission_prob[word][backpointer_tag][tag] = 1
            else :
                emission_prob[word][backpointer_tag][tag] += 1

            backpointer_word = word
            backpointer_tag = tag
            if(backpointer_word == ".") :
                backpointer_word = "<s>"

    for x in list_tag :
        print(x , list_tag[x])