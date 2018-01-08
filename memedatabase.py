import sqlite3


class MemeDatabase:
    def __init__(self):
        self.__conn = sqlite3.connect('gif_database.db')
        # TODO: Get last id from the database
        self.__next_free_id = 0
        self.__conn.execute(
            'CREATE TABLE IF NOT EXISTS file_references(id INTEGER PRIMARY KEY, filename TEXT)')

    def get_next_free_id(self):
        return self.__next_free_id

    def create_safe_filename(self, filename):
        """

        :param filename:
        :type filename str
        :return:
        """
        index_of_dot = filename.find('.')
        return '%s_%d.%s' % (filename[:index_of_dot], self.__next_free_id, filename[index_of_dot+1:])

    def save_file_reference(self, filename):
        self.__conn.execute(
            'INSERT INTO file_references VALUES(?, ?)', (self.__next_free_id, filename)
        )
        self.__conn.commit()
        self.__next_free_id += 1

    def get_all_file_references(self):
        self.__conn.execute("SELECT * FROM file_references")
        rows = self.__conn.fetchall()

        for row in rows:
            print(row)


    def remove_file_reference(self, id):
        self.__conn.execute(
            'DELETE FROM file_references WHERE id = ?', (id,)
        )
        pass

