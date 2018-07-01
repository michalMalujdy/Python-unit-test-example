'''Calculates lines and characters in a text file'''

#The module required for unit tests. It comes from standard libraries.
import unittest
import os

#The method to be tested
def analyze_text(filename):
    '''Analize a text containing file by counting the number of character
    and lines
    
    Args: 
        filename: The name of the file to analyze
    
    Rises:
        IOError: If the file cannot be read
        
    Returns: 
        number of characters
        number of lines'''

    with open(file = filename, mode = 'rt', encoding = 'utf-8') as file:
        text = file.read()
        characters_count = len(text)
        lines_count = len([char for char in text if char == '\n']) + 1
        return characters_count, lines_count

#The test class needs to derive from unittest.TestCase.
class TextAnalyzerUnitTests(unittest.TestCase):
    '''Unit tests for the functionality provided by analyze_text()'''
    
    #So called fixture. This one is run BEFORE all tests so it can be used for
    #enviroment prearation such as creating text file for this case.
    #The name is relevant.
    def setUp(self):
        self.filename = 'test_file.txt'
        self._text = 'Some\nrandom text.\nCompletely random.\nWith a few lines'
        
        with open(file = self.filename, mode = 'wt', encoding = 'utf-8') as file:
            file.write(self._text)


    #So called fixture. This one is run AFTER all tests so it can be used for
    #enviroment enclosure such as removing text file created for test methods.
    #The name is relevant.
    def tearDown(self):
        os.remove(self.filename)


    #test method must have 'test' prefix in the name and recievie self.
    def test_function_runs(self):
        analyze_text(self.filename)


    def test_count_correct_number_of_characters(self):
        chars, _ = analyze_text(self.filename)
        self.assertEqual(chars, 53)


    def test_count_correct_number_of_lines(self):
        _, lines = analyze_text(self.filename)
        self.assertEqual(lines, 4)


    #This is how you assert a function throws an exception
    def test_rise_IOError_if_cant_read_file(self):
        with self.assertRaises(IOError):
            analyze_text('not-exisiting-filename.txt')

if __name__ == '__main__':

    #Invocation of all test methods that are included in test classes.
    unittest.main()