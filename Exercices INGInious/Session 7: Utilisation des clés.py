def get_country(l,name):
    for i in range(len(l)):
        if l[i]["City"] == name:
            return l[i]["Country"]
    return False
