
data_train = "pos.train.txt"
data_test = "pos.test.txt"

#list_tag = ["<s>","."]
#list_word = []

transition_prob = {
    "<s>" : {"<s>" : 0, "." : 0},
    "." : {"<s>" : 0, "." : 0}
}

emission_prob = {
    "<s>" : {},
    "." : {}
}

def calc_prob(prob) :
    for tag in prob :
        total = 0
        for value in prob[tag] :
            if prob[tag][value] != 0 :
                total += prob[tag][value]
        for value in prob[tag] :
            if prob[tag][value] != 0 :
                prob[tag][value] = prob[tag][value] / total

def learn_param(data_train):
    with open(data_train) as data :
        backpointer_tag = "<s>"
        for datum in data :
            if datum != "\n" :
                word = datum.rsplit(' ',-1)[0] # ngambil word dari line
                tag = datum.rsplit(' ',-1)[-1] # ngambil tag dari line
                tag = tag.replace("\n","")

                #if not (tag in list_tag) :
                #    list_tag.append(tag)
                #if not (word in list_word):
                #    list_word.append(word)

                if not (tag in transition_prob) :
                    transition_prob[tag] = {}
                if not (tag in emission_prob) :
                    emission_prob[tag] = {}

                for x in transition_prob :
                    if not(tag in transition_prob[x]) :
                        transition_prob[x][tag] = 0
                for x in emission_prob :
                    if not(word in emission_prob[x]) :
                        emission_prob[x][word] = 0

                if tag in transition_prob[backpointer_tag] :
                    transition_prob[backpointer_tag][tag] += 1
                if word in emission_prob[tag] :
                    emission_prob[tag][word] += 1

                backpointer_tag = tag
                if(backpointer_tag == ".") :
                    backpointer_tag = "<s>"

        calc_prob(transition_prob)
        calc_prob(emission_prob)

def viterbi(sentence, transition_prob, emission_prob):
    words = sentence.split()
    words[-1] = words[-1][:-1]
    words.append(".")

    best_score = {}
    best_edge = {}
    best_score[0]["<s>"] = 0
    best_edge[0]["<s>"] = None
    for i in range (0,len(words)):
        for prev in transition_prob :
            found = False
            for next in transition_prob :
                if prev in best_score[0] and next in transition_prob[prev] :
                    print(next)
                    score = 0
                    if(words[i] in emission_prob[next]) :
                        score = best_score[0][prev] + transition_prob[prev][next] * emission_prob[next][words[i]]
                        if best_score[next] > score :
                            best_score[next] = score
                            best_edge[next] = prev
                        found = True
                if not found :
                    score = best_score[0][prev] + transition_prob[prev]["NNP"] * 1
                    if best_score[next] > score :
                        best_score[next] = score
                        best_edge[next] = prev

    tags = []
    next_edge = best_edge["."]
    while next_edge != "<s>" :
        tags.append(next_edge)
        next_edge = best_edge[next_edge]
    tags.reverse()
    print(tags)

def testing(data_test):
    with open(data_test) as data_test2:
        true_positive = 0
        false_positive = 0
        false_negative = 0
        i = 0
        test_word_list = {0: []}
        test_tag_list = []
        viterbi_list = []
        for line in data_test2:
            if line != "\n" :
                word = line.rsplit(' ',-1)[0] # ngambil word dari line
                tag = line.rsplit(' ',-1)[-1] # ngambil tag dari line
                tag = tag.replace("\n","")
                test_word_list[i].append(word)
                test_tag_list[i].append(tag)
            else:
                viterbi_list.append(viterbi(test_word_list, transition_prob, emission_prob))
                i+=1
                test_word_list = []
        for i in range(0, len(test_tag_list)):
            if test_tag_list[i] == viterbi_list[i]:
                true_positive+=1
            else:
                false_negative+=1
                false_positive+=1
        print('Precision: ',(true_positive/(true_positive+false_positive))*100,' %')
        print('Recall: ',(true_positive/(true_positive+false_negative))*100,' %')
        print('Accuracy: ',((true_positive+0)/(true_positive+false_negative+false_negative+0))*100, ' %')


def main():
    learn_param(data_train)
    viterbi("Rockfell International.", transition_prob, emission_prob)

main()