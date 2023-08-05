from graph import Graph

"""
Test class
Todo:
Write CSV file that has a dictionary of all publications 2020 and beyond
Write CSV file that has a dictionary of all publications 2019 and beyond
Create a smaller test set to verify and test code
"""

class GraphTest:

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
        # Create an instance of the Graph class
        VIDD_module = Graph()
        # Specify the folder path containing the CSV files
        folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\test_files'
        # initialize the name dictionary
        VIDD_module.load_names(filename)
        # Call the method to read CSV files in the folder
        VIDD_module.read_csv_files_in_folder(folder_path)
        # Create the matrix
        adjMatrix = VIDD_module.construct_matrix()
        assert(len(matrix) == len(adjMatrix) and len(matrix[0]) == len(adjMatrix[0]))  
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j,matrix[i][j],adjMatrix[i][j])
                assert(matrix[i][j] == adjMatrix[i][j])

g = GraphTest()
g.small_matrix_test('test_names.txt')
    # Specify the CSV file path
    #csv_file_path = 'test_matrix.csv'

    #write to the file
    #VIDD_module.write_matrix_to_file(csv_file_path, matrix)