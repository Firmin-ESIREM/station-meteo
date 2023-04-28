import sqlite3
import mysql.connector
from os import path
from pathlib import Path

class Database():
	def __init__(self, sqlite=True, user="", password="", host="", port="", database=""):
		self.connection = None
		if sqlite:
			self.path = path.join(Path(__file__).parents[1], "database.db")
			self.connection = sqlite3.connect(self.path)
		else:
			self.user = user
			self.password = password
			self.host = host
			self.port = port
			self.database = database
			self.connection = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
		self.__create_tables__()

	
	def __create_tables__(self):
		cursor = self.connection.cursor()
		cursor.execute("")
		self.connection.commit()
		cursor.close()