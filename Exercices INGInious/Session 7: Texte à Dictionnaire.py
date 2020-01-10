def create_dictionary(filename):
    d = {}
    flat_list = []
    with open(filename,"r") as fin:
        for line in fin:
            for word in line.split():
                flat_list.append(word)
        for mot in flat_list:
            if d.get(mot,0) == 0:
                d[mot] = 1
            else :
                d[mot] +=1
        
        return d


def occ(dictionary, word):
    return dictionary.get(word,0)
