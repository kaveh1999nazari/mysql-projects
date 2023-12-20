# ask information of customer then order their food
import mysql.connector
# make connection :
connection = mysql.connector.connect (host = input('Enter your host =') , 
                                      user = input('Enter your user =') , 
                                      password = input('Enter password =') , 
                                      database = input('Enter your database ='))
cursor = connection.cursor()
# Enter information customer and order food :
class Customer :
    def __init__(self , first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
    def GetInfo(self):
        return(self.first_name,self.last_name)
first_name = input('Enter your name =')
last_name = input('Enter your family =')
customer = Customer(first_name , last_name)

print('Do you want to order? yes/no')
answer = input('Answer =')
choice_food = []
while answer.lower() == 'yes':
    print('choice your food :')
    cursor.execute('select * from food_list')
    result = cursor.fetchall()
    for i in result:
        food_id , food_name , price = i
        print(f'{food_id} : {food_name} , {price} $')
    choice = input('choice your food =')
    choice_food.append(choice)
    print('do you want still order?')
    answer = input('Answer =')

# add to database :
try:
    sqlcommand = 'insert into customer (first_name , last_name) values (%s , %s)'
    values = customer.GetInfo()
    cursor.execute(sqlcommand,values)
    id = cursor.lastrowid

    for choice in choice_food:
        sqlcommand = 'insert into order_list(food_id , customer_id) values(%s , %s)'
        values = (choice , id)
        cursor.execute(sqlcommand,values)


    print('your order is :')
    cursor.execute(f'''select f.food_name , f.price
    from order_list o
    join food_list f
    using(food_id)
    where customer_id = {id}''')
    shows = cursor.fetchall()
    for show in shows:
        food_name , price = show
        print(f'food order = {food_name} , price ={price} $')


    print('your cost order is :')
    sqlcommand = f"""select o.customer_id , c.first_name, c.last_name , sum(f.price) as total
    from order_list o
    join food_list f
    using(food_id)
    join customer c
    using (customer_id)
    where customer_id = {id}"""
    cursor.execute(sqlcommand)
    order_cost = cursor.fetchall()
    for order in order_cost:
        customer_id ,first_name , last_name ,total_cost = order
        print(f"customer id = {customer_id} , full name {first_name + ' ' + last_name}, total cost = {total_cost} $")

    connection.commit()


except mysql.connector.Error as e:
    print(e)
    connection.rollback()