import re
import csv
import os
#from fuzzywuzzy import fuzz

"""
Author: Ethan Bai
Main graph functionalities:
Reads CSV files, trims their data, and creates an adjacency matrix of an undirected graph
"""

class Graph:
    def __init__(self):
        self.VIDD_AUTHORS = {} # tracks the entire set of VIDD authors
        self.IVD_AUTHORS = {} # tracks the set of IVD authors
        self.BBE_AUTHORS = {} # tracks the set of BBE authors
        self.IDS_AUTHORS = {} # tracks the set of IDS authors

        # tracks index to author to generate lists
        self.VIDD_indices = {}
        self.IVD_indices = {}
        self.BBE_indices = {}
        self.IDS_indices = {}

        self.database = {} # tracks post 2020 PMID -> author list
        self.DATECUTOFF = 2020 # requested cutoff date is 2020
        self.preCutoffPapers = {} # tracks pre 2020 PMID -> author list
        #self.fuzzedDatabase = {}

    # reads a folder of csv files
    def read_csv_files_in_folder(self, folder_path):
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
        for csv_file in csv_files:
            csv_file_path = os.path.join(folder_path, csv_file)
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                # skip the first line
                next(csv_reader)
                for row in csv_reader:
                    if row[0] not in self.database:
                        names = row[2].strip().split(',')
                        year = row[6]
                        if int(year) >= self.DATECUTOFF:
                            self.database[row[0]] = set()
                            for name in names:
                                longerName = name.strip().upper()
                                # name comparison to avoid losing people with middle initials
                                for author in self.VIDD_AUTHORS:
                                    if author in longerName:
                                        # converts all names into last_name first_initial format
                                        self.database[row[0]].add(author)
                            # removes papers that don't have any VIDD authors
                            if len(self.database[row[0]]) == 0:
                                del self.database[row[0]]

                        # additional sectioning of pre 2020 papers
                        else:
                            self.preCutoffPapers[row[0]] = set()
                            for name in names:
                                longerName = name.strip().upper()
                                for author in self.VIDD_AUTHORS:
                                    if author in longerName:
                                        self.preCutoffPapers[row[0]].add(author)
                            if len(self.preCutoffPapers[row[0]]) == 0:
                                del self.preCutoffPapers[row[0]]
        return self.database, self.preCutoffPapers

    # Write the matrix to a CSV file
    def write_matrix_to_file(self, matrix, path, filename):
        file_path = f"{path}/{filename}.csv"
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in matrix:
                csv_writer.writerow(row)
            
    # Write the dictionary to a CSV file
    def write_dict_to_file(self, data, path, filename):
        file_path = f"{path}/{filename}.csv"
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for key, values in data.items():
                row = [key] + list(values)
                csv_writer.writerow(row)
            csv_file.close()
    
    # reads the name file into a dictionary of name -> index
    def load_names(self, path, namefile, groupfile):
        namefile_path = f"{path}/{namefile}.txt"
        groupfile_path = f"{path}/{groupfile}.txt"
        names_list = []
        with open(namefile_path, "r") as file:
            names_list = file.readlines()
        with open(groupfile_path, "r") as file:
            group_list = file.readlines()
        # array with index 0->BBE, index 1->IVD, and index 2->IDS
        count = {"BBE": 0, "IVD": 0, "IDS": 0}
        for i in range(len(names_list)):
            group = group_list[i].strip()
            name_parts = names_list[i].strip().split()
            name = name_parts[0] + ' ' + name_parts[1][0]
            self.VIDD_AUTHORS[name] = i
            self.VIDD_indices[i] = name
            if group in "BBEIVDIDS":
                # group map update
                group_attr = f"{group}_AUTHORS"
                group_name = f"{group}"
                group_authors = getattr(self, group_attr)
                group_authors[name] = count[group_name]
                # creating reverse map
                index_attr = f"{group}_indices"
                index_authors = getattr(self, index_attr)
                index_authors[count[group_name]] = name
                
                count[group_name] += 1


    # Write a legend of index in matrix -> author name
    def create_legend(self, group, path, filename):
        file_path = f"{path}/{filename}.txt"
        group_attr = f"{group}_indices"
        legend = getattr(self, group_attr)
        with open(file_path, 'w', newline='') as file:
            for i in range(len(legend)):
                file.write(legend[i] + "\n")
        

    # constructs the adjacency matrix from a given group
    def construct_matrix(self, group):
        group_attr = f"{group}_AUTHORS"
        author_list = getattr(self, group_attr)
        size = len(author_list) + 1
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for pub in self.database:
            curr = list(self.database[pub])
            # Avoids duplication
            for i in range(len(curr)):
                for j in range(i+1, len(curr)):
                    # limit to only the authors in the specificed group
                    if curr[i] in author_list and curr[j] in author_list:
                        x = author_list[curr[i]]
                        y = author_list[curr[j]]
                        matrix[x][y] += 1
                        matrix[y][x] += 1
        return matrix