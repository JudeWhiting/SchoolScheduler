import unittest
import sys
sys.path.append('src/SchoolScheduler')
import base
import read_files
import meeting_functions
import main

def add(x, y):
    return x + y

class TestFunctions(unittest.TestCase):

    def test_timetable_creation(self):

        while 1:
            df = meeting_functions.create_table()
            df = meeting_functions.feasible_timetable(df)
            if not df.isin([0]).any().any():
                break
        
        self.assertTrue(not df.isin([0]).any().any())

    def test_local_search(self):
        while 1:
            df = meeting_functions.create_table()
            df = meeting_functions.feasible_timetable(df)
            if not df.isin([0]).any().any():
                break
        start_cost = meeting_functions.objective_function(df)[0]
        df = meeting_functions.local_search(df, 20)
        end_cost = meeting_functions.objective_function(df)[0]

        self.assertTrue(end_cost < start_cost)

    def test_p5_swap(self):
        while 1:
            df = meeting_functions.create_table()
            df = meeting_functions.feasible_timetable(df)
            if not df.isin([0]).any().any():
                break
        df = meeting_functions.local_search(df, 1)
        start_cost = meeting_functions.objective_function(df)[0]
        df = meeting_functions.p5_swap(df)
        end_cost = meeting_functions.objective_function(df)[0]

        self.assertTrue(end_cost <= start_cost)

    def test_feasibility(self):
        while 1:
            df = meeting_functions.create_table()
            df = meeting_functions.feasible_timetable(df)
            if not df.isin([0]).any().any():
                break

        self.assertTrue(meeting_functions.objective_function(df)[0] < 9999)

    def test_feasibility_after_optimisation(self):
        while 1:
            df = meeting_functions.create_table()
            df = meeting_functions.feasible_timetable(df)
            if not df.isin([0]).any().any():
                break
        df = meeting_functions.local_search(df, 1)
        df = meeting_functions.p5_swap(df)

        self.assertTrue(meeting_functions.objective_function(df)[0] < 9999)

        
if __name__ == '__main__':
    unittest.main()
