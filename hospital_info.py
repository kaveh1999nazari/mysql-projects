#make connection:
import mysql.connector as mysql
def Connection_mysql():
    connection = mysql.connect(host = input('Enter your host =') , 
                         user = input('Enter your user =') , 
                         password = input('Enter password =') , 
                         database = input('Enter your database ='))
    return connection
def check_connection(connection):
    try:
        if connection:
            print('connection is ok and you can use very comfortable :)')
    except ValueError as e:
        print(e)
def save_connection():
    return connection.commit()

connection = Connection_mysql()
cursor = connection.cursor()

# check information by hospital_id and doctor_id :
def info_ID():
    try:
        print("""which one do you want to check information?
    0 - exit
    1 - hospital
    2 - doctor""")
        while True:
            choice = int(input('Enter your choice ='))
            if choice == 0: break
            elif choice == 1:
                sqlcommand = """select *
                                from hospital_table
                                where hospital_id = %s"""
                hospital_id = input('Enter your hospital Id =')
                cursor.execute(sqlcommand,(hospital_id ,))
                result = cursor.fetchall()
                for i in result:
                    hospital_id , hospital_name , bed_count = i
                    print(f"""hospital_id = {hospital_id}
hospital_name = {hospital_name}
bed_count = {bed_count}""")
            elif choice == 2:
                sqlcommand = """select *
from doctor_table
where doctor_id = %s"""
                doctor_id = input('Enter doctor_id =')
                cursor.execute(sqlcommand,(doctor_id ,))
                result = cursor.fetchall()
                for i in result:
                    doctor_id , doctor_name , hospital_id , joining_date , speciality , salary , experience = i
                    print(f"""doctor_id = {doctor_id}
doctor_name = {doctor_name}
joining_date = {joining_date}
speciality = {speciality}
salary = {salary}
experience = {experience}""")
                else:
                    pass
    except ValueError as e:
        print(e)
# check speciality and salary by user :
def Info_speciality_salary():
    try:
        print('input your speciality and salary to show')
        speciality = input('Enter speciality =')
        salary = input('Enter salary =')
        sqlcommand = """select *
from doctor_table
where speciality = %s and salary > %s"""
        values = (speciality,salary)
        cursor.execute(sqlcommand,values)
        result = cursor.fetchall()
        for i in result:
            doctor_id , doctor_name , hospital_id , joining_date , speciality , salary , experience = i
            print(f"""doctor_id = {doctor_id}
doctor_name = {doctor_name}
joining_date = {joining_date}
speciality = {speciality}
salary = {salary}
experience = {experience}
#########################""")
    except ValueError as e:
        print(e)
# get doctor names by user:
def get_doctors():
    try:
        print('Enter your hospital ID to show doctors')
        sqlcommand = """select doctor_id , doctor_name
from doctor_table
where hospital_id = %s"""
        hospital_id = input('Enter hospital_id =')
        cursor.execute(sqlcommand,(hospital_id ,))
        result = cursor.fetchall()
        for i in result:
            doctor_id , doctor_name = i
            print(f"""doctor_id = {doctor_id}
doctor_name = {doctor_name}""")
    except ValueError as e:
        print(e)

def update_doctor_experience():
    try:
        print('Enter your Doctor_id to update their experience')
        doctor_id = input('Enter Doctor ID =')
        experience = input("Enter doctor experience=")
        sqlcommand = """update doctor_table
set experience = %s
where doctor_id = %s"""
        values = (experience,doctor_id)
        cursor.execute(sqlcommand,values)
        print('successfully updated :)')
        sqlcommand1 = """select *
from doctor_table
where doctor_id = %s"""
        cursor.execute(sqlcommand1,(doctor_id ,))
        result = cursor.fetchall()
        for i in result:
            doctor_id , doctor_name , hospital_id , joining_date , speciality , salary , experience = i
            print(f"""doctor_id = {doctor_id}
doctor_name = {doctor_name}
joining_date = {joining_date}
speciality = {speciality}
salary = {salary}
experience = {experience}""")
    except ValueError as e:
        print(e)


save_connection()

############################################################################
###this is example from this site:
###https://pynative.com/python-database-programming-exercise-with-solution/
############################################################################