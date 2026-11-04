import sqlite3
import re

try:
    connection_vocab = sqlite3.connect('./db/vocab.db')
    cursor_vocab = connection_vocab.cursor()  
    print('Connected to kindle vocab DB')

    connection_existing = sqlite3.connect("./db/existing_vocab.db")
    cursor_existing = connection_existing.cursor()
    print('Connected to existing vocab DB')

    query = 'SELECT word, lang FROM WORDS;'
    cursor_vocab.execute(query)

    words = cursor_vocab.fetchall()

    for word in words:
        # Check if the word exists in the existing_words db
        query = f"SELECT * FROM WORDS WHERE word={word[0]} AND lang={word[1]};"
        insert = False
        try:
            cursor_existing.execute(query)
        except sqlite3.Error as error:
            match = re.match("no such column: ", str(error))
            if match:
                insert = True
            else:
                continue
        # Insert the word into the existing_words db
        if not insert:
            continue


        query = f"INSERT INTO WORDS (word, lang) VALUES({word[0]}, {word[1]});"
        cursor_existing.execute(query)

        
    cursor_vocab.close()
    cursor_existing.close()

except sqlite3.Error as error:
    print("Error occurred - ", error)

finally:
    # Ensures the db connection_databse is closed
    if connection_vocab:
        connection_vocab.close()
        print("SQLite Connection to kindle vocab db is closed")

    if connection_existing:
        connection_existing.close()
        print("SQLite Connecction to existing vocab db is closed")
