Subjects = ['math','eng','phy','bio','chem','mus','ict','his','geo','art','per']

# Open the file in write mode to overwrite it
with open('src/data/teachers.txt', 'w') as file:
    # Iterate through each line
    for i, hours in enumerate([4,4,3,3,3,1,1,2,2,1,1]):
            for j in range(hours*2):
                file.write(f'spesh , {Subjects[i]}\n')

    for i in range(100):
         file.write(f'generic , \n')