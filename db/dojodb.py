
#import the needed modules
import sqlite3

class DojoDb():
    '''The module helps to create the connection
    to the sqlite3 database.'''
    def __init__(self, db_name):
        # create a db connection.
        self.db_name = db_name

    def create_tables(self):
        # create tables in the database specified or use
        # the default.
        self.conn = sqlite3.connect(self.db_name)
        self.curr = self.conn.cursor()
        self.curr.executescript('''
            DROP TABLE IF EXISTS app_session_data;
            CREATE TABLE app_session_data
                (app_session_pickle BLOB);
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
        self.conn = sqlite3.connect(self.db_name)
        self.curr = self.conn.cursor()
        self.curr.execute('''SELECT * FROM app_session_data
            ''')
        app_session_data = self.curr.fetchone()[0]
        return app_session_data

    def delete_data(self):
        pass

    def save_data(self, app_session_pickle):
        self.curr.execute('INSERT INTO app_session_data VALUES(?)', (app_session_pickle,))
        self.conn.commit()
        print('Your session has been saved to the database {}'.format(self.db_name))

    # def save_people_data(self, people_data):
    #     self.curr.execute('INSERT INTO people VALUES(?)', people)
    #     self.conn.commit()

    # def save_state_data(self, app_state):
    #     self.curr.execute('INSERT INTO app_session VALUES(?)', app_session)
    #     self.conn.commit()

    def close_connection(self):
        self.conn.close()

