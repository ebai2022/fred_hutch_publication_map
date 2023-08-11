from graph import Graph

"""
Author: Ethan Bai
Test class
"""

class GraphTest:
    def __init__(self):
        self.VIDD_module = Graph()


    def small_matrix_test(self, filename):
        matrix = [
            [0, 1, 2, 1, 0, 2, 0, 2],
            [1, 0, 0, 2, 2, 2, 1, 1],
            [2, 0, 0, 1, 1, 2, 1, 1],
            [1, 2, 1, 0, 0, 1, 0, 2],
            [0, 2, 1, 0, 0, 1, 2, 2],
            [2, 2, 2, 1, 1, 0, 2, 1],
            [0, 1, 1, 0, 2, 2, 0, 0],
            [2, 1, 1, 2, 2, 1, 0, 0]
        ]
        # Specify the folder path containing the CSV files
        folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\test_files'
        # initialize the name dictionary
        self.VIDD_module.load_names(filename)
        # Call the method to read CSV files in the folder
        self.VIDD_module.read_csv_files_in_folder(folder_path)
        # Create the matrix
        adjMatrix = self.VIDD_module.construct_matrix()
        assert(len(matrix) == len(adjMatrix) and len(matrix[0]) == len(adjMatrix[0]))  
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j,matrix[i][j],adjMatrix[i][j])
                assert(matrix[i][j] == adjMatrix[i][j])


    def check_symmetry(self):
        
        # Specify the folder path containing the CSV files
        folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\VIDD_publication_set'

        # initialize the name dictionary
        self.VIDD_module.load_names('names.txt', 'VIDD_primary_scientific_program.txt')

        # Call the method to read CSV files in the folder
        currData, pastData = self.VIDD_module.read_csv_files_in_folder(folder_path)

        # Create the matrices
        full_matrix = self.VIDD_module.construct_matrix('ALL')
        BBE_matrix = self.VIDD_module.construct_matrix('BBE')
        IVD_matrix = self.VIDD_module.construct_matrix('IVD')
        IDS_matrix = self.VIDD_module.construct_matrix('IDS')

        # Check if symmetry holds
        self.isSymmetry(full_matrix)
        self.isSymmetry(BBE_matrix)
        self.isSymmetry(IVD_matrix)
        self.isSymmetry(IDS_matrix)

    def isSymmetry(self, matrix):
        size = len(matrix)
        transpose = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                transpose[i][j] = matrix[j][i]
        
        for i in range(size):
            for j in range(size):
                assert(matrix[i][j] == transpose[i][j])

g = GraphTest()
#g.small_matrix_test('test_names.txt')
g.check_symmetry()