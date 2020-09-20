# This program will calssify your life stage based on your age. 
while True:
    try:
        age = int(input("How old are you? "))
    except NameError:
        print("Please enter a number greater than 0.")
        continue
    
    if age < 2:
        print("You are a baby.")
        break
    elif age >=2 and age < 4:
        print("You are a toddler.")
        break
    elif age >= 4 and age < 13:
        print("You are a kid.")
        break
    elif age >= 13 and age < 20:
        print("You are a teenager.")
        break
    elif age >= 20 and age < 65:
        print("You are an adult.")
        break
    else:
        print("You are an older adult.")
        break
