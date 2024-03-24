import unittest
from parse_course_file import parse_course_file

class ParseCourseFileTest(unittest.TestCase):
    def test_can_read_file(self):
        filePath = './TestingFiles/submarine_kata_test_input.txt'
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

