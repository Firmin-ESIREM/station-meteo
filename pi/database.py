import sqlite3
import mysql.connector
from os import path
from pathlib import Path


class Database:
	def __init__(self, sqlite=True, user="", password="", host="", port="", database=""):
		self.connection = None
		self.datas = ["temperature", "humidity", "air_quality", "pressure", "datetime"]  # [] { }
		if sqlite:
			self.path = path.join(Path(__file__).parents[1], "database.db")
			self.connection = sqlite3.connect(self.path, check_same_thread=False)
		else:
			self.user = user
			self.password = password
			self.host = host
			self.port = port
			self.database = database
			self.connection = mysql.connector.connect(user=user, password=password, host=host, port=port,
													  database=database)
		self.__create_tables__()

	def __create_tables__(self):
		cursor = self.connection.cursor()
		cursor.execute(
			"CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature FLOAT, humidity FLOAT, air_quality INTEGER, pressure FLOAT, datetime DATETIME DEFAULT CURRENT_TIMESTAMP)")
		self.connection.commit()
		cursor.close()

	def add_data(self, dictionary):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO data (temperature, humidity, air_quality, pressure) VALUES (?, ?, ?, ?)", (
			dictionary["temperature"], dictionary["humidity"], dictionary["air_quality"], dictionary["pressure"]))
		self.connection.commit()
		cursor.close()

	def get_all_datas(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM data")
		values = cursor.fetchall()
		cursor.close()
		# TODO vérifier comment sort les données dans values
		return {data: value for data, value in zip(self.datas, values)}

	def get_last_data(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
		values = cursor.fetchone()
		cursor.close()
		if values is None:
			return {data: None for data in self.datas} 
		return {data: value for data, value in zip(self.datas, values)}