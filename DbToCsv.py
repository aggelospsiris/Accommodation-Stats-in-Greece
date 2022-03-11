import mysql.connector
import pandas as pd

########################################################################################################################
#nights_spent

#open the scv file in write mode
with open('nights_spent_final.csv', 'w') as csvfile:
    #connect to the database
    try:
        database = mysql.connector.connect(host="localhost", user="root", passwd="", database="accomodation_stats")
    except:
        print('Database connection failed!')

    # Get the cursor, which is used to traverse the database, line by line
    mycursor = database.cursor()

    mycursor.execute("SELECT * FROM nights_spent")
    select_result = mycursor.fetchall()

    #write the rows from tha database to csv using pandas dataframe
    df = pd.DataFrame(select_result)
    df.to_csv('nights_spent_final.csv', header=["Country", "Year", "Nights spent at tourist accommodation establishments"], index=False)
    mycursor.close()
    #close the csv file
csvfile.close


########################################################################################################################
#nights_spent_by_non_residents

#open the scv file in write mode
with open('nights_spent_by_non_residents_final.csv', 'w') as csvfile:
    #connect to the database
    try:
        database = mysql.connector.connect(host="localhost", user="root", passwd="", database="accomodation_stats")
    except:
        print('Database connection failed!')

    # Get the cursor, which is used to traverse the database, line by line
    mycursor = database.cursor()

    mycursor.execute("SELECT * FROM nights_spent_by_non_residents")
    select_result = mycursor.fetchall()

    #write the rows from tha database to csv using pandas dataframe
    df = pd.DataFrame(select_result)
    df.to_csv('nights_spent_by_non_residents_final.csv', header=["Country", "Year", "Nights spent at tourist accommodation establishments by non residents"], index=False)
    mycursor.close()
    #close the csv file
csvfile.close

########################################################################################################################
# arrivals

# open the scv file in write mode
with open('arrivals_final.csv', 'w') as csvfile:
        # connect to the database
        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="accomodation_stats")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        mycursor.execute("SELECT * FROM arrivals")
        select_result = mycursor.fetchall()

        # write the rows from tha database to csv using pandas dataframe
        df = pd.DataFrame(select_result)
        df.to_csv('arrivals_final.csv',
                  header=["Country", "Year", "Arrivals at tourist accommodation establishments"],
                  index=False)
        mycursor.close()
        # close the csv file
csvfile.close


########################################################################################################################
# arrivals by non residents

# open the scv file in write mode
with open('arrivals_by_non_residents_final.csv', 'w') as csvfile:
        # connect to the database
        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="", database="accomodation_stats")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        mycursor.execute("SELECT * FROM arrivals_by_non_residents")
        select_result = mycursor.fetchall()

        # write the rows from tha database to csv using pandas dataframe
        df = pd.DataFrame(select_result)
        df.to_csv('arrivals_by_non_residents_final.csv',
                  header=["Country", "Year", "Arrivals at tourist accommodation establishments by non residents"],
                  index=False)
        mycursor.close()
# close the csv file
csvfile.close