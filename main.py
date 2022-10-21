import re
from collections import defaultdict


def check_name(name: str) -> bool:
    return re.fullmatch(r'[\da-zA-Z]*', name) is not None


def get_file(directory: list, path: str):
    file_dict = defaultdict(int)
    for file in directory:
        file_dict[file] += 1
    max_file_name = ""
    for file in file_dict:
        if check_name(file) and file_dict[file] == 1 and len(path) + len(file) + 1 < 256:
            if len(max_file_name) < len(file):
                max_file_name = file
    if len(max_file_name) == 0:
        return "/"
    return path + "/" + max_file_name


def dfs(directory: dict, path: str):
    if len(directory) == 0:
        return path
    max_path = "/"
    for dir in directory:
        if check_name(dir) and len(dir) + len(path) + 1 < 256:
            if isinstance(directory[dir], list):
                if len(directory[dir]) == 0:
                    _path = path + "/" + dir
                else:
                    _path = get_file(directory[dir], path + "/" + dir)
            else:
                _path = dfs(directory[dir], path + "/" + dir)
            if len(_path) > len(max_path):
                max_path = _path
    return max_path


def biggestPath(X: dict) -> str:
    return dfs(X, "")


if __name__ == "__main__":
    print(biggestPath({'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}))
    print(biggestPath({'dir1': ['file1', 'file1']}))
    print(biggestPath({'dir1': ['file1', 'file2', 'file2']}))