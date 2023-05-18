import subprocess
from os import listdir
from os.path import isfile, join

path = "./Dataset/Evaluation/"
txtfiles = [f for f in listdir(path) if isfile(join(path, f))]
txtfiles = [f for f in txtfiles if f.endswith(".txt") \
            and (f.find('Dofloo') != -1 or f.find('Xor') != -1)] # filter specific report
txtfiles = ['Xorddos-MS.txt']
print(f"Continue to run these reports: {txtfiles}")

# execute paper's command line
for txt in txtfiles:
    cmd = f"python main.py -M attackGraphGeneration -R \"{path}{txt}\" -O ./Output/{txt}.pdf"
    subprocess.call(cmd, shell=True)

# import os
# os.system('dir /d')
# subprocess.call('dir /d', shell=True)