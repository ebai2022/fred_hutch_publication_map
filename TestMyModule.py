from main import *

def test_matrix_small():
    module = Main()
    folder_path = r'C:\Users\Ethan\Documents\fred_hutch_project\dataset'
    csv_file_path = 'test_matrix_small.csv'
    VIDD_module.load_names('names.txt')
    VIDD_module.read_csv_files_in_folder(folder_path)
    matrix = VIDD_module.construct_matrix()
    VIDD_module.write_to_file(csv_file_path, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            assert(matrix[i][j] >= 0, 'non negative number')
            if i == j:
                assert(matrix[i][j] == 0)
            if matrix[i][j] >= 1:
                pass

