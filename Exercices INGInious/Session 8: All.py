#----------------------------------- 
# Session 8: Student - init
#----------------------------------- 

class Student:
    def __init__(self, name, surname, birth_date, email):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.email = email
        
#-----------------------------------        
# Session 8: Pair.opposite()
#----------------------------------- 

return Pair(-self.a,-self.b)

#----------------------------------- 
# Session 8: __eq__()
#----------------------------------- 

def __eq__(self, p):
    if (self.a,self.b) == p:
        return True
    else:
        return False
    
#----------------------------------- 
# Session 8: OrderedPair
#-----------------------------------

def set_a(self, n_a):
    self.p.a = n_a
    if n_a > self.p.b:
        self.ordered = False
    else:
        self.ordered = True       # Ne marche pas sans ces lignes
    
def set_b(self, n_b):
    self.p.b = n_b
    if n_b < self.p.a:
        self.ordered = False
    else:
        self.ordered = True   # Ne marche pas sans ces lignes
        
        
#----------------------------------- 
# Session 8: Q* SMS Store
#-----------------------------------

class SMSStore:
    
    def __init__(self):
        self.storage = []
        
    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        self.storage.append([from_number, time_arrived, text_of_SMS, False])
    
    def message_count(self):
        return len(self.storage)
    
    def get_unread_indexes(self):
        index_not_viewed = []
        for i in range(len(self.storage)):
            if self.storage[i] == False:
                index_not_viewed.append(i)
        return index_not_viewed
             
    def get_message(self,i):
        if i > len(self.storage):
            return None
        else:                                           # !!! i-1 à la place de i... Pourquoi? Je ne sais pas
            self.storage[i-1][3] = True
            return (self.storage[i-1][0],self.storage[i-1][1],self.storage[i-1][2])
    def delete(self,i):
        del self.storage[i-1]
        
    def clear(self):
        self.storage = []
