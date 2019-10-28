from unittest import TestCase
import sudoku.insert as sudoku 

class InsertTest(TestCase):
    
    def setUp(self):
        self.error1 = {'status':'error: invalid cell reference'}
        self.testDict = {}
        self.INVALIDLEVEL = {'status':'error: invalid level'}
        self.test1Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 3, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': '96484cb0a36217f3a7500c50b5b7d3b6012b336be9a1cae83abab27e48c7a627',
                          'status': 'ok'}

        self.test2Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
                          'status': 'ok'}

        self.test3Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 4, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': 'efef1d144fedbb92020b1f8ce9a830735ee9ba88bc271e71cc0f0896e06fce0a',
                          'status': 'warning'}   
        
        self.test4Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
                          'status': 'ok'} 
            
    def setUpDict(self, setCell, setValue, setGrid, setIntegrity):
        self.testDict["cell"] = setCell
        if setValue != 'null':
            self.testDict["value"] = setValue
        self.testDict["grid"] = setGrid
        self.testDict["integrity"] = setIntegrity
        
    def gridsToCall(self, gridNumber):
        if (gridNumber == '1'):
            return '[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'
        if (gridNumber == '2'):
            return '[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 3, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]'
        
        
    def test100_010_shouldInsertValueIntoNomialSpace(self):
        self.maxDiff = None
        self.setUpDict('r3c1', '3', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.test1Grid)
        
    def test100_020_shouldRemoveValueFromNomialSpace(self):
        self.maxDiff = None
        self.setUpDict('r3c1', 'null', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.test2Grid)
        
    def test100_030_shouldRemoveValueFromNomialSpace(self):
        self.maxDiff = None
        self.setUpDict('r3c1', '4', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.test3Grid)
        
    def test900_030_shouldReturnCellError(self):
        self.maxDiff = None
        self.setUpDict('r3c0', '3', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.error1)