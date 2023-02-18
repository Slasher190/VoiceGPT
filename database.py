import os

class FileHandler:
    def create_file(self, file_path):
        try:
            with open(file_path, 'w'):
                pass
            print(f"File created: {file_path}")
        except Exception as e:
            print(f"Error creating file: {e}")

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"File deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print(f"File does not exist: {file_path}")

    def file_exists(self, file_path):
        if os.path.exists(file_path):
            print(f"File exists: {file_path}")
            return True
        else:
            print(f"File does not exist: {file_path}")
            return False

class TextFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def append_text(self, text):
        with open(self.file_path, "a") as f:
            f.write(text)
        print(f"Text appended to file: {self.file_path}")

    def delete_text(self, text):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        with open(self.file_path, "w") as f:
            for line in lines:
                if line.strip() != text:
                    f.write(line)
        print(f"Text deleted from file: {self.file_path}")

    def read_text(self):
        with open(self.file_path, "r") as f:
            text = f.read()
        return text

class Folder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def create(self):
        try:
            os.makedirs(self.folder_path)
            print(f"Folder created: {self.folder_path}")
        except FileExistsError:
            print(f"Folder already exists: {self.folder_path}")

    def delete(self):
        try:
            os.rmdir(self.folder_path)
            print(f"Folder deleted: {self.folder_path}")
        except FileNotFoundError:
            print(f"Folder does not exist: {self.folder_path}")

    def exists(self):
        return os.path.isdir(self.folder_path)
