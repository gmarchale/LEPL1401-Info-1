def write_coordinates(filename, l):
    with open(filename,"r") as f:
        for i in l:
            f.write(l[i][0],l[i][1],"\n")


def read_coordinates(filename):  #Pas très beau mais fonctionne
    l = []
    with open(filename,"r") as f:
        flist = f.readlines()
        for i in flist:
            l.append(i, i+1)
            i+=1
    return l

def read_coordinates(filename):  #Méthode plus jolie
    l = []
    with open(filename,"r") as f:
        for line in f:
            b=line.rstrip('\n')
            x=b.split(",")
            l.append((float(x[0]),float(x[1])))
    return l
