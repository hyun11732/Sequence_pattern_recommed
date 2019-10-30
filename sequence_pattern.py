from itertools import product

def cut_minsup(dic, minsup) :
    words = dic.keys()
    for word in list(words):
        if dic[word] < minsup :
            del dic[word]
    return dic


def sequence_words(inputs, length) :
    dic = dict()
    temp = []
    for line in inputs :
        for i in range(len(line) - length + 1) :
            item = tuple(line[i : i + length])
            if item not in dic :
                dic[item] = 1
            else :
                dic[item] += 1
    return dic

if __name__ == "__main__" :
    minsup = 2
    string = input()
    inputs = []
    while string or string == "" :
        temp = string.split()
        inputs.append(temp)
        try :
            string = input()
        except :
            break
    dic = dict()
    dic.clear()
    sequence_input = []
    for i in range(2, 6) :
        dic.update(sequence_words(inputs, i))
    dic = cut_minsup(dic, minsup)
    sort_keys = sorted(dic, key = lambda l : (-dic[l], l))
    count = 0
    for keys in sort_keys :
        print("[", dic[keys], end = ", ", sep ="")
        string = ""
        for key in keys :
            string += key + " "
        string = string[:-1]
        print("'", string, "']", sep ="")
        count += 1
        if count == 20 :
            break