#coding = utf-8
#0 NA
#age:
#child 1 teenage 2 adult 3 old 4
#gender:
#female 1 male 2
#bag:
#yes:1 no:2
#color:
#black 1 blue 2 green 3 red 4 white(gray) 5 yellow 6 other 7
#direction:
#up 1 down 2 right 3 left 4
#hair:
#long 1 short 2
#upper:
#black 1 blue 2 green 3 red 4 white 5 grey 6 yellow 7 purple 8 other 9
#lower:
#black 1 blue 2 green 3 red 4 white 5 grey 6 yellow 7 purple 8 other 9
#mask:
#yes:1 no:2
#shoes:
#black 1 white 2 other 3
#type:
#bicycle 1 motorcycle 2 tricycle 3
#helmet:
#hat 1 helmet 2 no 3

# age gender hair shoes bag upper lower mask helmet color type direction
import os
def travel(root,all):
    files = os.listdir(root)
    for file in files:
        # print(file)
        if os.path.isdir(file):
            travel(os.path.join(root,file),all)
        elif file[-4:] == '.jpg':
            all.append(os.path.join(root,file))
    return all
all = []
travel(os.path.abspath('.'),all)
def get_id(s):
    """
    :param input: string
    :return:
    """
    last = s.split('_')[-1]
    return last[:-4]



# print(get_id('./helmet/helmet/bike_1114411402_411.jpg'))

def get_pic2attr(all):
    pic2attr = {}
    for x in all:
        id = get_id(x)
        if id in pic2attr:
            pic2attr[id].append(x)
        else:
            pic2attr[id] = [x]
    return pic2attr

print(sorted(get_pic2attr(all).items(),key = lambda x : len(x[1]),reverse = True))




