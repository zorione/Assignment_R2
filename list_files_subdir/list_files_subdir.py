import os
def list_files_and_subdir(directory_path):
    file_and_subdir_names = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):          ## If subdirectory, add to the list
          file_and_subdir_names.append(item)
        elif os.path.isfile(item_path):        ## If file, add to the list
          file_and_subdir_names.append(item)
    return file_and_subdir_names

directory_path = "/Users/mitisha.agarwal/Documents/efr"
file_and_folder_names = list_files_and_subdir(directory_path)

for file_or_subdir_name in file_and_folder_names:
  print(file_or_subdir_name)
