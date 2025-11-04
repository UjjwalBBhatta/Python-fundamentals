#JSON based expense tracking CLI app
"""ädd, list, summary, delete, exit, these are the minimum things the app needs to do"""


import json
from datetime import datetime



def add_expense():
    """"This function lets the user add expenses to the tracker, the tracker stores data in [date]: [expense]"""
    try:
        expense = float(input("Enter the amount that you have spent: "))
        date = datetime.strptime(input("Enter the date in YYYY-MM-DD format: "), "%Y-%m-%d").date()
        new_expense = {"date": str(date), "expense": expense}
        
        try:
            with open("expenses.json", "r") as f:
                tracker = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tracker = []
        tracker.append(new_expense)
        
        with open("expenses.json", "w") as f:
            json.dump(tracker, f, indent = 4)
    except Exception as e:
        print(f"Something went wrong: {e}")

        
def list_expense():
    """A function used to showcase the expenses(mayb later on we can even add some graphs)"""
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            print(data)
    except FileNotFoundError:
        print("The json file was not found")
    except json.JSONDecodeError:
        print("The notes file is either empty or corrupted")

def delete_expense():
    """A function to delete infomation from the file, so we will let it delete either by the 
    index or from the date of the expense(an issue here would be if someone has multiple expenses in
    a singular day"""
    try:
        with open("expenses.json", "r") as f:
            tracker = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No notes found or file corrupted.")
        return

    choice = input("Do you want to delete by 'time' or 'index'?").strip().lower()

    if choice == "time":
        time = datetime.strptime(input("Enter the date that you want to delete in YYYY-MM-DD format: "), "%Y-%m-%d").date()
        for check in tracker:     #searching for the inputed date
            if check["date"] == str(time):
                tracker.remove(check)
                print(f"Deleted the expense on the date: {check['date']}")
                break
        else:
            print("No expense here")
            return
    elif choice == "index":
        index = int(input("Enter the index of the expense: "))-1
        if 0<= index < len(tracker):    # we are checking if the index is in bounds
            removed_expense = tracker.pop(index)
            print(f"Deleted the expense on the date: {removed_expense['date']}")
        else:
            print("Invalid index")
            return
    else:
        print("Invalid option")
        return

    with open("expenses.json","w") as f:
        json.dump(tracker, f, indent=4)


def show_summary():
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            total = sum(item["expense"] for item in data)
            print(f"\nTotal expenses recorded: ${total:.2f}")
            print(f"Total transactions: {len(data)}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No data available to summarize.")

def main():
    print("=== Expense Tracker CLI ===")
    print("Commands: add | list | delete | summary | exit")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "add":
            add_expense()
        elif command == "list":
            list_expense()
        elif command == "delete":
            delete_expense()
        elif command == "summary":
            show_summary()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command, try again.")
            
if __name__ == "__main__":
    main()


        
            
            
                      


                        