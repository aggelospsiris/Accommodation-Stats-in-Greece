import mysql.connector

#mysql connection with python
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#create database
mycursor.execute("CREATE DATABASE  accomodation_stats ")

