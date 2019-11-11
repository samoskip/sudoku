from unittest import TestCase
import sudoku.solve as sudoku 

class SolveTest(TestCase):


    def setUp(self):
        self.INVALIDCHAR = {'status': 'error: invalid character in grid'}
        self.INVALIDLENGTH = {'status': 'error: invalid board length'}
        self.INVALIDSOLUTION = {'status': 'error: board not solvable'}
        self.INTEGRITYERROR = {'status':'error: integrity mismatch'}
        self.testDict = {}
        self.INVALIDLEVEL = {'status':'error: invalid level'}
        self.test1Grid = {'status': 'ok'}

        self.test2Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
                          'status': 'ok'}

        self.test3Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 4, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': 'efef1d144fedbb92020b1f8ce9a830735ee9ba88bc271e71cc0f0896e06fce0a',
                          'status': 'warning'}   
        
        self.test4Grid = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                          'integrity': '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
                          'status': 'ok'} 
            
    def setUpDict(self, setGrid, setIntegrity):
        self.testDict["grid"] = setGrid
        self.testDict["integrity"] = setIntegrity
        
    def gridsToCall(self, gridNumber):
        if (gridNumber == '1'):
            return '[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'
        if (gridNumber == '2'):
            return '[a,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'


    # 100 create
    #    Desired level of confidence:    correct output on finite inputs
    #    Input-output Analysis
    #        inputs:       string
    #        outputs:       dictionary
    #    Happy path analysis:
    #                nominal cell        n=3
    #                remove cell         n=5
    #                warning cell        n=1
    #        output:
    #                The output is the appropriate input from user to modify grid
    #
    #    Sad path analysis:
    #                missing cell
    #                invalid cell
    #                invalid modify
    #                invalid grid
    #                integrity mismatch
    
    #Happy Path    
    def test100_010_shouldInsertValueIntoNomialSpace(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._solve(self.testDict), self.test1Grid)
        
    '''   
    def test100_020_shouldRemoveValueFromNomialSpace(self):
        self.maxDiff = None
        self.setUpDict('r3c1', 'null', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.test2Grid)
        
    def test100_030_shouldRemoveValueFromNomialSpace(self):
        self.maxDiff = None
        self.setUpDict('r3c1', '4', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.test3Grid)
    
    #Sad path    
    def test900_010_shouldReturnCellError(self):
        self.maxDiff = None
        self.setUpDict('r3c0', '3', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.errorInvalidCell)
        
    def test900_020_shouldReturnMissingCellError(self):
        self.maxDiff = None
        self.setUpDict('null', '3', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.errorMissingCell)
        
    def test900_030_shouldReturnFixedHintError(self):
        self.maxDiff = None
        self.setUpDict('r1c1', '3', self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.errorHint)
        
    def test900_040_shouldReturnInvalidGridError(self):
        self.maxDiff = None
        self.setUpDict('r3c1', '3', self.gridsToCall('2'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._insert(self.testDict), self.errorGrid)
        
    def test900_040_shouldReturnIntegrityMismatchError(self):
        self.maxDiff = None
        self.setUpDict('r3c1', '3', self.gridsToCall('1'), '0000000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(sudoku._insert(self.testDict), self.errorIntegrity)
    '''