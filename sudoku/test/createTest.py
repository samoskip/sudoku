from unittest import TestCase
import sudoku.create as sudoku 

class CreateTest(TestCase):
    
    
    def setUp(self):
        self.testDict = {}
        self.INVALIDLEVEL = {'status':'error: invalid level'}
        
    def setUpDict(self, setLevel):
        self.testDict["level"] = setLevel




    def test100_010_shouldReturnLevel1Stub(self):
        self.setUpDict('1')
        self.assertEqual(sudoku._create(self.testDict), "This is level one")

    def test100_020_shouldReturnLevel2Stub(self):
        self.setUpDict('2')
        self.assertEqual(sudoku._create(self.testDict), "This is level two")

    def test100_030_shouldReturnLevel3Stub(self):
        self.setUpDict('3')
        self.assertEqual(sudoku._create(self.testDict), "This is level three")
        
    def test100_040_shouldReturnLevel4Stub(self):
        self.setUpDict('4')
        self.assertEqual(sudoku._create(self.testDict), "This is level four")
        
    def test100_050_shouldReturnLevel5Stub(self):
        self.setUpDict('5')
        self.assertEqual(sudoku._create(self.testDict), "This is level five")
        
    def test100_050_shouldDefaultToLevel3Stub(self):
        self.setUpDict("")
        self.assertEqual(sudoku._create(self.testDict), "This is level three")
        
#Sad Path
    def test100_910_ZeroShouldReturnInvalidError(self):
        self.setUpDict('0')
        self.assertEqual(sudoku._create(self.testDict), self.INVALIDLEVEL)
        
    def test100_920_StringShouldReturnInvalidError(self):
        self.setUpDict('foo')
        self.assertEqual(sudoku._create(self.testDict), self.INVALIDLEVEL)
