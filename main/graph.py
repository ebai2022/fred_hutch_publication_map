import re
import csv
import os
#from fuzzywuzzy import fuzz

"""
Todo:
Write CSV file that has a dictionary of all publications 2020 and beyond
Write CSV file that has a dictionary of all publications 2019 and beyond
Create a smaller test set to verify and test code
"""

class Graph:
    def __init__(self):
        self.VIDD_AUTHORS = {}
        self.database = {}
        self.DATECUTOFF = 2020
        self.preCutoffPapers = {}
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
                        print(row[0], names, year)
                        #print(self.VIDD_AUTHORS)
                        if int(year) >= self.DATECUTOFF:
                            #pubCount += 1
                            for name in names:
                                longerName = name.strip().upper()
                                for author in self.VIDD_AUTHORS:
                                    #print(author, longerName, author in longerName)
                                    if author in longerName:
                                        self.database[row[0]].add(author)
                            if len(self.database[row[0]]) == 0:
                                del self.database[row[0]]
                        else:
                            for name in names:
                                longerName = name.strip().upper()
                                for author in self.VIDD_AUTHORS:
                                    if author in longerName:
                                        self.database[row[0]].add(author)
                            if len(self.database[row[0]]) == 0:
                                del self.database[row[0]]
        #print(pubCount, totalCount)
        #print(self.database)

    # Write the matrix to a CSV file
    def write_matrix_to_file(self, csv_file_path, matrix):
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in matrix:
                csv_writer.writerow(row)

    def write_dict_to_file(self, csv_file_path):
        pass
    
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