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
        for j in range (k,len(reversed_list)):                      #
            if reversed_list[j][0]==reversed_list[k-1][0]:          #
                top_list.append(reversed_list[j])                   #
    return top_list
