def topk_words(words, k):
    dict = {}
    for mot in words:
        dict[mot] = dict.get(mot,0) + 1
    
    flat_list = list(dict.items())
    tmplist = []
    for i in range(len(flat_list)):
        tmplist.append((flat_list[i][1],flat_list[i][0]))
    reversed_list = sorted(tmplist,reverse=True)
    
    top_list = []
    if k >= len(flat_list):
        return reversed_list
    else:
        for i in range(k):
            top_list.append(reversed_list[i])
        for j in range (k,len(reversed_list)):                      # Cette partie sert à s'occuper du cas ou le k ème mot 
            if reversed_list[j][0]==reversed_list[k-1][0]:          # de top_list n'est pas le seul avec cette occurence
                top_list.append(reversed_list[j])                   # Par exemple si k = 2 et que dans la liste il y a 3 fois "A", 2 fois "B"
                                                                    # et 2 fois "C". Alors la fonction renverra une liste de taille k+1
    return top_list                                                 
