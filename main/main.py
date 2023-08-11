from graph import Graph

"""
Author: Ethan Bai
Main program to run and operate graph creation


Notes:
140 VIDD members are listed in names.txt
Groups of the 140 VIDD members are listed in VIDD_primary_scientific_program
Publications from each person are in VIDD_publication_set


Future ideas:
Create flexible file pathing for both input and output (e.g. loading names/output matrices)
Add feature to construct matrices that combine different groups (e.g. IVD and IDS)
Build direct connection to Socnet software
Combine data sets of names and programs to read from 1 file instead of 2
Find a better way to test than on manually created data sets
Find a way to webscrape articles into CSV database
"""

class Main:
    # Create an instance of the Graph class
    VIDD_module = Graph()

    # Specify the folder path containing the CSV files
    folder_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\VIDD_publication_set'

    # Specify the CSV file path for different results
    full_matrix_file_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\combined_group_matrix.csv'
    BBE_matrix_file_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\BBE_group_matrix.csv'
    IVD_matrix_file_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\IVD_group_matrix.csv'
    IDS_matrix_file_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\IDS_group_matrix.csv'
    pre_2020_data_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\pre_cutoff_data.csv'
    post_2020_data_path = r'C:\Users\Ethan\Documents\fred_hutch_publication_map\main\output_files\post_cutoff_data.csv'

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
    VIDD_module.write_matrix_to_file(full_matrix, full_matrix_file_path)
    VIDD_module.write_matrix_to_file(BBE_matrix, BBE_matrix_file_path)
    VIDD_module.write_matrix_to_file(IVD_matrix, IVD_matrix_file_path)
    VIDD_module.write_matrix_to_file(IDS_matrix, IDS_matrix_file_path)

    # Write post 2020 data map to csv
    VIDD_module.write_dict_to_file(post_2020_data_path, currData)
    
    # Write pre 2020 data map to csv
    VIDD_module.write_dict_to_file(pre_2020_data_path, pastData)