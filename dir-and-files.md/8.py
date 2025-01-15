import os
p=(r"C:/Users/Aitzh/OneDrive/Рабочий стол/lab6/dir-and-files.md/M.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")