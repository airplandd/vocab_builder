1. Open the database
2. Read a row
3. Get the [word, language]
4. If word is not in existing_words database, in the corresponding language table:
    fetch the word from dictionary api
    create a flashcard for each part of speech
    write it in a txt file, corresponding to the language
    add the word in existing_words database
5. else:
    return to step 2