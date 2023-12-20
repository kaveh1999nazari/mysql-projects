# create contacts:
#make_connection:
import mysql.connector as sql
connection = sql.connect(host = input('Enter your host =') , user = input('Enter your user =') , password = input('Enter password =') , database = input('Enter your database ='))
cursor = connection.cursor()

# make menu :
def Contact():
    print('       wellcome to contacts      ')
    print('choice your option:')
    print('''1. show your contact
    2. add new contact
    3. search by number
    4. search by name and family
    5. delete contact
    6. close''')

    # choicing user :
    while True:
        choice = int(input('Enter to run :'))
        if choice == 1:
            sqlcommand = """select *
                            from contact"""
            cursor.execute(sqlcommand)
            result = cursor.fetchall()
            print(f'contact_id - first_name - last_name - phone_number1 - phone_number2')
            for i in result:
                contact_id , first_name , last_name , phone_number1 , phone_number2 = i
                print(f'   {contact_id}          {first_name}         {last_name}     {phone_number1}      {phone_number2}')
        elif choice == 2:
            sqlcommand1= """insert into contact (first_name , last_name , phone_number1 , phone_number2) values(%s,%s,%s,%s)"""
            class Contact:
                def __init__(self , first_name , last_name , phone_number1 , phone_number2):
                    self.first_name = first_name
                    self.last_name = last_name
                    self.phone_number1 = phone_number1
                    self.phone_number2 = phone_number2
                def GetInfo(self):
                    return (self.first_name , self.last_name , self.phone_number1 , self.phone_number2)
            first_name = input('Enter first name =')
            last_name = input('Enter last name =')
            phone_number1 = input('Enter phone 1 =')
            phone_number2 = input('Enter phone 2 (optional)=')
            contact = Contact(first_name , last_name , phone_number1 , phone_number2)
            values = contact.GetInfo()
            cursor.execute(sqlcommand1 , values)
        elif choice == 3:
            print('Enter numbers if they are same or different')
            n1 = input('Enter phone number 1 to find =')
            n2 = input('Enter phone number 2 to find =')
            sqlcommand3 = f"""SELECT * 
                            FROM contact
                            where phone_number1 like '{n1}%' or phone_number2 like '{n2}%' """
            cursor.execute(sqlcommand3)
            show = cursor.fetchall()
            print(f'contact_id - first_name - last_name - phone_number1 - phone_number2')
            for i in show:
                contact_id , first_name , last_name , phone_number1 , phone_number2 = i
                print(f'   {contact_id}          {first_name}         {last_name}     {phone_number1}      {phone_number2}')
        elif choice == 4:
            print('Enter first name and last name to find')
            name = input('Enter name =')
            family = input('Enter family =')
            sqlcommand4 = f"""SELECT * 
                            FROM contact
                            where first_name like '%{name}%' and last_name like '%{family}%' """
            cursor.execute(sqlcommand4)
            show1 = cursor.fetchall()
            print(f'contact_id - first_name - last_name - phone_number1 - phone_number2')
            for i in show1:
                contact_id , first_name , last_name , phone_number1 , phone_number2 = i
                print(f'   {contact_id}          {first_name}         {last_name}     {phone_number1}      {phone_number2}')
        elif choice == 5:
            print('choice your contact_id to delete')
            id = int(input('choice to delete:'))
            sqlcommand2 = f"""delete from contact
                            where contact_id = {id}"""
            cursor.execute(sqlcommand2)
            print('successfully delete your custom contact.')
        elif choice == 6:break
        else:
            print('choice correct!')
Contact()
connection.commit()