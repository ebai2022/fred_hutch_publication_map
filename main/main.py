from graph import Graph
import os
"""
Author: Ethan Bai
Main program to run and operate graph creation

Todo:
Create relative file tracking (use current file path and then route)
Once all name files are generated into a CSV, use those as the base txt files and use variables instead of storing so much data

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
    absolute_path = os.path.dirname(__file__)

    # RELATIVE PATHS (EDIT AS NEED BE):
    VIDD_pubset = "VIDD_publication_set"
    output_path = "output_files"
    input_path = "input_files"
    csv_folder_path = os.path.join(absolute_path, VIDD_pubset)
    output_folder_path = os.path.join(absolute_path, output_path)
    input_folder_path = os.path.join(absolute_path, input_path)

    # initialize the name dictionary
    VIDD_module.load_names(input_folder_path, "names", "VIDD_primary_scientific_program")

    # Call the method to read CSV files in the folder
    currData, pastData = VIDD_module.read_csv_files_in_folder(csv_folder_path)

    # Create the matrices
    full_matrix = VIDD_module.construct_matrix('ALL')
    BBE_matrix = VIDD_module.construct_matrix('BBE')
    IVD_matrix = VIDD_module.construct_matrix('IVD')
    IDS_matrix = VIDD_module.construct_matrix('IDS')

    # Write matrix to a file
    VIDD_module.write_matrix_to_file(full_matrix, output_folder_path, "combined_group_matrix")
    VIDD_module.write_matrix_to_file(BBE_matrix, output_folder_path, "BBE_group_matrix")
    VIDD_module.write_matrix_to_file(IVD_matrix, output_folder_path, "IVD_group_matrix")
    VIDD_module.write_matrix_to_file(IDS_matrix, output_folder_path, "IDS_group_matrix")

    # Write post 2020 data map to csv
    VIDD_module.write_dict_to_file(currData, output_folder_path, "post_cutoff_data")
    
    # Write pre 2020 data map to csv
    VIDD_module.write_dict_to_file(pastData, output_folder_path, "post_cutoff_data")