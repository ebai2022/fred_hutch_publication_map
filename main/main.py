from graph import Graph

"""
Main program for graph creation
"""

class Main:
    # Create an instance of the Graph class
    VIDD_module = Graph()

    # Specify the folder path containing the CSV files
    folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\VIDD_publication_set'

    # Specify the CSV file path
    csv_file_path = 'combined_group_matrix.csv'

    # initialize the name dictionary
    VIDD_module.load_names('names.txt', 'VIDD_primary_scientific_program.txt')

    # Call the method to read CSV files in the folder
    currData, pastData = VIDD_module.read_csv_files_in_folder(folder_path)

    # Create the matrices
    full_matrix = VIDD_module.construct_matrix('ALL')
    BBE_matrix = VIDD_module.construct_matrix('BBE')
    IVD_matrix = VIDD_module.construct_matrix('IVD')
    IDS_matrix = VIDD_module.construct_matrix('IDS')

    # Write matrix to a file
    VIDD_module.write_matrix_to_file(csv_file_path, full_matrix)
    VIDD_module.write_matrix_to_file('BBE_group_matrix.csv', BBE_matrix)
    VIDD_module.write_matrix_to_file('IVD_group_matrix.csv', IVD_matrix)
    VIDD_module.write_matrix_to_file('IDS_group_matrix.csv', IDS_matrix)

    # Write post 2020 data map to csv
    VIDD_module.write_dict_to_file('post_cuffoff_data.csv', currData)
    
    # Write pre 2020 data map to csv
    VIDD_module.write_dict_to_file('pre_cutoff_data.csv', pastData)