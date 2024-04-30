import meeting_functions
import pandas as pd




def main():

    solution = meeting_functions.process()

    with pd.ExcelWriter('src/output/student_timetables.xlsx', engine='xlsxwriter') as writer:

        print('Exporting results. Please wait...')

        # iterate through each student
        for student in meeting_functions.Students[:5]:

            # get the students' individual timetable
            student_timetable = meeting_functions.individual_timetable(solution, student)
            # write the timetable to an excel sheet
            student_timetable.to_excel(writer, sheet_name=student.name)

            # format the excel sheet
            worksheet = writer.sheets[student.name]
            # set row and column width
            #worksheet.set_column('A:F', 15)
            worksheet.set_default_row(60)




if __name__ == '__main__':

    main()

    print('Done!')