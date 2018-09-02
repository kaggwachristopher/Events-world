while True:
    

    class Ordinary:
        def ordinary_guest():
            ordinary_list_text_file=open("guest lists/ordinary_list.txt")
            ordinary_file_content=ordinary_list_text_file.read()
            ordinary_guest_names_list=[]
            
            ordinary_guest_names_list=ordinary_file_content.split("\n")
            for person in ordinary_guest_names_list:
                if person_name.lower() in person.lower():
                    return (person+", Ordinary")
                else:
                    pass
    class VIP:
        def vip_guest():
            vip_list_text_file=open("guest lists/vip_list.txt")
            vip_file_content=vip_list_text_file.read()
            vip_guest_names_list=[]
            vip_guest_names_list=vip_file_content.split("\n")
            for guest in vip_guest_names_list:
                        if person_name.lower() in guest.lower():
                            return (guest+", VIP")
                        else:
                            pass
                        
    def registration_checker():
        
        if Ordinary.ordinary_guest():
            return(Ordinary.ordinary_guest())
        elif VIP.vip_guest():
            return(VIP.vip_guest())
        else:
            return "Not registered"
        
    person_name=input("Enter a single name: ")
    print(registration_checker())
    
