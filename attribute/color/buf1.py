import os
def travel(root,all):
    files = os.listdir(root)
    for file in files:
        # print(file)
        if os.path.isdir(file):
            if file == 'gray':
                print('hhdadadjaldjladj')
            travel(os.path.join(root,file),all)
        elif file[-4:] == '.jpg':
            all.append(os.path.join(root,file))
    return all


all = []
print(travel(os.path.abspath('.'),all))
