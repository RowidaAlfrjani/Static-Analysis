import sys
from pathlib import Path

if __name__ == '__main__':
    root_folder = "G:/My Drive/10k-criteria"
    i = 0
    for f in Path(root_folder).rglob("*_scored_label_list.csv"):
        i = i + 1

    print(i)