from unittest import TestCase
import sudoku.solve as sudoku 

class SolveTest(TestCase):


    def setUp(self):
        self.SOLVED = {'status':'solved'}
        self.INCOMPLETE = {'status':'incomplete'}
        self.WARNING = {'status':'warning'}
        self.INVALIDLENGTH = {'status': 'error: invalid board length'}
        self.NOTSOLVABLE = {'status':'error: grid not solvable'}
        self.INTEGRITYERROR = {'status':'error: integrity mismatch'}
        self.INVALIDGRID = {'status':'error: invalid character in grid'}
        
        
        self.testDict = {}
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
        
        self.test5Grid = {'grid': [4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 3, 6],
                          'integrity': 'e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6',
                          'status':'ok'}
            
    def setUpDict(self, setGrid, setIntegrity):
        self.testDict["grid"] = setGrid
        self.testDict["integrity"] = setIntegrity
        
    def gridsToCall(self, gridNumber):
        if (gridNumber == '1'):
            return '[a,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'
        if (gridNumber == '2'):
            return '[-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'
        if (gridNumber == '3'):
            return '[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]'
        if (gridNumber == '4'):
            return '[-8,-1,-5,-7,-6,-9,-3,-2,8,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]'
        if (gridNumber == '5'):
            return '[0,-5,-8,-9,0,-1,-6,0,0,-2,0,0,-5,-8,0,0,-4,-1,-9,0,0,0,0,0,0,-5,0,-3,0,-6,-1,-5,0,0,-2,0,-1,-4,0,0,-2,0,-7,0,-9,0,0,0,0,-6,0,-5,0,0,0,-1,-3,-2,0,0,-4,-8,-7,0,0,-4,0,0,-3,0,0,0,-5,0,0,-8,-1,0,-2,0,0]'
    # 100 create
    #    Desired level of confidence:    correct output on finite inputs
    #    Input-output Analysis
    #        inputs:       string
    #        outputs:       dictionary
    #    Happy path analysis:
    #                answers a solvable grid
    #        output:
    #                The output is from backtracking algorithm within the rules of sudoku
    #
    #    Sad path analysis:
    #                not solvable
    #                invalid length
    #                invalid grid
    #                integrity mismatch
    
    
    
    #Happy Path
    def test100_010_invalidGirdInput(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('5'), '6594d6506dc349fdbd9e5dda58acfa8d563657b0ef8bfc3a24ea53df9c988f9b')
        self.assertEqual(sudoku._solve(self.testDict), self.test5Grid)    
    
    
    
    
    #Sad Path    
    def test900_010_invalidGirdInput(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('1'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._solve(self.testDict), self.INVALIDGRID)
        
    def test900_020_invalidLength(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('2'), '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        self.assertEqual(sudoku._solve(self.testDict), self.INVALIDLENGTH)
        
    def test900_030_integrityMismatched(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('3'), '000000000')
        self.assertEqual(sudoku._solve(self.testDict), self.INTEGRITYERROR)
        
    def test900_040_gridNotSolavable(self):
        self.maxDiff = None
        self.setUpDict(self.gridsToCall('4'), 'fb798a9148fd1854800420123530ec8a2f2ef00731d386b26eb69cb4bf9b8ffc')
        self.assertEqual(sudoku._solve(self.testDict), self.NOTSOLVABLE)
