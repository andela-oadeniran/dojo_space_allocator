
#import the needed modules
import sqlite3

class DojoDb():
    '''The module helps to create the connection
    to the sqlite3 database.'''
    def __init__(self, db_name):
        # create a db connection.
        self.conn = sqlite3.connect(db_name)
        self.curr = self.conn.cursor()

    def create_tables(self):
        # create tables in the database specified or use
        # the default.
        self.curr.executescript('''
            DROP TABLE IF EXISTS rooms;
            CREATE TABLE IF NOT EXISTS rooms
                (name CHAR, purpose TEXT, occupants TEXT, max_size INT);
            DROP TABLE IF EXISTS people;
            CREATE TABLE IF NOT EXISTS people
                (id INT, name TEXT, role TEXT, room TEXT);
            DROP TABLE IF EXISTS sessions;
            CREATE TABLE IF NOT EXISTS sessions
                (session BLOB);
            ''')
        # self.conn.commit()


    # def save_data(self,rooms_data, person_data, app_state):
    #     # write the application's data to the database
    #     if rooms_data:
    #         self.save_rooms_data(room_data)
    #     if person_data:
    #         self.save_people_data(person_data)
    #     self.save_state_data(app_state)

    def get_data(self):
        # create a connection to the given database
        # retrieve the app state and return.
        self.curr.execute('''SELECT * FROM sessions
            ''')
        app_state = self.curr.fetchone()[0]
        return app_state

    def delete_data(self):
        pass

    def save_rooms_data(self,room_data):
        self.create_tables()
        self.curr.executemany('INSERT INTO rooms VALUES(?,?,?,?)', room_data)
        self.conn.commit()


    def save_people_data(self, people_data):
        self.create_tables()
        self.curr.executemany('INSERT INTO people VALUES(?,?,?,?)', people_data)
        self.conn.commit()

    def save_state_data(self, app_state):
        self.create_tables()
        self.curr.execute('INSERT INTO sessions VALUES(?)', (app_state, ))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

