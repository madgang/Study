import sys
from report import get_descript
print("import start")

description = get_descript()
#print("Today's Wether :",description)
print('Program arguments:',sys.argv)
print('Standalone program work',description)

for place in sys.path:
    print(place)

for place in sys.path:
    print(place)
