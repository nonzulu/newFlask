import os

class Functions():
	def get_database_connection(self):
		import sqlite3
		sqlite_file = 'site.db'
		file_exists = os.path.isfile(sqlite_file)
		conn = sqlite3.connect(sqlite_file)
		if not file_exists:
			create_sqlite_tables(conn)
		return conn

	def create_sqlite_tables(self,conn):
		cursor = conn.cursor()
		with open('schema.sql','r') as schema_file:
			cursor.executescript(schema_file.read())
		conn.commit()

	def check_name(self,id):
		conn = get_database_connection()
		try:
			cursor = conn.cursor()
			cursor.execute('SELECT id FROM Student WHERE id=?',(id))
			result =cursor.fetchone()
			if result:
				return result[0]
		except:
			return False
			
	