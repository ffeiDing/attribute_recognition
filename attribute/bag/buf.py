#0 NA  1 2 3 4

import os
def travel(root,all):
    files = os.listdir(root)
    for file in files:
        if os.path.isdir(file):
            travel(os.path.join(root,file),all)
        elif file[-4:] == '.jpg':
            all.append(os.path.join(root,file))
    print(all)

all = []
travel('.',all)

