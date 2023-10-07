import os
def list_files_in_directory(directory_path):
    file_names = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_names.append(file)
    return file_names

directory_path = "/Users/mitisha.agarwal/Documents"
files_list = list_files_in_directory(directory_path)
for file in files_list:
    print(file)
