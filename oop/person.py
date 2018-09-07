import uuid

class Person:
    def __init__(self,gender,age):
        self.gender=gender
        self.age=age
    def voice(self):
        if self.gender.lower()=="male":
            return "Deep voice"
        elif self.gender.lower=="female":
            return "soft voice"
        else :
            return "gender type is either male or female"
#new_person=Person("Male",24)
#print(new_person.voice())
class User(Person):
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id
class GuestList(User):
    def __init__(self):
        self.guest_list=list()
        
    def add_user(self,user_name):
        self.user_name=user_name
        new_user={
            "user_id": str(uuid.uuid1()),
            "user_name":self.user_name
        }
        self.guest_list.append(new_user)
        return self.guest_list
 #The commented lines below create a new user chris with both a user id and a user name       
#guest=GuestList()
#print (guest.add_user("chris"))
    def get_users(self):
        return self.guest_list
    def delete_user(self,user_id):
        self.user_id=user_id
        for guest in self.guest_list:
            if guest['user_name']==self.user_name:
                self.guest_list.remove(guest)
                return ("user deleted successfully")
            else:
                return "user doesnt exist"
'''
guest=GuestList()
print (guest.add_user("chris"))
print (guest.add_user("joel"))
print (guest.add_user("faith"))
print (guest.delete_user("chris"))
print (guest.get_users())
'''
    

