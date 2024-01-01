import os

index_file_name = ".advanced-listing"
advanced_listing_file_extension = "advanced-list"
version_number = 1.0

def select_option(option: int):
    if option == 1: # preview list
        with open(index_file_name, "r") as configuration:
            lists = configuration.readlines()
            print("You have %s lists, which one would you like to preview?" % len(lists))
            for index, list_ in enumerate(lists):
                print("#%s - %s" % (str(index + 1), list_.rstrip()))
            _list = lists[int(input("Selection: "))-1]
            print("") # new line
            try: # open list 
                with open(_list.rstrip() + ".%s" % advanced_listing_file_extension, "r") as items:
                    for index, item in enumerate(items.readlines()):
                        print("#%s - %s" % (str(index + 1), item.rstrip()))
            except: 
                print("This list either does not exist or is corrupted!")
    elif option == 2: # create a list
        list_name = input("Name your list: ")
        list_file = "%s.%s" % (list_name, advanced_listing_file_extension)
        print("Adding list to configuration..")
        with open(index_file_name, "a") as configuration:
            configuration.write(list_name + "\n")
        print("Creating list file..")
        with open(list_file, "w") as _list:
            _range = int(input("How many items should I add to the list? "))
            for _ in range(int(_range)):
                _list.write(input("#%s: " % str(_ + 1)) + "\n")
            print("List Created!")
            _list.close()
    elif option == 3: # add to a list
        with open(index_file_name, "r") as configuration:
            lists = configuration.readlines()
            print("You have %s lists, which one would you like to add to?" % len(lists))
            for index, list_ in enumerate(lists):
                print("#%s - %s" % (str(index + 1), list_.rstrip()))
            _list = lists[int(input("Selection: "))-1]
            print("") # new line
            try: # open list 
                with open(_list.rstrip() + ".%s" % advanced_listing_file_extension, "a") as _list:
                    _range = input("How many items should I add to the list? ")
                    for _ in range(int(_range)):
                        _list.write(input("#%s: " % str(_ + 1)) + "\n")
                _list.close()
                print("Finished adding to list!")
            except: 
                print("This list either does not exist or is corrupted!")
    elif option == 4:
        with open(index_file_name, "r") as configuration:
            lists = configuration.readlines()
            print("You have %s lists, which one would you like to get the item count of?" % len(lists))
            for index, list_ in enumerate(lists):
                print("#%s - %s" % (str(index + 1), list_.rstrip()))
            _list = lists[int(input("Selection: "))-1]
            try: # open list 
                with open(_list.rstrip() + ".%s" % advanced_listing_file_extension, "r") as items:
                    print("The Item Count of this List is: %s" % len(items.readlines()))
            except: 
                print("This list either does not exist or is corrupted!")
    elif option == 5:
        with open(index_file_name, "r") as configuration:
            lists = configuration.readlines()
            print("You have %s lists, which one would you like to delete?" % len(lists))
            for index, list_ in enumerate(lists):
                print("#%s - %s" % (str(index + 1), list_.rstrip()))
            _list = lists[int(input("Selection: "))-1]
            os.remove(_list.rstrip() + ".%s" % advanced_listing_file_extension)
            print("List (File) has been deleted..")
            with open(index_file_name, "r+") as configuration:
                data = configuration.readlines()
                if _list.rstrip() + "\n" in data:
                    data.remove(_list)
                configuration.seek(0)
                configuration.truncate(0)
                configuration.write("".join(data))
            print("List (Configuration Data) has been deleted..")

def advanced_listing():
    selection = input("Welcome to AdvancedListing %s! \n\n1: Preview List\n2: Create New List\n3: Add to List\n4: Get Item Count of List\n5: Delete a List\n\nSelect an Option: " %  version_number)
    select_option(int(selection))
# check if index_file_name exist
try: 
    open(index_file_name, "r").close()
    advanced_listing()
except: 
    print("Setting up AdvancedListing..")
    open(index_file_name, "w").close()
    print("Setup!")
    advanced_listing()
