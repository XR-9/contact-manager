contact = []
is_running = True

def info(name, mobile):
    return {"name": name, "mobile": mobile}

print("┌-----------------------------┐")
print("│WELCOME TO THE LIST GENERATOR│")
print("└-----------------------------┘")

while is_running:

    print("\n1. Add information")
    print("2. View information")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Please enter a valid choice")
        continue

    # ------------------- ADD INFO -------------------
    elif choice == "1":
        name = input("Enter name: ").lower()

        if not all(part.isalpha() for part in name.split()):
            print("Please enter a valid name")
            continue

        mobile = input("Enter mobile number: ")

        if not mobile.isdigit() or len(mobile) != 10:
            print("Please enter a valid mobile number")
            continue

        # Duplicate mobile check
        duplicate = False
        for item in contact:
            if item["mobile"] == mobile:
                print("Mobile number already exists")
                duplicate = True
                break

        if duplicate:
            continue

        contact.append(info(name, mobile))
        print("Contact added successfully!")

    # ------------------- VIEW / SEARCH / UPDATE -------------------
    elif choice == "2":
        while True:
            print("\n1. Search by name")
            print("2. Search by mobile")
            print("3. View all contacts")
            print("4. Update info")
            print("5. Quit")

            option = input("Enter your option: ")

            if not option.isdigit():
                print("Please enter a valid choice")
                continue

            # ------------------- SEARCH BY NAME -------------------
            elif option == "1":
                search_name = input("Enter name: ").lower()

                if not all(part.isalpha() for part in search_name.split()):
                    print("Please enter a valid name")
                    continue

                found = False
                for item in contact:
                    if item["name"] == search_name:
                        print(item)
                        found = True

                if not found:
                    print("Name does not exist")

            # ------------------- SEARCH BY MOBILE -------------------
            elif option == "2":
                search_mobile = input("Enter mobile number: ")

                if not search_mobile.isdigit() or len(search_mobile) != 10:
                    print("Please enter a valid mobile number")
                    continue

                found = False
                for item in contact:
                    if item["mobile"] == search_mobile:
                        print(item)
                        found = True

                if not found:
                    print("Mobile number does not exist")

            # ------------------- VIEW ALL CONTACTS -------------------
            elif option == "3":
                if len(contact) == 0:
                    print("EMPTY")
                else:
                    print("\n---- YOUR CONTACT LIST ----")
                    for item in contact:
                        print(f"Name   : {item['name']}")
                        print(f"Mobile : {item['mobile']}")
                        print("---------------------------")

            # ------------------- UPDATE INFO -------------------
            elif option == "4":
                print("\n1. Update name only")
                print("2. Update mobile only")
                print("3. Update both")
                print("4. Quit")

                choice_2 = input("Enter your choice: ")

                if not choice_2.isdigit():
                    print("Please enter a valid choice")
                    continue

                # -------- UPDATE NAME ONLY --------
                elif choice_2 == "1":
                    old_name = input("Enter old name: ").lower()

                    if not all(part.isalpha() for part in old_name.split()):
                        print("Invalid name")
                        continue

                    found = None
                    for item in contact:
                        if item["name"] == old_name:
                            found = item
                            break

                    if found is None:
                        print("Contact not found")
                        continue

                    new_name = input("Enter new name: ").lower()
                    if not all(part.isalpha() for part in new_name.split()):
                        print("Invalid name")
                        continue

                    found["name"] = new_name
                    print("Update successful:", found)

                # -------- UPDATE MOBILE ONLY --------
                elif choice_2 == "2":
                    old_mobile = input("Enter old mobile number: ")

                    if not old_mobile.isdigit() or len(old_mobile) != 10:
                        print("Invalid mobile number")
                        continue

                    found = None
                    for item in contact:
                        if item["mobile"] == old_mobile:
                            found = item
                            break

                    if found is None:
                        print("Mobile number not found")
                        continue

                    new_mobile = input("Enter new mobile number: ")
                    if not new_mobile.isdigit() or len(new_mobile) != 10:
                        print("Invalid mobile number")
                        continue

                    # Duplicate check
                    duplicate = False
                    for item in contact:
                        if item["mobile"] == new_mobile and item != found:
                            print("Mobile number already exists")
                            duplicate = True
                            break

                    if duplicate:
                        continue

                    found["mobile"] = new_mobile
                    print("Update successful:", found)

                # -------- UPDATE BOTH --------
                elif choice_2 == "3":
                    identify = input("Enter old name or old mobile: ").lower()

                    found = None
                    for item in contact:
                        if item["name"] == identify or item["mobile"] == identify:
                            found = item
                            break

                    if found is None:
                        print("Contact not found")
                        continue

                    new_name = input("Enter new name: ").lower()
                    if not all(part.isalpha() for part in new_name.split()):
                        print("Invalid name")
                        continue

                    new_mobile = input("Enter new mobile number: ")
                    if not new_mobile.isdigit() or len(new_mobile) != 10:
                        print("Invalid mobile number")
                        continue

                    # Duplicate check
                    duplicate = False
                    for item in contact:
                        if item["mobile"] == new_mobile and item != found:
                            print("Mobile number already exists")
                            duplicate = True
                            break

                    if duplicate:
                        continue

                    found["name"] = new_name
                    found["mobile"] = new_mobile
                    print("Update successful:", found)

                elif choice_2 == "4":
                    continue

            # ------------------- EXIT UPDATE MENU -------------------
            elif option == "5":
                break

    # ------------------- EXIT PROGRAM -------------------
    elif choice == "3":
        is_running = False
