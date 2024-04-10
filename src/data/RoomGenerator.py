# Open the file in read mode and read all lines
with open('src/data/rooms.txt', 'r') as file:
    lines = file.readlines()

subjects = ['math','eng','phy','bio','chem','mus','ict','his','geo','art','per']

# Open the file in write mode to overwrite it
with open('src/data/rooms.txt', 'w') as file:
    # Iterate through each line
    for subject in subjects:
        for i in range(16):
            file.write(f'{subject}{i} , {subject}\n')


