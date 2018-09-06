class Reception:
    def __init__(self):  
        self.vip=[]
        self.ordinary=[]
    def store_vip(self):
        temp_vip=open('guest_lists/vip_list.txt','r')       
        for line in temp_vip:
            self.vip.append(line.strip('\n'))
        return self.vip

    def store_ordinary(self):
        temp_ordinary=open('guest_lists/ordinary_list.txt','r')
        for line in temp_ordinary:
            self.ordinary.append(line.strip('\n'))
        return self.ordinary
    
    def validation(self,name):
        if " " in name:
            raise TypeError
            
      
    def registration_checker(self,enter_name):
        vip_names=[]
        ordinary_names=[]
        ordinary_names=self.store_ordinary()
        vip_names=self.store_vip()
        for nm in vip_names:
            if enter_name in nm.casefold():
                return nm+" VIP"
            else:
                pass
        for n in ordinary_names:
            if enter_name in n.casefold():
                return n+" ordinary"
        else:
            return enter_name+" Not Registered"

people=Reception()
print (people.registration_checker(input('Enter name: ')))      