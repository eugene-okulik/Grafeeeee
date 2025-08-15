import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', help='add file')
parser.add_argument('-t', '--text', help='text for search')
args = parser.parse_args()


def logs_files():
    for filename in os.listdir(args.file):
        fullpath = os.path.join(args.file, filename)
        with open(fullpath, 'r', encoding='utf-8') as f:
            for i, file_line in enumerate(f):
                words = file_line.strip().split()
                if args.text in words:
                    for idx, word in enumerate(words):
                        if args.text == word:
                            before = words[max(0, idx - 5): idx]
                            after = words[idx+1:idx+6]
                            print(f'Requested text is founded on {i} in {filename}. Consist of ({before}),'
                                  f' ({word}) and ({after})')


logs_files()
