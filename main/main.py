from graph import Graph

"""
Main program for graph creation
"""

class Main:
    # Create an instance of the Graph class
    VIDD_module = Graph()

    # Specify the folder path containing the CSV files
    folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\dataset'

    # Specify the CSV file path
    csv_file_path = 'adj_matrix.csv'

    # initialize the name dictionary
    VIDD_module.load_names('names.txt')

    # Call the method to read CSV files in the folder
    currData, pastData = VIDD_module.read_csv_files_in_folder(folder_path)

    # Create the matrix
    matrix = VIDD_module.construct_matrix()

    # Write matrix to a file
    VIDD_module.write_matrix_to_file(csv_file_path, matrix)

    # Write post 2020 data map to csv
    VIDD_module.write_dict_to_file('post_cuffoff_data.csv', currData)
    
    # Write pre 2020 data map to csv
    VIDD_module.write_dict_to_file('pre_cutoff_data.csv', pastData)