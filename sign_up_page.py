import mysql.connector as mysql
import string
import random
class Email:
    def __init__(self,user_name:str,email:str,password:str):
        self.user_name = user_name
        self.email = email
        self.password = password
    def Info(self):
        return (self.user_name,self.email,self.password)
# make menu:
print('     WELLCOME TO SIGN UP PAGE    ')
print(f"""choice your menu:
1. getting your information and sign up
2. change your password
3. show your information 
4. type of your email
5. delete your account
6. exit""")
# function for checking input :
def Check(user_name,password):
    sqlcommand = 'select user_name , passwrd from email where user_name = %s and passwrd = %s'
    values = (user_name,password)
    cursor.execute(sqlcommand,values)
    check = cursor.fetchone()
    return check
# make connection :
connection = mysql.connect(host = input('Enter your host =') , 
                         user = input('Enter your user =') , 
                         password = input('Enter password =') , 
                         database = input('Enter your database ='))
cursor = connection.cursor()

# make options :
while True:
    choice = int(input('enter your choice ='))
    if choice == 1:
        user_name = input('Enter your user_name =')
        email = input('Enter your Email =')
        print('choice your password type: \n1.random password\n2.your custom password')
        ask = int(input('enter your choice ='))
        if ask == 1:
            lenght = int(input('Enter lenght of your password ='))
            password = ''.join(random.choice(string.ascii_letters + string.digits)for i in range(lenght))
        elif ask == 2:
            password = input('Enter your password =')
        sqlcommand1 = 'insert into email (user_name , email,passwrd) values (%s,%s,%s)'
        obj = Email(user_name,email,password)
        values = obj.Info()
        cursor.execute(sqlcommand1,values)
        print('succefully registered')
    # change user password by them user_name
    elif choice == 2:
        # check password for enter :
        print('Enter your user_name and current password')
        user_name = input('Enter your user_name =')
        password = input('Enter your password =')
        #check:
        check = Check(user_name,password)
        #your enter:
        x = (user_name,password)
        #control if is correct:
        if x == check :
            sqlcommand2 = 'update email set passwrd = %s  where user_name =%s '
            new_pass = input('Enter your new password =')
            value = (new_pass,user_name)
            cursor.execute(sqlcommand2,value)
        else:
            print('invalid input')
    # show user information
    elif choice == 3:
        print('Enter your user_name and password to show your email')
        user_name = input('Enter your user_name =')
        password = input('Enter your password =')
        check = Check(user_name,password)
        x = (user_name,password)
        if check == x:
            sqlcommand3 = 'select email from email'
            cursor.execute(sqlcommand3)
            result = cursor.fetchall()
            for i in result:
                i = email
                print(f'user name = {user_name} \n{email}')
        else:
            print('invalid input')
    # type email
    elif choice == 4:
        print('Enter your user_name and password to show your email type')
        user_name = input('Enter your user_name =')
        password = input('Enter your password =')
        check = Check(user_name,password)
        x = (user_name,password)
        if check == x:
            sqlcommand3 = 'select email from email'
            cursor.execute(sqlcommand3)
            result = cursor.fetchall()
            for i in result:
                i = email
                x = i.split('@')
                y = x[1].split('.')
                print(f'type of your email is : {y[0]}')
        else:
            print('invalid input')
    # delete user account
    elif choice == 5:
        sqlcommand4 = 'delete from email where user_name = %s and passwrd = %s'
        user_name = input('Enter your user name to delete your account =')
        password = input('Enter your password =')
        values = (user_name,password)
        check = Check(user_name,password)
        if values == check:
            cursor.execute(sqlcommand4,values)
        print('Delete successfully')
    # exit
    elif choice == 6:
        break


connection.commit()