# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:54:40 2018

@author: Rozan
"""
#loc = 'C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron1/ham'
import os
import csv

dirpath = 'C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron1/ham'
output = 'output_file.csv'
with open(output, 'w', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['Kelas', 'Email'])

    files = os.listdir(dirpath)

    for filename in files:
        with open(dirpath + '/' + filename) as afile:
            csvout.writerow(['ham', afile.read()])
            afile.close()

    outfile.close()
    
    