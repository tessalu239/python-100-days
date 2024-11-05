while True:
    try:
        word_per_page = int(input("Number of words per page: "))
        pages = int(input("Number of pages: "))
        total_words = pages * word_per_page
        print(total_words)
        break
    except ValueError:
        print('You typed in not a NUMBER, using something like 1, 10 so on')
