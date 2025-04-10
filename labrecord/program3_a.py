def list_operations():
    my_list = []
    while True:
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Display List")
        print("5. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            element = input("Enter element to insert:")
            my_list.append(element)
            print(f"Element {element} inserted.")
        elif choice == 2:
            element = input("Enter element to delete:")
            if element in my_list:
                my_list.remove(element)
                print(f"Element '{element}' deleted.")
            else:
                print(f"Element '{element}' not found.")
        elif choice == 3:
            element = input("Enter element to find:")
            if element in my_list:
                print(f"Element'{element}' found.")
            else:
                print(f"Element '{element}' not found.")
        elif choice == 4:
            print(f"Current list: {my_list}")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

list_operations()