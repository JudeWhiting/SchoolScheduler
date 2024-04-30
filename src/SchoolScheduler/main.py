import meeting_functions
import pandas as pd




def main():

    solution = meeting_functions.process()

    with pd.ExcelWriter('src/output/student_timetables.xlsx', engine='xlsxwriter') as writer:

        print('Exporting results. Please wait...')

        # iterate through each student
        for student in meeting_functions.Students:

            # get the students' individual timetable
            student_timetable = meeting_functions.individual_timetable(solution, student)
            # write the timetable to an excel sheet
            student_timetable.to_excel(writer, sheet_name=student.name)

            # format the excel sheet
            worksheet = writer.sheets[student.name]
            worksheet.set_default_row(60)


    with pd.ExcelWriter('src/output/teacher_timetables.xlsx', engine='xlsxwriter') as writer:

        # iterate through each teacher
        for teacher in meeting_functions.Teachers:

            # get the current teachers' individual timetable
            t_timetable = meeting_functions.teacher_timetable(solution, teacher)
            # write the timetable to an excel sheet
            t_timetable.to_excel(writer, sheet_name=teacher.name)

            # format the excel sheet
            worksheet = writer.sheets[teacher.name]
            worksheet.set_default_row(60)




if __name__ == '__main__':

    main()

    print('Done!')