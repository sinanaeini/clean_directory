import shutil
import os
from src.utiles import read_json
from pathlib import Path
import sys


class CleanDirectory:
    def __init__(self, j_path, file_path):
        self.format = read_json(j_path)
        self.file_path = file_path

    @staticmethod
    def make_file_path(path):
        x = os.walk(path)
        for dir, _, file in x:
            for item in file:
                pth = dir + '/' + item
                yield pth

    def clean_dir(self):
        for item in self.make_file_path(self.file_path):
            for type in self.format:
                if Path(item).suffix in self.format[type]:
                    (Path(self.file_path / type).
                     mkdir(parents=True, exist_ok=True)
                     )
                    shutil.move(str(item), str(self.file_path / type))
                    break


if __name__ == '__main__':
    print(sys.argv)
    j_path = Path(sys.argv[1])
    file_path = Path(sys.argv[2])
    dir = CleanDirectory(j_path, file_path)
    dir.clean_dir()
print('done')
