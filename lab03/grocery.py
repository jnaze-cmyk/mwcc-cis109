grocery_list = []

while(True):
    print(f"""
    Welcome to Your Shopping List!
    
    Please make a selection from one of the following options:
    
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list. 
    7. Exit the program.
    """)

    selection = input("Selection: ")


    
    if(selection == "1"):
        item = input("Item to add: ")
        grocery_list.append(item)

    elif(selection == "2"):
        print(f"Grocery List: {grocery_list}")
        input("Hit [enter] to continue...")
        

    elif(selection == "3"):
        print(f"Item Count: {len(grocery_list)}")

    elif(selection == "4"):
        print(f"FIRST ITEM: {grocery_list[0]}")

    elif(selection == "5"):
        print(f"LAST ITEM: {grocery_list[-1]}")

    elif(selection == "6"):
        grocery_list = []
        print(f"The shopping list is now empty!")
        

    elif(selection == "7"):
        print("Goodbye!")
        exit()
        

    else:
        print(f"You entered an invalid option. \nPlease try again!")