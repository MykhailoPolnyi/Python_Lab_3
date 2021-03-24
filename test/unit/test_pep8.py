import unittest
import pep8
import os


class TestPEP8(unittest.TestCase):
    def test_pep8(self):
        self.file_structure = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        print("Testing for PEP8 compliance of python files in {}".format(self.file_structure))
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        filenames = []
        for root, _, files in os.walk(self.file_structure):
            python_files = [f for f in files if f.endswith('.py') and "examples" not in root]
            for file in python_files:
                if len(root.split('samples')) != 2:
                    filename = '{0}/{1}'.format(root, file)
                    filenames.append(filename)
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0, 'PEP8 style errors: %d' % check.total_errors)
