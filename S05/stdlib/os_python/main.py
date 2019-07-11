import os


# os.system("ipconfig")
f = os.popen("ipconfig")
text = f.read()

res = os.getcwd()
print(res)
# os.chdir("../../../../..")
os.system("dir")