import os

root_dir = f"{os.getcwd()}\\database6"
s=0
for i in range(56):
    # print(i, len(os.listdir(f"{root_dir}\\{i}\\")))
    s+=len(os.listdir(f"{root_dir}\\{i}\\"))
print(s/56)