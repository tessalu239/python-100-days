while True:
    try:
        age=int(input('How old are you?'))
        if age >=18:
            print(f"You are {age}, you can drive")
        else:
            print(f"You are {age}, you cannot drive")
        break
    except ValueError:
        print("You typed not a actual number")