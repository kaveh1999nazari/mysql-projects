# employee entry and exit company
import datetime
#make connection:
import mysql.connector as sql
connection = sql.connect(host = input('Enter your host =') , 
                         user = input('Enter your user =') , 
                         password = input('Enter password =') , 
                         database = input('Enter your database ='))
cursor = connection.cursor()
#make menu :
def Device_Entry():
    print('Enter your user name :')
    username = input('Enter = ')
    passwrd = input('Enter your password')
    try:
        # employee user:
        sqlcommand123 = 'select * from employee where employee_id = %s'
        cursor.execute(sqlcommand123,(username ,))
        user = cursor.fetchone()
        #admin _entry :
        if username.lower() == 'admin' and passwrd == '12345':
            while True:
                print("""        wellcome                
            choose your option:
                1. add new employee
                2. show all employee
                3. exit""")
                choice = input('Enter your choice = ')
                if choice == '1':
                    sqlcommand = 'insert into employee(first_name , last_name , password) values(%s , %s , %s)'
                    first_name = input('Enter name = ')
                    last_name = input('Enter family = ')
                    paswrd = input(f'Enter password for {first_name} {last_name}')
                    values = (first_name,last_name,paswrd)
                    cursor.execute(sqlcommand,values)
                    print('new employee added.')
                elif choice == '2':
                    sqlcommand = 'select * from employee'
                    cursor.execute(sqlcommand)
                    result = cursor.fetchall()
                    print(f'user_name , first_name , last_name , password')
                    for i in result:
                        employee_id ,first_name , last_name , password = i
                        print(f'{employee_id} , {first_name} , {last_name} , {password}')
                elif choice == '3': break
                else: print('choice correct')
        # employee user entry:
        elif user and user[3] == passwrd:
            print(f'   wellcome {user[1]} {user[2]}    ')
            print('''choice one of them:
        1. Enter
        2. exit''')
            while True:
                choice = input('Enter =')
                if choice == '1':
                    sqlcommand = 'insert into entry(employee_id , time , date) values(%s,%s,%s)'
                    time1 = datetime.datetime.now()
                    time = time1.strftime('%H:%M:%S')
                    date = time1.strftime('%Y-%m-%d')
                    values = (user[0] , time , date)
                    cursor.execute(sqlcommand,values)
                    print(f'good morning dear {user[1]} {user[2]}! enjoy your time!')
                    break
                elif choice == '2':
                    sqlcommand = 'insert into quit(employee , time , date) values(%s,%s,%s)'
                    time1 = datetime.datetime.now()
                    time = time1.strftime('%H:%M:%S')
                    date = time1.strftime('%Y-%m-%d')
                    values = (user[0] , time , date)
                    cursor.execute(sqlcommand,values)
                    print(f'good bye dear {user[1]} {user[2]}')
                    break    
        else :
            print('valid input')
    except sql.Error as e:
        print(e)
Device_Entry()
connection.commit()