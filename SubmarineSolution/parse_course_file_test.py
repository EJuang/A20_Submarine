import unittest
from parse_course_file import parse_course_file

#run test with python -m unittest parse_course_file_test.py

class ParseCourseFileTest(unittest.TestCase):
    def test_can_read_file(self):
        filePath = './InputFiles/submarine_kata_test_input.txt'
        expectedResult = [
            ("forward", "5"),
            ("down", "5"),
            ("forward", "8"),
            ("up", "3"),
            ("down", "8"),
            ("forward", "2")
        ]
        instruction_sets = parse_course_file(filePath)
        self.assertEqual(expectedResult, instruction_sets)

