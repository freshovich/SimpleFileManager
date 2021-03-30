from FileManager import FileManager
from Properties import FMan_way

my_FMan = FileManager(FMan_way)
print("Current way: ", my_FMan.get_curr_dir())


while True:
    command = input(">>> ")
    if command.split(' ')[0] == "make_dir":
        new_dir = command.split(' ')[1]
        my_FMan.make_dir(new_dir)

    elif command.split(' ')[0] == "del_dir":
        dirname = command.split(' ')[1]
        my_FMan.del_dir(dirname)

    elif command.split(' ')[0] == "ch_dir":
        dirname = command.split(' ')[1]
        my_FMan.ch_dir(dirname)

    elif command.split(' ')[0] == "make_file":
        filename = command.split(' ')[1]
        my_FMan.make_file(filename)

    elif command.split(' ')[0] == "write_file":
        filename = command.split(' ')[1]
        text = ' '.join(command.split(' ')[2:])
        my_FMan.write_file(filename, text)

    elif command.split(' ')[0] == "read_file":
        filename = command.split(' ')[1]
        my_FMan.read_file(filename)

    elif command.split(' ')[0] == "del_file":
        filename = command.split(' ')[1]
        my_FMan.del_file(filename)

    elif command.split(' ')[0] == "copy_file":
        currpath = command.split(' ')[1]
        newpath = command.split(' ')[2]
        my_FMan.copy_file(currpath, newpath)

    elif command.split(' ')[0] == "move_file":
        currpath = command.split(' ')[1]
        newpath = command.split(' ')[2]
        my_FMan.move_file(currpath, newpath)

    elif command.split(' ')[0] == "rename_file":
        filepath = command.split(' ')[1]
        newname = command.split(' ')[2]
        my_FMan.rename_file(filepath, newname)

    elif command.split(' ')[0] == "curr":
        print("Current way:", my_FMan.get_curr_dir())

    elif command == "tree_list":
        print("Folder contents:")
        my_FMan.tree_list()

    elif command == "help" or command == "?":
        my_FMan.helper()

    elif command == "quit" or command == "q":
        print("See you later!")
        break
    else:
        print("Error command, try (help) or (?).")