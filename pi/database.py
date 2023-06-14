import sqlite3
import mysql.connector
from os import path
from datetime import datetime
from pathlib import Path


class Database:
	def __init__(self, sqlite=True, user="", password="", host="", port="", database=""):
		self.connection = None
		self.datas = ["id","temperature", "humidity", "air_quality", "pressure", "datetime"]  # [] { }
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
			"CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature FLOAT, humidity FLOAT, air_quality INTEGER, pressure INTEGER, datetime DATETIME DEFAULT CURRENT_TIMESTAMP)")
		self.connection.commit()
		cursor.close()

	def add_data(self, dictionary):
		cursor = self.connection.cursor()
		print(dictionary)
		cursor.execute("INSERT INTO data (temperature, humidity, air_quality, pressure) VALUES (?, ?, ?, ?)", (
			dictionary["temperature"], dictionary["humidity"], dictionary["air_quality"], dictionary["pressure"]))
		self.connection.commit()
		cursor.close()

	def get_all_specific_data(self, data):
		cursor = self.connection.cursor()
		cursor.execute(f"SELECT {data}, datetime FROM data")
		values = cursor.fetchall()
		cursor.close()
		print(values)
		if values is None:
			return [{"x": None, "y": None}]
		return [{"x": date, "y": data_db} for data_db, date in values]

	def get_all_data(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM data")
		values = cursor.fetchall()
		cursor.close()
		if values is None:
			return {"id": None, "temperature": None, "humidity": None, "air_quality": None, "pressure": None, "date": None}
		liste = []
		for value in values:
			dictionary = {"id": value[0], "temperature": value[1], "humidity": value[2], "air_quality": value[3], "pressure": value[4], "date": value[5]}
			liste.append(dictionary)
		return liste

	def get_last_data(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
		values = cursor.fetchone()
		cursor.close()
		if values is None:
			return {data: None for data in self.datas}
		test_data = {data: value for data, value in zip(self.datas, values) if data != "id"}
		return test_data