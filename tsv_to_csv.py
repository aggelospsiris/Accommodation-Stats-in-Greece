#code for converting tsv to csv

import pandas as pd

#Nights spent at tourist accommodation establishments
tsv_file= '../tsv/tin00177.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('nights_spent.csv',index=False)

#Nights spent by non-residents at tourist accommodation establishments
tsv_file= '../tsv/tin00175.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('nights_spent_by_non_residents.csv',index=False)

#Arrivals at tourist accommodation establishments
tsv_file= '../tsv/tour_occ_arnat.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('arrivals.csv',index=False)

#Arrivals of non-residents at tourist accommodation establishments
tsv_file= '../tsv/tin00174.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('arrivals_by_non_residents.csv',index=False)