def winning_house(scroll): # Pas Compris
    sc={}
    houses=['gryffindor','ravenclaw','hufflepuff','slytherin']
    for a in houses:
        sc[a]=0
    f=open(scroll,"r")
    l=f.readlines()
    f.close()
    for i in l:
        i.rstrip("\n")
        i=i.split(" ")
        if i[0] in students['gryffindor']:
            sc['gryffindor']+= float(i[1])
        elif i[0] in students['ravenclaw']:
            sc['ravenclaw']+=float(i[1])
        elif i[0] in students['hufflepuff']:
            sc['hufflepuff']+= float(i[1])
        elif i[0] in students['slytherin']:     
            sc['slytherin']+= float(i[1])
            
    max=sc['gryffindor']
    winner=[]
    for j in sc :
        if sc[j]>max:
            max=sc[j]
    for k in sc:
        if sc[k]==max:
            winner.append(k)
    if len(winner)==1:
        return (winner[0])
    return (winner)
