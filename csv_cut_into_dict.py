import csv

# nights_spent

# open file in read mode
with open('nights_spent.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = csv.DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # get only the data from greece into dictionary 1 and spain into  dictionarie 2
        if row["c_resid,unit,nace_r2,geo\\time"] == "TOTAL,NR,I551,EL":
            dict1 = row

        if row["c_resid,unit,nace_r2,geo\\time"] == "TOTAL,NR,I551,IS":
            dict2 = row

# Using dictionary comprehension + items()
# Extracting 2008-2011 keys from dictionary
dict1 = {key: dict1[key] for key in dict1.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
dict2 = {key: dict2[key] for key in dict2.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
# Add the name of each country
dict1['Country'] = 'Greece'
dict2['Country'] = 'Ispania'
# So far we have the number of Nights spent in greece and spain ,at tourist accommodation establishments for 4  years
read_obj.close()

##########################################################################################################################

# nights spent by non residents

# open file in read mode
with open('nights_spent_by_non_residents.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = csv.DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # get only the data from greece into dictionary 3 and spain into  dictionarie 4
        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551-I553,EL":
            dict3 = row

        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551-I553,IS":
            dict4 = row

# Using dictionary comprehension + items()
# Extracting 2008-2011 keys from dictionary
dict3 = {key: dict3[key] for key in dict3.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
dict4 = {key: dict4[key] for key in dict4.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
# Add the name of each country
dict3['Country'] = 'Greece'
dict4['Country'] = 'Ispania'
# So far we have the number of Nights spent by non residents in greece and spain ,at tourist accommodation establishments for 4  years
read_obj.close()
##########################################################################################################################################


# arrivals

# open file in read mode
with open('arrivals.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = csv.DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # get only the data from greece into dictionary 5 and spain into  dictionarie 6
        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551,EL":
            dict5 = row

        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551,IS":
            dict6 = row

# Using dictionary comprehension + items()
# Extracting 2008-2011 keys from dictionary
dict5 = {key: dict5[key] for key in dict5.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
dict6 = {key: dict6[key] for key in dict6.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
# Add the name of each country
dict5['Country'] = 'Greece'
dict6['Country'] = 'Ispania'
# So far we have the number of arrivals in greece and spain ,at tourist accommodation establishments for 4  years
read_obj.close()
##########################################################################################################################################

# arrivals by non residents

# open file in read mode
with open('arrivals_by_non_residents.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = csv.DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # get only the data from greece into dictionary 7 and spain into  dictionarie 8
        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551-I553,EL":
            dict7 = row

        if row["c_resid,unit,nace_r2,geo\\time"] == "FOR,NR,I551-I553,IS":
            dict8 = row

# Using dictionary comprehension + items()
# Extracting 2008-2011 keys from dictionary
dict7 = {key: dict7[key] for key in dict7.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
dict8 = {key: dict8[key] for key in dict8.keys()
         & {'2008 ', '2009 ', '2010 ', '2011 '}}
# Add the name of each country
dict7['Country'] = 'Greece'
dict8['Country'] = 'Ispania'
# So far we have the number of arrivals by non residents in greece and spain ,at tourist accommodation establishments for 4  years
read_obj.close()
###########################################################


