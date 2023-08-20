print("hello world")

# ***Constants***
False = 1   # this does not mean that the variable name of "False" stores the value 1
            # it gets an error because "False" is a reserved word
            # that can't be used as variable names / identifiers

# ***Variables***
a = 1       # storing value 1 at the location with name "a"
b = 2
a = b       # assign the value location name "b" to the location name "a".
            # "a" will have the value equal to "b". It is the same with a = 2

# ***Operations / numeric expressions***
c = 1 + 2   # addition, resulting 3
c = 2 - 1   # subtraction, resulting 1
c = 1 * 2   # multiplication, resulting 2
c = 2 / 1   # division, resulting 2
c = 1 ** 2  # power, resulting 1
c = 5 % 3   # remainder, resulting 2

# ***Types***
eee = 'hello ' + 'world'    # the type of "eee" is string
print(type(eee))            # it will display the type of the variable eee
eee = eee + 1               # during the execution, it will generate an error due to type difference

# ***Inputs***
name = input('Please input your name: ')    # the variable "name" stores the input from a user
print('Welcome', name)                      # it prints the stored "name" variable with "Welcome"

# ***Conditional Steps***
# 1. One-way decision
x = 5
if x < 10:                  # the comparison operator will compare the x value with 10,
    print('Smaller')        # then generate the following output with the comparison
if x > 20:
    print("Bigger")
print('Finish')             # the output will generate: Smaller\nFinish

# 2. Multi-way decision
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('Finish')

# ***try-except***
# program that handles non-numeric input
hour = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    int(hour)
    int(rate)
except:
    print('Error, please enter numeric input')

# ***function***
def thing():
    print('Hello')

thing()
print('World')
thing()             # at this point, the result will be 'Hello\nWorld\nHello'
                    # as the function is stored and called two times

# ***function with parameter inputs***
hello = 'Hello'
def printing(x):
    print(x)

printing(hello)
print('World')
printing(hello)     # the result will be printed exactly the same with
                    # the previous function without parameters

# ***Loops***
# indefinite loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# definite loop
for i in [5, 4, 3, 2, 1]:   # or can be written; for i in range(5):
    print(i)
print('Done!')

# ***greedy matching***
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
# result will be ['From: Using the :']

# ***non-greedy matching***
y = re.findall('^F.+?:', x)
print(y)
# result will be ['From:']


# ***network programming***
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pre4e.org'), 80)                                # 80 is a common internet port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()   # encode to send
sock.send(cmd)

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

sock.close()

# ***network programming_Built-in HTTP Request library***
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# ***Data Visualization***
data = [[0, 31.3019316538656, 120.76745961353, -1],
        [10, 31.3021382523654, 120.767529047259, 1.07],
        [20, 31.3022098896158, 120.767596405547, 0.57],
        [30, 31.302236, 120.767528, 0.87],
        [40, 31.30246, 120.767728, 0.46],
        [50, 31.3025416, 120.767605, 0],
        [60, 31.302697, 120.76755, 0],
        [70, 31.3028358, 120.767575, 1.00],
        [80, 31.3029333, 120.767588, 0.57],
        [90, 31.3030795, 120.767493, 0],
        [100, 31.3033512, 120.767487, 1.31],
        [110, 31.3035104, 120.767624, 1.37],
        [120, 31.30365, 120.76777, 1.10],
        [130, 31.3037863, 120.767824, 1.23],
        [140, 31.3038909, 120.768001, 1.49],
        [150, 31.3039771, 120.76818, 1.37],
        [160, 31.3040516, 120.768369, 1.45],
        [170, 31.3040673, 120.768258, 1.45],
        [180, 31.303999, 120.76871, 1.29],
        [190, 31.3040138, 120.7689, 1.46],
        [200, 31.3039883, 120.769058, 1.38],
        [210, 31.3039837, 120.769179, 1.11],
        [220, 31.3039634, 120.769351, 1.19],
        [230, 31.3039325, 120.769523, 1.52],
        [240, 31.303734, 120.76959, 1.47],
        [250, 31.3035495, 120.769594, 1.49],
        [260, 31.3034593, 120.769675, 1.11],
        [270, 31.303414, 120.769786, 1.28],
        [280, 31.3033729, 120.769913, 1.29],
        [290, 31.3032959, 120.770065, 1.14],
        [300, 31.3032257, 120.770243, 1.43],
        [310, 31.3031936, 120.770436, 1.46],
        [320, 31.3032596, 120.770501, 0.67],
        [330, 31.3033994, 120.770457, 1.25],
        [340, 31.3035345, 120.77043, 1.045],
        [350, 31.3036469, 120.770377, 1.13],
        [360, 31.3037858, 120.770354, 1.28],
        [370, 31.3039192, 120.770363, 1.32],
        [380, 31.3040301, 120.770409, 1.30],
        [390, 31.304194, 120.770366, 1.28],
        [400, 31.304351, 120.770327, 1.48],
        [410, 31.3044777, 120.770339, 1.17],
        [420, 31.3045842, 120.770271, 1.43],
        [430, 31.3046164, 120.770115, 1.66],
        [440, 31.3046327, 120.769966, 1.43],
        [450, 31.3046485, 120.769822, 1.47],
        [460, 31.3045829, 120.769641, 1.32],
        [470, 31.304558, 120.769463, 1.44],
        [480, 31.3045415, 120.769302, 1.09],
        [490, 31.3045464, 120.769143, 1.29],
        [500, 31.3045852, 120.768974, 1.30],
        [510, 31.3045596, 120.768817, 1.27],
        [520, 31.3045428, 120.768649, 1.35],
        [530, 31.3045512, 120.7685, 1.23],
        [540, 31.3045521, 120.768334, 1.34],
        [550, 31.3044699, 120.768156, 1.10],
        [560, 31.3044757, 120.76799, 1.44],
        [570, 31.3044712, 120.767798, 1.45],
        [580, 31.3045004, 120.76762, 1.49],
        [590, 31.304509, 120.767457, 1.43],
        [600, 31.3044937, 120.767312, 1.42]]

import folium
from folium.features import DivIcon

g_map = folium.Map(location=[31.303, 120.7685], zoom_start=18)

for time, lat, long, speed in data:

    if (speed < 0.61):
        folium.Circle(
            location=[lat, long],
            radius=1,
            color="yellow"
        ).add_to(g_map)

    elif (0.61 <= speed < 1.22):
        folium.Circle(
            location=[lat, long],
            radius=1,
            color="orange"
        ).add_to(g_map)

    else:
        folium.Circle(
            location=[lat, long],
            radius=1,
            color="red"
        ).add_to(g_map)

    folium.map.Marker([lat + 0.0001, long - 0.00002],
                      icon=DivIcon(
                          icon_size=(1, 1),
                          icon_anchor=(0, 0),
                          html='<div style="font-size: 9.5pt">%s</div>' % speed,
                      )
                      ).add_to(g_map)

g_map.save('map.html')
g_map
