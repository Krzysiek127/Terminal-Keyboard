# Terminal Piano by Krzysiek127
# 27.11.2019 19:06 UTC+01 Warsaw Time Zone

# Soyuz Nierushimyj Riespublik Svobodnykh

import msvcrt as mv
import winsound as ws

tune = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 587.33, 659.25]  # cdefgabcde
keys = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
# keys = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
time = 750  # ms

print("Terminal Piano by Krzysiek127")

try:
    with open("notes.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    entries = len(content)

    file = bool(input("Open from file? "))
except FileNotFoundError:
    file = False
print("Load from file: ",file)

if len(tune) != len(keys): raise Exception("Lists don't contain the same amount of things!")

while not file:
    key = mv.getch().decode('utf-8')
    try:
        ws.Beep(round(tune[keys.index(key)]), time)
    except ValueError:
        if key=="f":
            print("Can we get Fs in the chat?")

if file:
    for i in range(0,entries):
        ws.Beep(int(tune[int(content[i])]),time)
