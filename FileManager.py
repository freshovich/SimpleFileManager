import os
import shutil
from pathlib import Path


class FileManager:
    def __init__(self, work_dir):
        self.WORK_DIR = Path(work_dir).absolute()
        try:
            os.chdir(self.WORK_DIR)
        except FileNotFoundError:
            print("The working folder could not be found.")
        self.curr_dir = Path(work_dir).absolute()
        self.last_dir = self.WORK_DIR.name


    def helper(self):
        print("Hello! It's a FileManager! Check it out:\n")
        print("quit or q                     Exit")
        print("make_dir [name]               Make a folder")
        print("del_dir [name]                Del folder (for name)")
        print("ch_dir [name]                 Moving between folders")
        print("make_file [name]              Creating empty files with the name")
        print("write_file [name] [text]      Writing text to a file")
        print("read_file  [name]             Check the contents of a text file")
        print("del_file  [name]              Del file (for name)")
        print("copy_file [name] [new_dir]    Copy files from folder to folder")
        print("move_file [name] [new_dir]    Moving Files")
        print("rename_file [name] [new_name] Rename files")
        print("tree_list                     Show folder patter")
        print("curr                          Current directory")
        print("help or ?                     Info")

    def get_curr_dir(self):
        return os.getcwd()

    def tree_list(self):
        if os.listdir(path=self.curr_dir):
            for item in os.listdir(path=self.curr_dir):
                print(item)
        else:
            print("The folder is empty.")

    def make_dir(self, path):
        """ 1. Создание папки по имени."""
        try:
            if os.path.exists(path):
                print("A folder with this name already exists.")
            else:
                os.makedirs(str(path))
                print(f'Folder {path.split("/")[-1]} was created successfully.')
        except FileNotFoundError:
            print("Invalid path specified.")

    def del_dir(self, path):
        """ 2. Удаление папки по имени. """
        if os.path.isdir(path):
            shutil.rmtree(str(path), ignore_errors=True)
            print("Folder", path.split("/")[-1], "deleted.")
        else:
            print("The name of the folder was not found.")

    def ch_dir(self, path):
        """ 3. Перемещение между папками."""
        try:
            if len(path) != 0:
                if path == "..":
                    if self.last_dir in str(self.curr_dir.parent):
                        os.chdir(self.curr_dir.parent)
                        self.curr_dir = self.WORK_DIR.joinpath(self.curr_dir.parent)
                        print("Current way:", self.curr_dir)
                    else:
                        print("outside of the working folder")
                else:
                    os.chdir(path)
                    self.curr_dir = self.WORK_DIR.joinpath(path)
                    print("Current way:", self.curr_dir)
        except FileNotFoundError:
            print("The name of the folder was not found.")
        except OSError:
            print("The name of the folder was not found.")

    def make_file(self, path):
        """ 4. Создание файла по имени. """
        try:
            if os.path.exists(path):
                print("The name of the file was not found.")
            else:
                open(path, "w", encoding="utf-8").close()
                print('File was created.')
        except FileNotFoundError:
            print("The way to file is not found")


    def write_file(self, path, inner):
        """ 5. Запись в текстовый файл. """
        try:
            self.curr_dir.joinpath(path).write_text(inner)
            print(f"Info '{inner}' successfully recorded in {path}.")
        except FileNotFoundError:
            print("File in not found")

    def read_file(self, path):
        """ 6. Просмотр содержимого текстового файла. """
        try:
            if os.path.exists(path):
                print(str(self.curr_dir.joinpath(path).read_text()))
            else:
                print("The name of the file was not found")
        except OSError:
            print("The name of the file was not found")

    def del_file(self, path):
        """ 7. Удаление файла по имени. """
        try:
            if os.path.exists(path):
                os.remove(self.curr_dir.joinpath(path))
                print(f"file {path} was deleted.")
            else:
                print("The name of the file was not found")
        except OSError:
            print("The name of the file was not found")

    def copy_file(self, curr_path, new_path):
        """ 8. Копирование файлов. """
        try:
            if os.path.exists(curr_path):
                shutil.copy2(curr_path, new_path)
                print(f"file was copied to {new_path}")
            else:
                print("The name of the file was not found")
        except OSError:
            print("The name of the file was not found")

    def move_file(self, curr_path, new_path):
        """ 9. Перемещение файлов. """
        try:
            if os.path.exists(curr_path):
                os.replace(curr_path, new_path)
                print(f"File moved from {curr_path} to {new_path}")
            else:
                print("The name of the file was not found")
        except OSError:
            print("The name of the file was not found")

    def rename_file(self, path, new_name):
        """ 10. Переименование файлов. """
        try:
            if os.path.exists(path):
                self.curr_dir.joinpath(path).rename(new_name)
                print(f"File moved to {new_name}")
            else:
                print("The name of the file was not found")
        except FileExistsError:
            print("The file has already been created")
        except OSError:
            print("The name of the file was not found")