
data_train = "pos.train.txt"
data_test = "pos.test.txt"
list_tag = []

with open(data_train) as data :
    for datum in data :
        tag = datum.rsplit(' ',1)[-1]
        if not tag in list_tag :
            list_tag.append(tag)
            print(tag)
