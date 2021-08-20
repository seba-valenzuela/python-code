import sqlite3

db_name = 'music.db'

def connect_to_db():
    # connect to the database
    # this will create it new if it doesn't already exist
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("Connected to DB.")
    # This will return multiple variables IN ORDER
    return db_conn, db_cursor;

def display_menu(db_conn, db_cursor):
    print("\nMain Menu:\n")
    print("Enter S to get started & create/refresh the table")
    print("Enter C to create a new row")
    print("Enter R to retrieve data")
    print("Enter U to update a row")
    print("Enter D to delete a row")
    print("Enter Q to quit the program")

    repeat = 0

    while repeat == 0:
        menu_input = input("\nEnter choice: ")
        if (menu_input.lower() == 's'):
            drop_table(db_cursor)
            create_table(db_cursor)
            db_conn.commit()
            select_all(db_cursor)
        elif (menu_input.lower() == 'c'):
            insert_row(db_cursor)
            db_conn.commit()
            select_all(db_cursor)
        elif (menu_input.lower() == 'r'):
            select_row(db_conn, db_cursor)
            db_conn.commit()
            select_all(db_cursor)
        elif (menu_input.lower() == 'u'):
            update_row(db_conn, db_cursor)
            db_conn.commit()
            select_all(db_cursor)
        elif (menu_input.lower() == 'd'):
            delete_row(db_cursor)
            db_conn.commit()
            select_all(db_cursor)
        elif (menu_input.lower() == 'q'):
            print("Goodbye.")
            db_conn.commit()
            repeat = 1
        else:
            print("\nInvalid choice. Try again: ")

def drop_table(db_cursor):
    # first drop the table just in case it already exists
    sql_statement = 'DROP TABLE IF EXISTS music'
    db_cursor.execute(sql_statement)
    print("Dropped Table.")

def create_table(db_cursor):
    # create the table
    sql_statement = 'CREATE TABLE music (artist TEXT, track TEXT, album TEXT, year INTEGER, price REAL, genre TEXT)'
    db_cursor.execute(sql_statement)
    print("Created Table.")

def insert_row(db_cursor):
    print("Row Values must be entered in the following order:")
    print("Artist, Track, Album, Year, Price (as floating point number), Genre\n")
    # ask the user for input, store in variables
    a, b, c, d, e, f = input("Enter values for your row: ").split(", ")
    sql_statement = 'INSERT INTO music VALUES (?, ?, ?, ?, ?, ?)'
    # create tuple with values appropriately formatted
    tuple_of_field_values = (a, b, c, int(d), float(e), f)
    db_cursor.execute(sql_statement, tuple_of_field_values)
    print("Inserted row into table.")

def select_row(db_conn, db_cursor):
    # Ask user for artist, search for music by artist name
    value_input = input("Search music by Artist: ")
    sql_statement = 'SELECT * from music WHERE artist = ?'
    tuple_of_key_value = (value_input, )
    result_set = db_conn.execute(sql_statement, tuple_of_key_value)
    for row in result_set:
        print(row)

def update_row(db_conn, db_cursor):

    # Ask user for artist, search for music by artist name
    value_input = input("Lets update a row! First search for it by track name: ")
    sql_statement = 'SELECT * from music WHERE track = ?'
    tuple_of_key_value = (value_input, )
    result_set = db_conn.execute(sql_statement, tuple_of_key_value)
    print("Here are all your current fields: ")
    for row in result_set:
        print(row)

    sql_statement = 'UPDATE music SET artist=?, album=?, year=?, price=?, genre=? WHERE track = ?'
    a, b, c, d, e = input("Update info for Artist, Album, Year, Price (as floating point number), and Genre: ").split(", ")
    tuple_of_key_value = (a, b, int(c), float(d), e, value_input)
    db_cursor.execute(sql_statement, tuple_of_key_value)

def delete_row(db_cursor):
    # delete one row based on key
    value_input = input("Indicate the Track of the row you would like to delete: ")
    sql_statement = 'DELETE FROM music WHERE track = ?'
    tuple_of_key_value = (value_input, )
    db_cursor.execute(sql_statement, tuple_of_key_value)
    print("Deleted row of track ", value_input)

def select_all(db_cursor):
# select all rows and print them
    sql_statement = 'SELECT * from music'
    result_set = db_cursor.execute(sql_statement)
    print("\nTable currently has the following rows:")
    for row in result_set:
        print(row)

def main():
    # connect_to_db()
    # assigned the 2 variables returned from this function
    # pass these variables as parameters into "display_menu" function
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)
main()
