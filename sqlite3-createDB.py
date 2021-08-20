#import sqlite3 as db
import mysql.connector

# NOTES:
# Use python3 when calling this program


# Initialize a new DB to store expenditures
def init():
    # Create a new database called "tracker.db" and save it in the current directory. If db already exists it will connect to it.
    conn = db.connect("tracker.db")
    # Create a cursor to execute SQL queries on the database
    cur = conn.cursor()
    # The first query you need to execute is "create table". Table will have the following fields: name, type, amount, date
    sql = '''
    create table if not exists expenses (
        name string,
        type string,
        amount number,
        date string
        )
    '''
    # Use the db cursor to execute the above query
    cur.execute(sql)
    # In order to store any executed queries in the DB, use a commit
    conn.commit()

# This function takes in 3 parameters and stores that in the DB. It doesn't return anything
# Since message is an optional parameter it is set to an empty string (message="") - DEPRECATED
def log(name, type, amount):
    # Same as init function
    # Import datetime and then create variable "date" with current date time as a string
    from datetime import datetime
    date = str(datetime.now())
    conn = db.connect("tracker.db")
    cur = conn.cursor()
    # This SQL statement inserts a value into the DB. Each of the {} are placeholders, which are replaced with the variables in the 'format' function
    sql = '''
    insert into expenses values (
        '{}',
        '{}',
         {},
        '{}'
        )
    '''.format(name, type, amount, date)
    cur.execute(sql)
    conn.commit()

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

#connect to mysql db
mydb = mysql.connector.connect(
    host='capstone.cuzcfmfwvsp1.us-east-1.rds.amazonaws.com',
	user='admin',
	password='apprentice'
)

init()

print("\n Welcome to the Expense Tracker!")
print("\n Format for submitting an expense: [name] [type of expense] [amount]
print("Adding an expense (example): jeff food 30")
print("To view all expenses: view")
print("To view expenses by type: view by [type]")
print("\n To exit the program: exit")

exit = 0

while exit == 0: # while the user doesn't exit the program...
    input = input("\n Enter a command: ")
    split = input.split() # this splits up the input into a list of words
    if input == 'exit':
        exit = 1
    elif input == 'view':
        view()
    elif 'view by' in input: # if the string 'view by' can be found in the input...
        last_word = split[-1] # this means get the last element of this list
        view(last_word)
    elif len(split) == 3 and type(split[0]) == 'str' and type(split[1]) == 'str' and type(split[2]) == 'int': # if the input is formatted correctly...
        log(split[0],split[1],split[2])

print("\nYou've exited the program\n")
