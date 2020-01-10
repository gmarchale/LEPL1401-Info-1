def translate(data,lan):
    data = data.lower()
    data = data.split(" ")
    trad= ""
    tmplist =""
    
    for mot in data:
        if mot in lan:
            tmplist = lan[mot] + " "
            trad+=tmplist
        else:
            trad+=mot+ " "
    return trad
