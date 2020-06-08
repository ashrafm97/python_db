import pyodbc


# connecting_to_python = pyodbc.connect('driver= {OBDC driver for SQL}; Server = databases2.spartaglobal.academy;')

server = "databases2.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"


connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print(connection)


