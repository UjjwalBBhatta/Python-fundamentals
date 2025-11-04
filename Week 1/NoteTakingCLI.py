#JSON based note taking CLI app
"""Ok now we start the hard stuff, like idk what it all is but we will make itttt
You’ll make a JSON-based note-taking CLI app that supports:
add → add a new note
list → show all notes
delete → remove a note by index or title
save → automatically save updates to JSON
We’ll also handle:
FileNotFoundError (when file doesn’t exist yet)
JSONDecodeError (when the JSON file is empty or broken), So thats what our friend ChatGPT wants us to do"""
#thinking of making all into small functions, then creating a function to do all these tasks
# They can also create json files with the names and all which will automatically go to a dictonary to be saved
#Then when the add or delete function is called we can know which json file we are operating in
#We also need to make a simple CLI so first to ask for them to input the text, then to ask them the operation

#First lets import the json extension
import json

def Add_note():
    """"So this is a function to append stuff written to the json noes file"""
    try:
        title = input("Enter the title for this note: ")
        content = input("Enter the content to be inputed: ")
        new_note = {"title": title, "content": content}
        try: 
            with open("Notes.json", "r") as f:
                notes = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            notes = []    #So that file is always a list
        #Now we append the note    
        notes.append(new_note)
        
        with open("Notes.json", "w") as f:
            json.dump(notes, f, indent=4)
    except Exception as e:
        print(f"Something went wrong: {e}")

def Show_note():
    """It will show their notes, which they have taken"""
    try:
        with open("Notes.json", "r") as f:
            content = json.load(f)
            print(content)
    except FileNotFoundError:
        print("No notes file was found")
    except json.JSONDecodeError:
        print("The notes file is either empty or corrupted")

def Delete_index():
    try:
        with open("Notes.json", "r") as f:
            notes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No notes found or file corrupted.")
        return

    choice = input("Do u want to delete by 'number' or 'title'?").strip().lower()

    if choice == "number":
        # get note number from the user
        number = int(input("Enter the note number to delete: ")) - 1
        if 0 <= number < len(notes):
            removed_note = notes.pop(number)
            print(f"Deleted note titled '{removed_note['title']}'")
        else:
            print("Invalid number.")
            return

    elif choice == "title":
        # get title from user
        title_to_delete = input("Enter the title of the note to delete: ").strip()
        for note in notes:
            if note["title"].lower() == title_to_delete.lower():
                notes.remove(note)
                print(f"Deleted note titled '{note['title']}'")
                break
        else:
            print("Note not found.")
            return
    else:
        print("Invalid option.")
        return

    with open("Notes.json", "w") as f:
        json.dump(notes, f, indent=4)

#Now lets make a dictonary of possible user inputs, they will call their respective functions
user_input = {"add": Add_note,
              "save": Add_note,
              "listout": Show_note,
              "view": Show_note,
              "delete": Delete_index,
              "remove": Delete_index}

def main():
    print("Sup man, this is your note taking app")
    print("Type 'add', 'view', 'delete', or 'exit' to quit.")

    while True:
        command = input("\n> ").strip().lower()

        if command in ("exit", "quit"):
            print("Goodbye!")
            break
        elif command in user_input:
            user_input[command]()   # Calls the function
        else:
            print("Unknown command. Try again.")
if __name__ == "__main__":
    main()

