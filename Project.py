while True:
    name = input("Enter Customer's Name: ")
    total = 0

    while True:
        print("Enter The Amount and Quantity")
        amount = float(input("Enter Amount: "))
        quantity = float(input("Enter Quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name: ",name)
    print("Amount to be paid: ",total)
    print("-"*40)
    print("*************Happy Shopping*************")

    repeat1 = input("Do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break