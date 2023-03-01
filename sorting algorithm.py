def main():
    print("\n\nSORTING ALGORITHM APPLICATION")
    print("Programmed by: Shin I. Lim")
    print("BSCOE 2-1")
    # Display the options for the user
    while True:
        print("\n< < < M A I N   M E N U > > >\n")
        print("(1) SELECTION SORTING")
        print("(2) BUBBLE SORTING")
        print("(3) INSERTION SORTING")
        print("(4) MERGE SORTING")
        print("(5) EXIT")

        choice = int(input("\nSelect an option: "))

        if choice == 1:
            user_list = []
            # Get the elements from the user after they choose a sorting type
            number_values = int(input(f"How many elements are there on your list? "))
            # Ask the user to put an integer or letter to sort
            print(f"Enter your {number_values} elements now using ENTER key.")
            for i in range(number_values):
                user_input = input()
                user_list.append(user_input)
            selection_sort(user_list)

            # Ask the user to try the program again, if yes it will redisplay the main menu
            try_again = input("\nDo you want to try again? [y/n] ")
            if try_again == "y":
                main()
            else:
                break

        elif choice == 2:
            user_list = []
            # Get the elements from the user after they choose a sorting type
            number_values = int(input(f"How many elements are there on your list? "))
            # Ask the user to put an integer or letter to sort
            print(f"Enter your {number_values} elements now using ENTER key.")
            for i in range(number_values):
                user_input = input()
                user_list.append(user_input)
            bubble_sort(user_list)

            # Ask the user to try the program again, if yes it will redisplay the main menu
            try_again = input("\nDo you want to try again? [y/n] ")
            if try_again == "y":
                main()
            else:
                break

        elif choice == 3:
            user_list = []
            # Get the elements from the user after they choose a sorting type
            number_values = int(input(f"How many elements are there on your list? "))
            # Ask the user to put an integer or letter to sort
            print(f"Enter your {number_values} elements now using ENTER key.")
            for i in range(number_values):
                user_input = input()
                user_list.append(user_input)
            insertion_sort(user_list)

            # Ask the user to try the program again, if yes it will redisplay the main menu
            try_again = input("\nDo you want to try again? [y/n] ")
            if try_again == "y":
                main()
            else:
                break

        elif choice == 4:
            user_list = []
            # Get the elements from the user after they choose a sorting type
            number_values = int(input(f"How many elements are there on your list? "))
            # Ask the user to put an integer or letter to sort
            print(f"Enter your {number_values} elements now using ENTER key.")
            for i in range(number_values):
                user_input = input()
                user_list.append(user_input)
            for_merge_sort(user_list)

            # Ask the user to try the program again, if yes it will redisplay the main menu
            try_again = input("\nDo you want to try again? [y/n] ")
            if try_again == "y":
                main()
            else:
                break

        elif choice == 5:
            exit()
        else:
            print("\nInvalid selection. Please try again.")


# Function that performs selection sorting
def selection_sort(user_list):
    try:
        element_type = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        if element_type == 1:
            print(f"You selected INTEGER.")
        elif element_type == 2:
            print(f"You selected LETTER.")
        else:
            print("\nInvalid selection. Please choose between INTEGER and LETTER.")

        sorting_type = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPHABETICALLY\nEnter sorting type: ")))
        print("\nUNSORTED LIST OF THE ELEMENTS:", "\n", user_list)
        if sorting_type == 1 or sorting_type == 3:
            for i in range(len(user_list)):
                min_idx = i
                for j in range(i + 1, len(user_list)):
                    if user_list[min_idx] > user_list[j]:
                        min_idx = j
                user_list[i], user_list[min_idx] = user_list[min_idx], user_list[i]
                print("\nPass", i + 1, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
        elif sorting_type == 2:
            for i in range(len(user_list)):
                min_idx = i
                for j in range(i + 1, len(user_list)):
                    if user_list[min_idx] < user_list[j]:
                        min_idx = j
                user_list[i], user_list[min_idx] = user_list[min_idx], user_list[i]
                print("\nPass", i + 1, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
    except ValueError:
        print("\nInvalid input. Please enter only integers.")
        selection_sort(user_list)


# Function that performs bubble sorting
def bubble_sort(user_list):
    try:
        element_type = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        if element_type == 1:
            print(f"You selected INTEGER.")
        elif element_type == 2:
            print(f"You selected LETTER.")
        else:
            print("\nInvalid selection. Please choose between INTEGER and LETTER.")

        sorting_type = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPHABETICALLY\nEnter sorting type: ")))
        print("\nUNSORTED LIST OF THE ELEMENTS:", "\n", user_list)
        if sorting_type == 1 or sorting_type == 3:
            for i in range(len(user_list)):
                for j in range(0, len(user_list) - i - 1):
                    if user_list[j] > user_list[j + 1]:
                        user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
                        print("\nPass", i + 1, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
        elif sorting_type == 2:
            for i in range(len(user_list)):
                for j in range(0, len(user_list) - i - 1):
                    if user_list[j] < user_list[j + 1]:
                        user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
                        print("\nPass", i + 1, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
    except ValueError:
        print("\nInvalid input. Please enter only integers.")
        bubble_sort(user_list)


# Function that performs insertion sorting
def insertion_sort(user_list):
    try:
        element_type = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        if element_type == 1:
            print(f"You selected INTEGER.")
        elif element_type == 2:
            print(f"You selected LETTER.")
        else:
            print("\nInvalid selection. Please choose between INTEGER and LETTER.")

        sorting_type = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPHABETICALLY\nEnter sorting mode: ")))
        print("\nUNSORTED LIST OF THE ELEMENTS:", "\n", user_list)
        if sorting_type == 1 or sorting_type == 3:
            for i in range(1, len(user_list)):
                key = user_list[i]
                j = i - 1
                while j >= 0 and key < user_list[j]:
                    user_list[j + 1] = user_list[j]
                    j -= 1
                user_list[j + 1] = key
                print("\nPass", i, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
        elif sorting_type == 2:
            for i in range(1, len(user_list)):
                key = user_list[i]
                j = i - 1
                while j >= 0 and key > user_list[j]:
                    user_list[j + 1] = user_list[j]
                    j -= 1
                user_list[j + 1] = key
                print("\nPass", i, ":", user_list)
            print("\nFINAL SORTED LIST:", user_list)
    except ValueError:
        print("\nInvalid input. Please enter only integers.")
        insertion_sort(user_list)


def for_merge_sort(user_list):
    element_type = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
    if element_type == 1:
        print(f"You selected INTEGER.")
    elif element_type == 2:
        print(f"You selected LETTER.")
    else:
        print("\nInvalid selection. Please choose between INTEGER and LETTER.")

    sorting_type = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPHABETICALLY\nEnter sorting mode: ")))
    if sorting_type == 1 or sorting_type == 3:
        merge_sort_ascending(user_list)
    elif sorting_type == 2:
        merge_sort_descending(user_list)


# Function that performs merge sorting
def merge_sort_ascending(user_list):
    try:
        print("\nUNSORTED LIST OF THE ELEMENTS:", user_list)
        if len(user_list) > 1:
            mid = len(user_list) // 2
            left = user_list[:mid]
            right = user_list[mid:]

            merge_sort_ascending(left)
            merge_sort_ascending(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    user_list[k] = left[i]
                    i += 1
                else:
                    user_list[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                user_list[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                user_list[k] = right[j]
                j += 1
                k += 1
            print("\nPass", k, ":", user_list)
        print("\nSORTED LIST:", user_list)

    except ValueError:
        print("\nInvalid input. Please enter only integers.")
        merge_sort_ascending(user_list)


# Function that performs merge sorting
def merge_sort_descending(user_list):
    try:
        print("\nUNSORTED LIST OF THE ELEMENTS:", user_list)
        if len(user_list) > 1:
            mid = len(user_list) // 2
            left = user_list[:mid]
            right = user_list[mid:]

            merge_sort_descending(left)
            merge_sort_descending(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    user_list[k] = left[i]
                    i += 1
                else:
                    user_list[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                user_list[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                user_list[k] = right[j]
                j += 1
                k += 1
            print("\nPass", k, ":", user_list)
        print("\nSORTED LIST:", user_list)
    except ValueError:
        print("\nInvalid input. Please enter only integers.")
        merge_sort_descending(user_list)


main()


