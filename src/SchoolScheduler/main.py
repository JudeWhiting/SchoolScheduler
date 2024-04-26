import Meeting_functions
import pandas as pd


def main():
    solution = Meeting_functions.process(3)
    #solution = Meeting_functions.readable_timetable(solution)
    
    #solution.to_excel('src/output/results.xlsx')
    with pd.ExcelWriter('src/output/results.xlsx', engine='xlsxwriter') as writer:
        # Write each DataFrame to a separate sheet
        for student in Meeting_functions.Students[:5]:
            student_timetable = Meeting_functions.individual_timetable(solution, student)
            student_timetable.to_excel(writer, sheet_name=student.name)

            #workbook  = writer.book
            worksheet = writer.sheets[student.name]
            
            # Set column width for columns A to F
            #worksheet.set_column('A:F', 15)  # Adjust the width as needed
            worksheet.set_default_row(60)


if __name__ == '__main__':
    main()