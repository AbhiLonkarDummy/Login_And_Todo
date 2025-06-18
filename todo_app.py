# TODO Create a todo app to add and remove items from a list

# list to store the data, as its mutable and supports variety of operations that could be used to build a todo app
todo_list = ["Make coffee", "Drink coffee", "Complete course", "Play cricket"]
while True:

    # * Letting the user choose what operation they want to perform
    # * stripping removes both trailing and leading whitespaces
    operation = input(
        "Enter a to add, d to delete, v to view and c to clear list: "
    ).strip()

    if operation.lower() == "a":
        # * user chooses add operation
        # * taking the item the user wants to enter
        item = input("Enter the item: ")
        # * Adding it to the list
        todo_list.append(item)
        # * Printing success message
        print(f"{item} added successfully")

    elif operation.lower() == "d":
        # * user chooses delete operation
        # * printing the list so the user can confirm the index of the item
        print(todo_list)
        itemIdx = int(input("Enter item's index you want to delete: "))
        # * Check if the index lies in the todo_list first
        if itemIdx >= len(todo_list):
            print("Enter correct itemIdx: ")
        # * If deletion possible go ahead and delete the item and give a success message
        else:
            item = todo_list[itemIdx]
            todo_list.pop(int(itemIdx))
            print(f"{item} deleted successfully")
    elif operation.lower() == "v":
        # * User chooses view list
        if len(todo_list) == 0:
            # * Empty list case
            print("List is empty")
        else:
            # * Showing complete list
            print(todo_list)
    elif operation.lower() == "c":
        # * User chooses to empty the list
        # * confirmation input to go ahead and empty the list
        shouldClear = input("Are you sure you want to clear the list (y/n): ")
        if shouldClear.lower() == "y":
            todo_list.clear()
        else:
            continue
    else:
        # * Notifies user if any invalid operation was chooses
        print("Enter valid operation")
