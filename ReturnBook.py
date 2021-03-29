# Importing the necessary modules
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc

# Connecting to the Sql server
server = 'DESKTOP-CHINWEU' 
database = 'LibraryManagementSystem' 
# username = 'myusername' 
# password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=server;DATABASE=database;Trusted_Connection=yes;')
cursor = cnxn.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books" #Book Table

allBid = []  #To store all the Book ID’s