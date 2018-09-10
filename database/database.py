import psycopg2
import random


class DatabaseConnection:

    def __init__(self):
        connection_credentials = """
        dbname='db' user='postgres' password='idontgiveadamnwhatyouthink'
         host='localhost' port='5432'
         """
        try:
            self.connection = psycopg2.connect(connection_credentials)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('\n\nConnected to Database\n\n')
        except Exception as e:
            print(e.message)
            print("Failed to connect to db")

    def create_user(self, first_name, last_name,email,password, age, created_at):
        insert_user_command = """
        INSERT INTO users (first_name, last_name, email,password, age, created_at) 
        VALUES ('{}', '{}','{}', '{}','{}','{}');
        """.format(first_name, last_name, email,password, age, created_at)
        self.cursor.execute(insert_user_command)
        id_fetch = """
        select user_id from users where email='{}'
        """.format(email)
        execution = self.cursor.execute(id_fetch)
        fetched_id=self.cursor.fetchone()
        return "New user created successfully with user id {}".format(fetched_id[0])

    def create_event(self,event_name, price, location):
        insert_user_command = """
        INSERT INTO Event (event_name, price, location) 
        VALUES ('{}', '{}', '{}');
        """.format(event_name, price, location)
        self.cursor.execute(insert_user_command)
        return "new event {} created successfully".format(event_name)

    def get_all_table_data(self,table_name):
        user_command = """
        SELECT * FROM {};
        """.format(table_name)
        self.cursor.execute(user_command)
        table_data = self.cursor.fetchall()
        return table_data

    def get_user_by_user_id(self, user_id):
        user_command = """
        SELECT * FROM users WHERE user_id= '{}';
        """.format(user_id)
        self.cursor.execute(user_command)
        user = self.cursor.fetchone()
        return user

    def update_table_data(self,table_name,column_name,update,primary_id):
        if table_name=="users" or table_name=="Ticket":
            user_command="""
            Update {} set {}='{}' where user_id='{}' 
            """.format(table_name, column_name, update, primary_id,)
            self.cursor.execute(user_command)
            return column_name+" succesfully updated"
        elif table_name == "Event":
            user_command="""
            Update {} set {}='{}' where event_id='{}' 
            """.format(table_name, column_name, update, primary_id,)
            self.cursor.execute(user_command)
            return column_name+" succesfully updated"

    def create_ticket(self, user_id, event_id, price, created_at):
            verification_code = int(random.uniform(1111111, 9999999))
            ticket_id=int(random.uniform(11111111,99999999))
            insert_user_command = """
            INSERT INTO Ticket (ticket_id, user_id,event_id, price, created_at,verification_code) 
            VALUES ('{}','{}','{}','{}','{}','{}');
            """.format(ticket_id, user_id, event_id, price, created_at, verification_code)
            self.cursor.execute(insert_user_command)
            return "New Ticket created successfully for user {} with ticket_id {}".format(user_id,ticket_id)

    def get_user_events(self, user_id):
        
        user_command='''
        select Event.event_name,Event.event_id,Ticket.ticket_id
        from
        Ticket
        inner join Event
        on Ticket.event_id=Event.event_id
        where
        user_id='{}'
        '''.format(user_id)
        self.cursor.execute(user_command)
        data=self.cursor.fetchall()
        return data

