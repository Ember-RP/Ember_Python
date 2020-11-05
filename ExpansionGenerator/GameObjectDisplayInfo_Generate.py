#imported_file = open("GameObjectDisplayInfo.dbc.csv")
#imported_write = open("NewObjects.csv", "w+")
#imported_sql = open("NewObjects.sql", "w+")

#print(imported_lines[-2])

# new_entry = imported_lines[-1]
# new_entry = new_entry.split(",")
# 
# # defines displayid entry
# new_entry = int(new_entry[0]) + 1

# DB ENTRY TO START WITH
DB_ENTRY = 5000000

# POSTFIX TO END WITH
DB_POSTFIX = " [BFA]"

#print(new_entry)

options = [
    "1. Create new GameObjectDisplayInfo.dbc.csv. This will create \"NewObjects.csv\" with the last displayid+1 to be manually added at the end of your existing GameObjectDisplayInfo.dbc.csv",
    "2. Generate SQL for gameobject_template. This will create \"NewObjects.sql\" to insert into your database.",
    "3. Generate APT items. If using the APT system from Wake, this will generate SQL to \"APTObjects.sql\" to insert into your database. This requires tables `apt_spawned` and `apt_template`, and file \"NewObjects.csv\"",
    "4. Help",
    "0. Quit",
]


import os
#for root, dirs, files in os.walk(".", topdown=False):
# #   print(root, "", dirs , "" , files)
##    print(root)
#    for name in files:
#        lets_go = 0
#        if name.find(".wmo") != -1:
#            lets_go = 1
#        elif name.find(".m2") != -1:
#            lets_go = 1
#        
#        if lets_go == 1:
##            print(name)
#            file_name = os.path.join(root, name)
#            file_name = file_name.replace(".\\","")
#            file_name = '"' + file_name + '"'
##            print(file_name)
#            new_entry = new_entry + 1
#            DB_ENTRY = DB_ENTRY + 1
#            new_line = (str(new_entry) + "," + file_name + ",0,0,0,0,0,0,0,0,0,0,-42.593334198,-43.3275909424,-11.2867012024,53.83852005,43.3115272522,66.5477981567,0,\n")
#            print(new_line)
#            imported_write.write(new_line)
#            sql_line = "INSERT INTO `gameobject_template` VALUES (" + str(DB_ENTRY) + ", 5, " + str(new_entry) + ", '" + name + "', '', '', '', 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0);\n"
#            imported_sql.write(sql_line)

def GameObjectDisplayInfo_Run():
    imported_file = open("GameObjectDisplayInfo.dbc.csv")
    imported_write = open("NewObjects.csv", "w+")
    imported_lines = imported_file.readlines()
    new_entry = imported_lines[-1]
    new_entry = new_entry.split(",")
    count = 0
    
    # defines displayid entry
    new_entry = int(new_entry[0]) + 1
    
    for root, dirs, files in os.walk(".", topdown=False):
#        print("go")
        for name in files:
#            print(os.path.join(root, name))
            lets_go = 0
            if name.find(".wmo") != -1:
                lets_go = 1
            elif name.find(".m2") != -1:
                lets_go = 1
            elif name.find(".M2") != -1:
                lets_go = 1
            elif name.find(".WMO") != -1:
                lets_go = 1
           
            if lets_go == 1:
                file_name = os.path.join(root, name)
                file_name = file_name.replace(".\\","")
                file_name = '"' + file_name + '"'
                count = count + 1
                new_line = (str(new_entry) + "," + file_name + ",0,0,0,0,0,0,0,0,0,0,-42.593334198,-43.3275909424,-11.2867012024,53.83852005,43.3115272522,66.5477981567,0,\n")
                print(new_line)
                new_entry = new_entry + 1
                imported_write.write(new_line)
    
    imported_write.close()
    imported_file.close()
    print("Finished processing " + str(count) + " wmos/.m2s and added them to \"NewObjects.csv\".")
    print()
    
def gameobject_template_Run():
    imported_file = open("GameObjectDisplayInfo.dbc.csv")
    imported_write = open("NewObjects.sql", "w+")
    imported_lines = imported_file.readlines()
    count = 0
    display_id = imported_lines[-1]
    display_id = display_id.split(",")
    display_id = (int(display_id[0]) + 1)
    
    user_DB_entry = int(input("Please enter the entry from gameobject_template that you would like to start from: "))
    user_prefix_entry = input("If you would like text before each name, please enter now or leave blank (ie: PREFIXgameobject123.m2): ")
    user_postfix_entry = input("If you would like text after each name, please enter now or leave blank (ie: gameobject123.m2POSTFIX): ")
    
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            lets_go = 0
            if name.find(".wmo") != -1:
                lets_go = 1
            elif name.find(".m2") != -1:
                lets_go = 1
            elif name.find(".M2") != -1:
                lets_go = 1
            elif name.find(".WMO") != -1:
                lets_go = 1
           
            if lets_go == 1:
                file_name = os.path.join(root, name)
                file_name = file_name.replace(".\\","")
                file_name = '"' + file_name + '"'
                count = count + 1
                new_line = user_prefix_entry + name + user_postfix_entry
                new_line = "INSERT INTO `gameobject_template` VALUES (" + str(user_DB_entry) + ", 5, " + str(display_id) + ", '" + new_line + "', '', '', '', 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0);\n"
                print(new_line)
                user_DB_entry = int(user_DB_entry) + 1
                display_id = display_id + 1
                imported_write.write(new_line)
    
    imported_write.close()
    imported_file.close()
    print("Finished processing " + str(count) + " wmos/.m2s and added them to \"NewObjects.sql\".")
    print()
    
def APTObjects_Run():
    imported_file = open("NewObjects.csv")
    imported_write = open("APTObjects.sql", "w+")
    imported_lines = imported_file.readlines()
    count = 0
    display_id = imported_lines[0]
    display_id = display_id.split(",")
    display_id = display_id[0]
    
    user_DB_entry = int(input("Please enter the entry from item_template that you would like to start from: "))
    user_GOB_entry = int(input("Please enter the entry from gameobject_template that you would like to start from: "))
    user_prefix_entry = input("If you would like text before each name, please enter now or leave blank (ie: PREFIX_gameobject123.m2): ")
    user_postfix_entry = input("If you would like text after each name, please enter now or leave blank (ie: gameobject123.m2_POSTFIX): ")
    
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            lets_go = 0
            if name.find(".wmo") != -1:
                lets_go = 1
            elif name.find(".m2") != -1:
                lets_go = 1
            elif name.find(".M2") != -1:
                lets_go = 1
            elif name.find(".WMO") != -1:
                lets_go = 1
           
            if lets_go == 1:
                file_name = os.path.join(root, name)
                file_name = file_name.replace(".\\","")
                file_name = '"' + file_name + '"'
                count = count + 1
                new_line = user_prefix_entry + name + user_postfix_entry
                new_line = "INSERT INTO `item_template` VALUES (" + str(user_DB_entry) + ", 15, 0, -1, '" + new_line + "', 20220, 2, 0, 0, 1, 0, 0, 0, -1, -1, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2000001, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, '', 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, 12340);\n"
                print(new_line)
                imported_write.write(new_line)
                new_line = "INSERT INTO `apt_template` VALUES (" + str(user_DB_entry) + ", " + str(user_GOB_entry) + ");\n"
                print(new_line)
                imported_write.write(new_line)
                display_id = int(display_id) + 1
                user_DB_entry = int(user_DB_entry) + 1
                user_GOB_entry = int(user_GOB_entry) + 1
    
    imported_write.close()
    imported_file.close()
    print("Finished processing " + str(count) + " wmos/.m2s and added them to \"APTObjects.sql\".")
    print()
    
def Help_Run():
    print()
    print("- - - - - - - - - - -")
    print("HELP")
    print("- - - - - - - - - - -")
    print("If you are having issues, please make sure your folder setup is similar to the following image. Any gameobject .M2s/.WMOs should be in the world folder. https://i.gyazo.com/70ada5f7debfdc5aac906a22aecd4611.png")
    print()
    print("Sometimes, when merging NewObjects.csv into GameObjectDisplayInfo.dbc.csv, newlines are created. Make sure that there are no newlines.")
    print()
    print("Need to edit the insert queries to match your database better? Edit this file with notepad!")
    print()
    print("Need more help? Contact me on Discord, grimreapaa#4214")
    print("- - - - - - - - - - -")
    print("HELP")
    print("- - - - - - - - - - -")
    print()

thing = 0
print()
print("- - - - - - - - - - -")
print("WAKE OBJECT GENERATOR")
print("- - - - - - - - - - -")
print()

while thing == 0:
    for x in options:
        print(x)
    
    user_input = int(input("Enter an option number between 1 and " + str(len(options) - 1) + ": "))
    if user_input == 1:
        GameObjectDisplayInfo_Run()
    elif user_input == 2:
        gameobject_template_Run()
    elif user_input == 3:
        APTObjects_Run()
    elif user_input == 4:
        Help_Run()
    elif user_input == 0:
        print()
        print("Goodbye")
        thing = 1
    else:
        print()
        print("Invalid option.")
        print()