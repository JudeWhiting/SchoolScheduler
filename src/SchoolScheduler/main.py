from Meeting_functions import *

def main():
    df = create_table()
    Meetings = create_meetings()
    
    df = assign_feasible_meetings()
    print(df)


if __name__ == '__main__':
    main()