#   Game collection list editor/random subset picker
#   v1.0 - begun 5:00pm on 29-March-2012
#        - picking, menu transversal functionality added
#        - templates for editing, addition semi-complete
#   v1.5 - begun 9:00am on 18-December-2012
#        - editing functionality added
#   Douglas Selby (selby.douglas@gmail.com)


from string import *
import random

options_text = 'Please input one of the following options:\n\
"edit" to insert/remove games from either list, or type "e",\n\
"pick" to have game choice(s) picked for you to play, or type "p",\n\
or "" (press Enter/Return) to exit.\n'
prompt_text = 'What do you want to do? '
caps_reminder_text = 'FYI: You left the CAPSLOCK on.'
nonsense_text = "I'm sorry, I didn't quite understand that last part."
full_gameList_filepath = 'gamesListFullLibrary.txt'
todo_gameList_filepath = 'gamesListToDo.txt'
exasperated_text = "Come back when you're ready to take this seriously."
edit_text = "Would you like to add (type 'add' or 'a'), or remove (type 'remove' or 'r') titles? "
remove_prompt = "Are you sure you would like to remove a title? y/n: "
remove_again_prompt = "Would you like to remove another title? y/n: "
systems_abbr_array = ['NES', 'SNES', 'SEGA', 'PSX', 'N64', 'PS2', 'GCN', 'XBOX', 'PS3', 'Wii', '360', 'PC', 'GBA', 'DS', '3DS', 'WiiU']
spacer_text = ""
newline_text = '\n'

def main():
    print("main() - Start")

    # Ask user for option, then execute
        # 'edit' for editing (adding/subtracting) from the master/todo list
        # 'pick' for picking a game to play (multiple options)
    getPurposeAndExecute()

    print("main() - Exit")

def getPurposeAndExecute():
    # prompt for user input, run program
    print(options_text)
    input_string = input(prompt_text)
    while(input_string != ''):
        if(input_string == 'e' or input_string == 'edit'):
            # run edit function
            editFile()
        elif(input_string == 'E' or input_string == 'EDIT'):
            print(caps_reminder_text)
            # run edit function
            editFile()
        elif(input_string == 'p' or input_string == 'pick'):
            # run edit function
            pickGames()
        elif(input_string == 'P' or input_string == 'PICK'):
            print(caps_reminder_text)
            # run edit function
            pickGames()
        else:
            print(nonsense_text)
        input_string = input(prompt_text)

def editFile():
    # figure out what list to operate on, then execute
    print("Editing - Begin")
    fileToHandle = fullOrTodo()
    if(fileToHandle == 'bad input'):
        print(exasperated_text)
    else:
        print("This program can allows you to add/remove titles from " + fileToHandle + ", the contents of which are displayed below:\n")
        f = open(fileToHandle, 'r')
        for line in f:
            print(line)
        f.close()
        
        input_string = input('\n' + edit_text)
        while(input_string != ''):
            if(input_string == 'a' or input_string == 'add'):
                full_title_text = getFullTitleInfo()
                addToFile(fileToHandle, full_title_text)
            elif(input_string == 'A' or input_string == 'ADD'):
                print(caps_reminder_text)
                full_title_text = getFullTitleInfo()
                addToFile(fileToHandle, full_title_text)
            elif(input_string == 'r' or input_string == 'remove'):
                removeTitles(fileToHandle)
            elif(input_string == 'R' or input_string == 'REMOVE'):
                print(caps_reminder_text)
                removeTitles(fileToHandle)
            else:
                print(nonsense_text)
            input_string = input(edit_text)
    print("Editing - Finished")

def getFullTitleInfo():
    print("Getting a full game title - Begin")
    system_valid = False
    tries = 0
    return_val = ''
    while(system_valid == False and tries < 3):
        print("The following are valid system name abbreviations:", systems_abbr_array)
        input_string = input("Please enter a system abbreviation: ")
        for system in systems_abbr_array:
            if(input_string == system):
                system_valid = True
        tries += 1
    if(tries < 3):
        print("Adding a game for the " + input_string + " console.")
        return_val += input_string
        input_string = input("Please enter the name of the game to be added: ")
        while(input_string == spacer_text):
            input_string = input("Please enter the name of the game to be added: ")
        return_val += '\t'
        return_val += input_string
    print("Getting a full game title - Finished")
    return return_val

def getNameTitleInfo():
    print("Getting a game title name - Begin")
    return_val = ''
    input_string = input("Please enter the name of the game to be removed: ")
    while(input_string == spacer_text):
        input_string = input("Please enter the name of the game to be removed: ")
    return_val += input_string
    print("Getting a game title name - Finished")
    return return_val

def addToFile(fileToHandle, full_title_text):
    print("Adding " + full_title_text + " to " + fileToHandle + " - Begin")
    # set default flags + vars
    game_exists_flag = False
    addition_success_flag = False
    temp_sys_name = ""
    # open file
    # iterate through file contents until one of the following happens:
        # system name matches the line system name, then...
            # set temp sys name var
            #  continue iterating through lines until one of the following happens:
                # line matches full_title_text, then...
                    # raise game exists_flag
                # line system name changes, then
                    # append full title text to temp contents
                    # raise addition success flag
                    # reset sys name check
                    temp_sys_name = ""
        # end of file is reached, then...
            # append full_title_text to temp file contents
    # close file
    if(game_exists_flag == True):
        print("Adding " + full_title_text + " to " + fileToHandle + " - Finished with no changes")
    else:
        # open file for writing
        # write temp contents to file
        # close file
        print("Adding " + full_title_text + " to " + fileToHandle + " - Finished Successfully")
        

def removeTitles(fileToHandle):
    print("Removing titles from " + fileToHandle + " - Begin")
    
    input_string = input(remove_prompt)
    if(input_string == 'y' or input_string == 'Y' or input_string == 'yes' or input_string == 'YES'):
        exit_bool = False
    else:
        exit_bool = True
    while(exit_bool == False):
        title_to_remove = getNameTitleInfo()
        print("Attempting to remove " + title_to_remove)
        title_to_remove += newline_text
        temp_file_contents = ''
        edited_success_flag = False
        # open file
        f = open(fileToHandle, 'r')
        # iterate through file contents
        for line in f:
            # if line.split(tab) == title_to_remove
            compare_title = line.split('\t')
            if(compare_title[0] != spacer_text and compare_title[0] != newline_text):
                if(compare_title[1] == title_to_remove):
                    # do not copy line to temp
                    #print(line + " -- Found game to remove!!!!")
                    # raise flag
                    edited_success_flag = True
                # if not
                else:
                    # copy line to temp
                    #print(line.split('\t'))
                    temp_file_contents += line
        # close file
        f.close()
        title_to_remove = title_to_remove.replace(newline_text, spacer_text)
        # if flag has not been raised
        if(edited_success_flag == False):
            # then removal was failure, as title was not found in lines in file
            print(title_to_remove + " was not found in " + fileToHandle + ".")
        # else
        else:
            # removal was completed, and file contents are different than before
            print(title_to_remove + " was successfully removed from " + fileToHandle + ".")
            # do something to save temp into old file name
            f = open(fileToHandle, 'w')
            f.write(temp_file_contents)
            f.close()
        input_string = input(remove_again_prompt)
        if(input_string == 'y' or input_string == 'Y' or input_string == 'yes' or input_string == 'YES'):
            exit_bool = False
        else:
            exit_bool = True
    
    print("Removing titles from " + fileToHandle + " - Finished")

def pickGames():
    # figure out what list to operate on, then execute
    print("Picking - Begin")
    fileToHandle = fullOrTodo()
    if(fileToHandle == 'bad input'):
        print(exasperated_text)
    else:
        print("This program can return up to three (3) titles from " + fileToHandle + ".\n")
        limit = getUserLimit()
        num_games_in_file = 0
        f = open(fileToHandle, 'r')
        for line in f:
            num_games_in_file += 1
        f.close()
        if(limit > num_games_in_file):
            print("Number of games in the file is smaller than the selected number of returned titles, will return contents of file")
            limit = num_games_in_file
        picked_titles = 0
        string1 = ''
        string2 = ''
        string3 = ''
        while(picked_titles < limit):
            rand_num = random.randint(0, num_games_in_file)
            #print("Current state = limit", limit, ", num_games_in_file", num_games_in_file, ", and rand_num", rand_num, ", and picked titles", picked_titles, "\n")
            i = 0
            f = open(fileToHandle, 'r')
            for line in f:
                if(i == rand_num and line != spacer_text):
                    if(picked_titles == 0):
                        string1 = line
                        picked_titles += 1
                    elif(picked_titles == 1):
                        if(string1 != line):
                            string2 = line
                            picked_titles += 1
                    elif(picked_titles == 2):
                        if(string1 != line and string2 != line):
                            string3 = line
                            picked_titles += 1
                i += 1
            f.close()
        print(string1 + '\n' + string2 + '\n' + string3)
        print("You have chosen...wisely.")
    print("Picking - Finished")

def fullOrTodo():
    print("Type 'full' to work with the full games library, \n\
            or type 'todo' to work with the smaller To-Do games list \n")
    input_string = input(prompt_text)
    if(input_string == 'full' or input_string == 'f'):
        return full_gameList_filepath
    elif(input_string == 'FULL' or input_string == 'F'):
        print(caps_reminder_text)
        return full_gameList_filepath
    elif(input_string == 'todo' or input_string == 'ToDo' or input_string == 'T'):
        return todo_gameList_filepath
    elif(input_string == 'TODO' or input_string == 'T'):
        print(caps_reminder_text)
        return todo_gameList_filepath
    else:
        return 'bad input'

def getUserLimit():
    #use crypto program to figure this out
    input_string = input("How many titles should be returned (Enter integer value, 1-3)? ")
    try:
        x = int(input_string)
    except:
        input_string = input("Error, How many titles should be returned (Enter integer value, 3 or less, in numerical form)? ")
    return x
        

main()
