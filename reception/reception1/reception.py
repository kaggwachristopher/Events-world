class Reception:
    def __init__(self):  
        self.vip=[]
        self.ordinary=[]
    def vip_guest(self):
        vip_file=open('guest_lists/vip_list.txt')       
        for full_name in vip_file:
            self.vip.append(full_name.strip('\n'))
        return self.vip

    def store_ordinary(self):
        ordinary_names_in_file=open('guest_lists/ordinary_list.txt')
        for full_name in ordinary_names_in_file:
            self.ordinary.append(full_name.strip('\n'))
        return self.ordinary
    
    def validation(self,name):
        if " " in name:
            raise TypeError
            
    def registration_checker(self,person_name):
        vip_names=[]
        ordinary_names=[]
        ordinary_names=self.store_ordinary()
        vip_names=self.vip_guest()
        for full_name_1 in vip_names:
            if person_name in full_name_1.casefold():
                return full_name_1+" VIP"
            else:
                pass
        for n in ordinary_names:
            if person_name in full_name_2.casefold():
                return full_name_2+" ordinary"
        else:
            return person_name+" Not Registered"
    def check_function(self):
        if self.registration_checker("string"):
            return True
        else:
            return False

            #the statements below run the app

# guest=Reception()            
# while True:
#    print(guest.registration_checker(input("Enter a single name: ")))