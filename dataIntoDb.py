import mysql.connector
from codes.csv_cut_into_dict import dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8


try:
    connection= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="accomodation_stats" )

    ####################################################################################################################
    # create table nights spent
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE nights_spent (country VARCHAR(20),dates YEAR(4) ,number_of_nights INT )")\

    #insert values from dictionaries to sql table
    insert_query = "INSERT INTO nights_spent (country,dates,number_of_nights) VALUES (%s,%s,%s)"

    val = (dict1.get('Country'),2008,dict1.get('2008 '))
    mycursor.execute(insert_query,val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict1.get('Country'), 2009, dict1.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict1.get('Country'), 2010, dict1.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict1.get('Country'), 2011, dict1.get('2011 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict2.get('Country'), 2008, dict2.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict2.get('Country'), 2009, dict2.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict2.get('Country'), 2010, dict2.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    val = (dict2.get('Country'), 2011, dict2.get('2011 '))
    mycursor.execute(insert_query, val)
    connection.commit()
    print(mycursor.rowcount, "Record inserted successfully into nights_spent table")
    mycursor.close()

    ####################################################################################################################
    # create table nights spent by non_residents
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE nights_spent_by_non_residents (country VARCHAR(20),dates YEAR(4) ,number_of_nights INT )")\

    #insert values from dictionaries to sql table
    insert_query = "INSERT INTO nights_spent_by_non_residents (country,dates,number_of_nights) VALUES (%s,%s,%s)"

    val = (dict3.get('Country'),2008,dict3.get('2008 '))
    mycursor.execute(insert_query,val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict3.get('Country'), 2009, dict3.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict3.get('Country'), 2010, dict3.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict3.get('Country'), 2011, dict3.get('2011 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict4.get('Country'), 2008, dict4.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict4.get('Country'), 2009, dict4.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict4.get('Country'), 2010, dict4.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    val = (dict4.get('Country'), 2011, dict4.get('2011 '))
    mycursor.execute(insert_query, val)
    connection.commit()
    print(mycursor.rowcount, "Record inserted successfully into nights_spent_by_non_residents table")
    mycursor.close()

    ####################################################################################################################
    # create table arrivals
    mycursor = connection.cursor()

    mycursor.execute(
        "CREATE TABLE arrivals (country VARCHAR(20),dates YEAR(4) ,arrivals INT )") \
 \
        # insert values from dictionaries to sql table
    insert_query = "INSERT INTO arrivals (country,dates,arrivals) VALUES (%s,%s,%s)"

    val = (dict5.get('Country'), 2008, dict5.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict5.get('Country'), 2009, dict5.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict5.get('Country'), 2010, dict5.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict5.get('Country'), 2011, dict5.get('2011 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict6.get('Country'), 2008, dict6.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict6.get('Country'), 2009, dict6.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict6.get('Country'), 2010, dict6.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    val = (dict6.get('Country'), 2011, dict6.get('2011 '))
    mycursor.execute(insert_query, val)
    connection.commit()
    print(mycursor.rowcount, "Record inserted successfully into arrivals table")
    mycursor.close()

    ####################################################################################################################
    # create table arrivals_by_non_residents
    mycursor = connection.cursor()

    mycursor.execute(
        "CREATE TABLE arrivals_by_non_residents (country VARCHAR(20),dates YEAR(4) ,arrivals INT )") \
 \
        # insert values from dictionaries to sql table
    insert_query = "INSERT INTO arrivals_by_non_residents (country,dates,arrivals) VALUES (%s,%s,%s)"

    val = (dict7.get('Country'), 2008, dict7.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict7.get('Country'), 2009, dict7.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict7.get('Country'), 2010, dict7.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict7.get('Country'), 2011, dict7.get('2011 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict8.get('Country'), 2008, dict8.get('2008 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict8.get('Country'), 2009, dict8.get('2009 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict8.get('Country'), 2010, dict8.get('2010 '))
    mycursor.execute(insert_query, val)
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    val = (dict8.get('Country'), 2011, dict8.get('2011 '))
    mycursor.execute(insert_query, val)
    connection.commit()
    print(mycursor.rowcount, "Record inserted successfully into arrivals_by_non_residents table")
    mycursor.close()


#insert failed
except mysql.connector.Error as error:
    print("Failed to insert record into  table {}".format(error))
#close connection
finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")