from unittest import TestCase
import sudoku.create as sudoku 

class CreateTest(TestCase):
    
    
    def setUp(self):
        self.testDict = {}
        
    def setUpDict(self, setLevel):
        self.testDict["level"] = 1

    def test100_shouldReturnLevel1Stub(self):
        self.setUpDict(1)
        self.assertEqual(sudoku._create(self.testDict), 1)
