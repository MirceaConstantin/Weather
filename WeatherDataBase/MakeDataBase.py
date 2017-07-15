# Multiple Table in 1 DataBase
# Multiple Inserts for each day and make them updating
# Connect file with creating and inserting data in DataBase with file who extract the DATA from XML
# Make a loop or decision for [create / insert / update] DataBase


import sqlite3
from sqlite3 import Error

def create_commectiom():

	try:
		# Create a DataBase
		conn = sqlite3.connect('Weather.sql')
		print (sqlite3.version)
	except Error as e:
		print(e)
	else:
		# Make a table in DataBase
		cursor = conn.cursor()
		cursor.execute("DROP TABLE IF EXISTS mondaySQL") and ("DROP TABLE IF EXISTS tusdaySQL")

		mondaySQL = """CREATE TABLE IF NOT EXISTS Monday (Temperature int(3), Humidity int(3), Data text, Day text,
								Sunrise text, Sunset text, Weather text, MaxTemperature int(3),
								MinTemperature int(3), WindDirection text, WindSpeed int(3))"""
		tusdaySQL = """CREATE TABLE IF NOT EXISTS Tusday (Temperature int(3), Humidity int(3), Data text, Day text,
								Sunrise text, Sunset text, Weather text, MaxTemperature int(3),
								MinTemperature int(3), WindDirection text, WindSpeed int(3))"""
		testSQL = """CREATE TABLE IF NOT EXISTS Test (Temperature int(3), Humidity int(3), Data text, Day text,
								Sunrise text, Sunset text, Weather text, MaxTemperature int(3),
								MinTemperature int(3), WindDirection text, WindSpeed int(3))"""

		cursor.execute((mondaySQL) and (tusdaySQL))
		# Insert data in Table
		try:
			cursor.execute (("INSERT INTO Monday VALUES (24 , 95 , '03.07.2017', '02.07.2017', '06:35:25', '20:30:45', 'Raining', 26, 16, 'South', 55)") and
							("INSERT INTO Tusday VALUES (24 , 95 , '03.07.2017', '02.07.2017', '06:35:25', '20:30:45', 'Raining', 26, 16, 'South', 55)"))
			print ("Inserted data... ")
			conn.commit()
			print ("Succes!")
		except Error as e:
			print (e)
		else:
			conn.rollback()
			print ("Retry...")
	finally:
		#close Connection
		conn.close()
	#return
create_commectiom()