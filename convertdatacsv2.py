# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 02:18:06 2018

@author: Rozan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:54:40 2018

@author: Rozan
"""
#loc = 'C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron6/ham'
import os
import csv

dirpath = 'C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron6/ham'
output = 'enron6.csv'
with open(output, 'w', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['Kelas', 'Email'])

    files = os.listdir(dirpath)

    for filename in files:
        with open(dirpath + '/' + filename) as afile:
            csvout.writerow(['ham', afile.read()])
            afile.close()
    
    files = os.listdir('C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron6/spam')
    
    for filename in files:
        with open('C:/Users/Rozan/Documents/Tugas Akhir Project/enror spam/enron6/spam' + '/' + filename, errors='ignore') as afile:
            csvout.writerow(['spam', afile.read()])
            afile.close()
    
    outfile.close()
    
    