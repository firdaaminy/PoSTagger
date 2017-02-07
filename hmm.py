
data_train = "pos.train.txt"
data_test = "pos.test.txt"

list_tag = ["<s>","."]
list_word = []

transition_prob = {
    "<s>" : {},
    "." : {}
}

emission_prob = {}

def calc_prob(prob) :
    for tag in prob :
        total = 0
        for value in prob[tag] :
            total += prob[tag][value]
        for value in prob[tag] :
            prob[tag][value] = prob[tag][value] / total

def learn_param(data_train):
    with open(data_train) as data :
        backpointer_tag = "<s>"
        for datum in data :
            if datum != "\n" :
                word = datum.rsplit(' ',-1)[0] # ngambil word dari line
                tag = datum.rsplit(' ',-1)[-1] # ngambil tag dari line
                tag = tag.replace("\n","")
                if not (tag in list_tag) :
                    list_tag.append(tag)
                if not (word in list_word):
                    list_word.append(word)
                if not (tag in transition_prob) :
                    transition_prob[tag] = {}
                if not (tag in emission_prob) :
                    emission_prob[tag] = {}
                if not(tag in transition_prob[backpointer_tag]) :
                    transition_prob[backpointer_tag][tag] = 1
                else :
                    transition_prob[backpointer_tag][tag] += 1
                if not(word in emission_prob[tag]) :
                    emission_prob[tag][word] = 1
                else :
                    emission_prob[tag][word] += 1
                backpointer_tag = tag
                if(backpointer_tag == ".") :
                    backpointer_tag = "<s>"
        calc_prob(transition_prob)
        calc_prob(emission_prob)

def main():
    learn_param(data_train)
    for x in emission_prob :
        print(x , emission_prob[x])

main()