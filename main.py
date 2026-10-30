import sqlite3

try:
    connection = sqlite3.connect('./db/vocab.db')
    cursor = connection.cursor()  
    print('DB initialised')

    query = 'SELECT sqlite_version()'
    cursor.execute(query)

    result = cursor.fetchall()
    print("SQLite Version is {}".format(result[0][0]))

    cursor.close()
except sqlite3.Error as error:
    print("Error occurred - ", error)

finally:
    # Ensures the db connection is closed
    if connection:
        connection.close()
        print("SQLite Connection Closed")
