import unittest
from calculate_submarine_distance import calculate_position, process_course

#run test with python -m unittest calculate_submarine_distance_test.py

class SubmarinePositionTest(unittest.TestCase):
    def test_calculate_position_normal_distances(self):
        distances = calculate_position('./InputFiles/submarine_kata_test_input.txt')
        self.assertEqual((15, 10, 150), distances)

class ProcessCourseTest(unittest.TestCase):
    def test_process_course_simple_course(self):
        testValues = [('forward', '10'),('down', '10')]
        distances = process_course(testValues)
        self.assertEqual((10, 10, 100), distances)

    def test_process_course_complex_course(self):
        testValues = [
            ('forward', '5'),
            ('down', '5'),
            ('forward', '8'),
            ('up', '3'),
            ('down', '8'),
            ('forward', '2')
        ]
        distances = process_course(testValues)
        self.assertEqual((15, 10, 150), distances)

    def test_process_course_raise_error_for_negative_course_instruction_value(self):
        testValues = [
            ('forward', '5'),
            ('down', '-1')
        ]
        self.assertRaises(ValueError, process_course, testValues)

    def test_process_course_raise_error_for_nonnumerical_course_instruction_value(self):
        testValues = [
            ('forward', '5'),
            ('down', 'six')
        ]
        self.assertRaises(ValueError, process_course, testValues)

    def test_process_course_raise_error_for_no_course_instruction_value(self):
        testValues = [
            ('forward', '5'),
            ('down')
        ]
        self.assertRaises(ValueError, process_course, testValues)

    def test_process_course_raise_error_for_invalid_course_instruction_type(self):
        testValues = [
            ('forward', '5'),
            ('dive', '6')
        ]
        self.assertRaises(ValueError, process_course, testValues)
