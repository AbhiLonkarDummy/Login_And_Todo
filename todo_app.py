# TODO Create a todo app to add and remove items from a list

todo_list = ["Make coffee", "Drink coffee", "Complete course", "Play cricket"]
while True:
    operation = input(
        "Enter a to add, d to delete, v to view and c to clear list: "
    ).strip()
    if operation.lower() == "a":
        item = input("Enter the item: ")
        todo_list.append(item)
        print(f"{item} added successfully")
    elif operation.lower() == "d":
        print(todo_list)
        itemIdx = int(input("Enter item's index you want to delete: "))
        if itemIdx >= len(todo_list):
            print("Enter correct itemIdx: ")
        else:
            item = todo_list[itemIdx]
            todo_list.pop(int(itemIdx))
            print(f"{item} deleted successfully")
    elif operation.lower() == "v":
        if len(todo_list) == 0:
            print("List is empty")
        else:
            print(todo_list)
    elif operation.lower() == "c":
        shouldClear = input("Are you sure you want to clear the list (y/n): ")
        if shouldClear.lower() == "y":
            todo_list.clear()
        else:
            continue
    else:
        print("Enter valid operation")
