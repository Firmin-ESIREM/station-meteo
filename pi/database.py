import sqlite3
import mysql.connector
from pathlib import Path
import platform
class Database():
	def __init__(self, sqlite=True, user="", password="", host="", port="", database=""):
		self.connection = None
		if sqlite:
			self.path = Path(__file__).parents[1] + "\\" if platform.system() == "Windows" else "/"
			self.connection = sqlite3.connect(self.path + "database")
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