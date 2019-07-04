#        C:\Users\Student\PycharmProjects\mft-05\S04\file_manipulation\read_file_relative_path.py
# path = "C:\Users\Student\PycharmProjects\mft-05\S04\functions\README.md"

# path = "./../functions/README.md"
# path = '../../S01/git/readme.md'
# .  --> current directory
# .. --> parent directory

path = "../../../../Desktop/a.txt"
f = open(path)
text = f.read()
print(text)