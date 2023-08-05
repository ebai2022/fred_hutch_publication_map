import re
import csv
import os
#from fuzzywuzzy import fuzz

"""
Todo:
Write CSV file that has a dictionary of all publications 2020 and beyond
Write CSV file that has a dictionary of all publications 2019 and beyond
Create a smaller test set to verify and test code
Testing commits
"""


class Main:
    def __init__(self):
        self.VIDD_AUTHORS = {}
        self.database = {}
        self.DATECUTOFF = 2020
        self.preCutoffPapers = {}
        #self.namefile = namefile # names of the employees of VIDD in "last_name first_initial" format
        #self.publicationfile = publicationfile # names under publication in "last_name first_initial" separated by commas
        #self.publicationNum = publicationNum # publication number associated with each paper (line matching)
        #self.fuzzedDatabase = {}

    # reads a folder of csv files
    def read_csv_files_in_folder(self, folder_path):
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
        pubCount = 0
        totalCount = 0
        for csv_file in csv_files:
            csv_file_path = os.path.join(folder_path, csv_file)
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                #print(f"Reading contents of {csv_file}:")
                for row in csv_reader:
                    if row[0] not in self.database:
                        #totalCount += 1
                        self.database[row[0]] = set()
                        names = row[2].strip().split(',')
                        year = row[6]
                        if int(year) >= self.DATECUTOFF:
                            #pubCount += 1
                            for name in names:
                                author = name.strip().upper()
                                for name in self.VIDD_AUTHORS:
                                    if name in author:
                                        self.database[row[0]].add(name)
                            if len(self.database[row[0]]) == 0:
                                del self.database[row[0]]
                        else:
                            for name in names:
                                author = name.strip().upper()
                                for name in self.VIDD_AUTHORS:
                                    if name in author:
                                        self.database[row[0]].add(name)
                            if len(self.database[row[0]]) == 0:
                                del self.database[row[0]]
        #print(pubCount, totalCount)
        #print(self.database)

    # Write the matrix to a CSV file
    def write_to_file(self, csv_file_path, matrix):
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in matrix:
                csv_writer.writerow(row)
    
    # reads the name file into a dictionary of name -> index
    def load_names(self, namefile):
        names_list = []
        with open(namefile, "r") as file:
            names_list = file.readlines()
        # Remove newline characters and whitespace from each name
        ret_names = {}
        for i in range(len(names_list)):
            name_parts = names_list[i].strip().split()
            name = name_parts[0] + ' ' + name_parts[1][0]
            self.VIDD_AUTHORS[name] = i
        
    # constructs the adjacency matrix
    def construct_matrix(self):
        size = len(self.VIDD_AUTHORS)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for pub in self.database:
            curr = list(self.database[pub])
            # jank stuff to not duplicate cause stupid sets
            for i in range(len(curr)):
                for j in range(i+1, len(curr)):
                    x = self.VIDD_AUTHORS[curr[i]]
                    y = self.VIDD_AUTHORS[curr[j]]
                    matrix[x][y] += 1
                    matrix[y][x] += 1
        return matrix
    
    """
    # reads the publication file into a format publication_id (currently using 0-whatever) -> names (set)
    def read_publications(self, nameList):
        with open(self.publicationfile, 'r', encoding='utf-8') as file:
            content = file.readlines()

        publication_entries = {}
        publication_id = 0  # Change this if you have a specific way of identifying publications

        for line in content:
            publication_entries[publication_id] = set()
            authors = line.strip().split(',')
            for author in authors:
                curr = author.strip().upper()
                for name in nameList:
                    if name in curr:
                        publication_entries[publication_id].add(name)
            publication_id += 1
        return publication_entries
        """

# Create an instance of the Main class
VIDD_module = Main()

# Specify the folder path containing the CSV files
folder_path = r'C:\Users\Ethan\Documents\fred_hutch_project\fred_hutch_publication_map\dataset'

# Specify the CSV file path
csv_file_path = 'adj_matrix.csv'

# initialize the name dictionary
VIDD_module.load_names('names.txt')

# Call the method to read CSV files in the folder
VIDD_module.read_csv_files_in_folder(folder_path)

# Create the matrix
matrix = VIDD_module.construct_matrix()

#write to the file
VIDD_module.write_to_file(csv_file_path, matrix)



# Call the read_names method to get the list of names
#names_list = VIDD_module.read_names()
#publications_list = name_reader.read_publications(names_list)
#matrix = name_reader.construct_matrix(names_list, publications_list)

# Print the list of names
#print(names_list)
#print(publications_list)
#print(matrix)