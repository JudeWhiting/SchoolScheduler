HOW TO USE

First:
- You will need to input data into the files in the 'data' folder, located in 'src/data', or just use the test data that's already there.
- If you want to use your own data, please delete the contents of students2 of the files and format your data as follows:
- For students.txt: (student's name) , (student's group) , (student's tutor group) , (student's maths set) , (student's english set) , (student's science set)
- For groups.txt: just write a list of the group names on separate lines
- For subjects.txt: (subject name) , (number of hours per week)
- note: make sure the hours of the subjects add up to 25
- For teachers.txt: (teacher's name) , (teacher's classroom) , (teacher's specialty subject)

Second:
- Ensure all dependencies are installed. these can be found in 'requirements.txt'

Third:
- Run the program by opening main.py, located in 'src/SchoolScheduler'.
- The program will ask you to enter how many sets there are in each group. If you are using the first set of test data, enter 5 or below. If you are using the second set of test data, enter 3 or below. If you are using your own data, enter any number but be aware that this number must be suitable for the amount of teachers there are.
- Next, the program will ask you how long you want it to run for. 3 and below are recommended, but if you want to push it to its limits choose 4.
- note: the time taken also depends on how large the dataset being used is.
- Finally, select which dataset you want to use. entering 1 will use the data in the files without a '2' in the name. entering 2 will.

Fourth:
- The program should take anywhere from 30 seconds to an hour to complete (depending on the factors mentioned above).
- a value called 'end result' will be printed to the console. This number indicates how optimised the timetable is. If it is below 9999, you can be sure that the timetable is feasible.
- When you get a message saying 'Done!', check in 'src/output'. Here you can see every indivdual student and teacher timetable, ready for use!

Note:
- you can quickly run a test on the program by navigating to 'tests/test_SchoolScheduler.py'. This will check to see that all of the code is working properly