

# Open the file in write mode to overwrite it
with open('src/data/students.txt', 'w') as file:
    # Iterate through each line
    sets = [4,3,2,1]
    for i, group in enumerate(['7N','7S','8N','8S','9N','9S','10N','10S','11N','11S']):
        for x in range(120):
            file.write(f'{i*120 + x} , {group} , {sets[x%4]} , {sets[x%4]} , {sets[x%4]} , {sets[x%4]}\n')