##import sqlite3
##
##con = sqlite3.connect('employees.db')
###con = sqlite3.connect('timeEntry.db')
###con = sqlite3.connect('paychecks.db')
###con = sqlite3.connect('manager.db')
##
###con = sqlite3.connect('loginAuth.db')
##
##print("Database opened successfully")
##
##con.execute("create table IF NOT EXISTS employees (employee_id INTEGER PRIMARY KEY, lname CHAR(20), \
##fname CHAR(20), ssn INTEGER, email EMAIL, \
##address CHAR(100), dep_name CHAR(20))")
##
##print("Employee Table created successfully")
##
##con.execute("create table IF NOT EXISTS loginAuth (employee_id INTEGER PRIMARY KEY, HashPwd CHAR(20))")
##
##print("LoginAuth Table created successfully")
##
##
##
##con.close()
