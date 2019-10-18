from unittest import TestCase
import sudoku.create as sudoku 

class CreateTest(TestCase):
    
    
    def setUp(self):
        self.testDict = {}
        self.INVALIDLEVEL = {'status':'error: invalid level'}
        self.level1Grid = {
            'grid' : '[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]',
            'integrity' : '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
            'status' : "ok"
            }
        
        self.level2Grid = {
            'grid' : '[0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]',
            'integrity' : '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26',
            'status' : "ok"
            }
        
        self.level3Grid = {
            'grid' : '[0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0]',
            'integrity' : 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8',
            'status' : "ok"
            }
        
    def setUpDict(self, setLevel):
        self.testDict["level"] = setLevel




    #def test100_010_shouldReturnLevel1Stub(self):
    #    self.setUpDict('1')
    #    self.assertEqual(sudoku._create(self.testDict), "This is level one")

    #def test100_020_shouldReturnLevel2Stub(self):
    #    self.setUpDict('2')
    #    self.assertEqual(sudoku._create(self.testDict), "This is level two")

    #def test100_030_shouldReturnLevel3Stub(self):
    #    self.setUpDict('3')
    #    self.assertEqual(sudoku._create(self.testDict), "This is level three")
        
    def test100_040_shouldReturnLevel4Stub(self):
        self.setUpDict('4')
        self.assertEqual(sudoku._create(self.testDict), "This is level four")
        
    def test100_050_shouldReturnLevel5Stub(self):
        self.setUpDict('5')
        self.assertEqual(sudoku._create(self.testDict), "This is level five")
        
    def test100_050_shouldDefaultToLevel3Stub(self):
        self.setUpDict("")
        self.assertEqual(sudoku._create(self.testDict), "This is level three")
        
    def test100_050_shouldDefaultToLevel1Full(self):
        self.setUpDict('1')
        self.assertEqual(sudoku._create(self.testDict), self.level1Grid)
        
    def test100_050_shouldDefaultToLevel2Full(self):
        self.setUpDict('2')
        self.assertEqual(sudoku._create(self.testDict), self.level2Grid) 
        
    def test100_050_shouldDefaultToLevel3Full(self):
        self.setUpDict('3')
        self.assertEqual(sudoku._create(self.testDict), self.level2Grid)    
        
#Sad Path
    def test100_910_ZeroShouldReturnInvalidError(self):
        self.setUpDict('0')
        self.assertEqual(sudoku._create(self.testDict), self.INVALIDLEVEL)
        
    def test100_920_StringShouldReturnInvalidError(self):
        self.setUpDict('foo')
        self.assertEqual(sudoku._create(self.testDict), self.INVALIDLEVEL)
