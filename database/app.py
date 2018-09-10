from database import DatabaseConnection

db = DatabaseConnection()
print(db)

# update=db.update_table_data('Event', 'event_name','baby shower',5)
# print(update);

# new_user = db.create_user('Phillips', 'Kigenyi', 'phil111@levelup.andela', 'kp.pk', '27', '2018-08-25')
# print(new_user)
# print(db.get_user_by_user_id(205))

# table_data = db.get_all_table_data('users')
# for lis_tup in table_data:
#    print(lis_tup)

# print(table_data)

# new_event=db.create_event('my bd', '$4500', 'kawempe')
# print(new_event)

# new_ticket=db.create_ticket(204,5,'$20','1/2/19')
# print(new_ticket)

# The function call below enables a user query his/her tickets for his/her events
'''
user_query=db.get_user_events('204')
lis_tupo: object
for lis_tupo in user_query:
    print({"Event Name": lis_tupo[0], "Event_id": lis_tupo[1], "ticket_id": lis_tupo[2]})
'''
