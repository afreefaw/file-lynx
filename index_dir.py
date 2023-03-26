import os
from pathlib import Path

def get_file_extension(file_path):
    return Path(file_path).suffix

def build_directory_graph(dir_path):
    dir_structure = {}

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            dir_structure[item] = build_directory_graph(item_path)
        elif os.path.isfile(item_path):
            file_ext = get_file_extension(item_path)
            dir_structure[item] = file_ext

    return dir_structure

def main(dr):
    root_directory = dr
    directory_graph = build_directory_graph(root_directory)
    return directory_graph




if __name__ == '__main__':
    main()