import pymysql

# NOTES:
# Use python3 when calling this program

# Initialize a new DB to store expenditures
def init():
    mydb = pymysql.connect(
        host='localhost',
	    user='root',
	    password='apprentice',
    )

    # Create your - drop db if already exist
    mycursor = mydb.cursor()
    mycursor.execute('DROP database IF EXISTS expensetracker')

    # Query to create a db
    mycursor.execute('CREATE database EXPENSETRACKER')

    #Dropping TRACKER table if already exists
    mycursor.execute('DROP TABLE IF EXISTS TRACKER')

    #Closing the connection
    mydb.close()

    # Connect to newly created DB
    mydb = pymysql.connect(
        host='localhost',
	    user='root',
	    password='apprentice',
	    database='EXPENSETRACKER'
    )

    #Creating table
    sql = '''CREATE TABLE TRACKER(
        NAME CHAR(50),
        TYPE CHAR (20),
        AMOUNT FLOAT
    )'''
    mycursor.execute(sql)

# This function takes in 3 parameters and stores that in the DB. It doesn't return anything
def log(name, type, amount):
    # Same as init function
    # Import datetime and then create variable "date" with current date time as a string
    from datetime import datetime
    date = str(datetime.now())
    mycursor = mydb.cursor()
    # This SQL statement inserts a value into the DB. Each of the {} are placeholders, which are replaced with the variables in the 'format' function
    sql = '''
    insert into expenses values (
        '{}',
        '{}',
         {},
        '{}'
        )
    '''.format(name, type, amount, date)
    mycursor.execute(sql)

# This function returns a list of all logged expenses and the total expense. Results can be filtered by type
def view(type=None):
    conn = db.connect("tracker.db")
    cur = conn.cursor()
    # if statement to decide whether or not to execute a SQL query with the type parameter
    if type:
        sql = '''
        select * from expenses where type = '{}'
        '''.format(type)
        # The below SQL query adds together all the expense amounts
        sql2 = '''
        select sum(amount) from expenses where type = '{}'
        '''.format(type)
    else:
        sql = '''
        select * from expenses
        '''
        sql2 = '''
        select sum(amount) from expenses where type = '{}'
        '''.format(type)
    cur.execute(sql)
    cur.execute(sql2)

    # store the result of the executed queries
    results = cur.fetchall()
    total_amount = cur.fetchone()[0]

    return total_amount, results

def main():

    init()

    print("\n Welcome to the Expense Tracker!")
    print("\n Format for submitting an expense: [name] [type of expense] [amount]")
    print("Adding an expense (example): jeff food 30")
    print("To view all expenses: view")
    print("To view expenses by type: view by [type]")
    print("\n To exit the program: exit")

    exit = 0

    while exit == 0: # while the user doesn't exit the program...
        input = input("\n Enter a command: ")
        user_input = input()
        split = user_input.split() # this splits up the input into a list of words
        if user_input == 'exit':
            exit = 1
        elif user_input == 'view':
            view()
        elif 'view by' in user_input.lower() and len(split) == 3: # if the string 'view by' can be found in the input...
            last_word = split[-1] # this means get the last element of this list
            view(last_word.lower())
        elif len(split) == 3 and split[0].isdigit() == False and split[1].isdigit() == False and split[2].isdigit() == True: # if the input is formatted correctly...
            log(split[0].lower(),split[1].lower(),split[2].lower())

    print("\nYou've exited the program\n")

main()
