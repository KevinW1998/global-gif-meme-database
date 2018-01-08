import sqlite3


class MemeDatabase:
    def __init__(self):
        self.__conn = sqlite3.connect('gif_database.db')
        # TODO: Get last id from the database
        self.__next_free_id = 0

        # Create TABLE if not exists
        self.__conn.execute(
            'CREATE TABLE IF NOT EXISTS file_references(id INTEGER PRIMARY KEY, filename TEXT)')

        # Get last id
        cur = self.__conn.cursor()
        cur.execute("SELECT id FROM file_references ORDER BY id DESC LIMIT 1")
        rows = cur.fetchall()
        if len(rows) > 0:
            self.__next_free_id = rows[0][0] + 1

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
        cur = self.__conn.cursor()
        cur.execute("SELECT * FROM file_references")
        return cur.fetchall()

    def get_file_reference_or_none(self, id):
        cur = self.__conn.cursor()
        cur.execute("SELECT * FROM file_references WHERE id = ?", (id,))
        return cur.fetchone()

    def remove_file_reference(self, id):
        try:
            self.__conn.execute(
                'DELETE FROM file_references WHERE id = ?', (id,)
            )
        except sqlite3.Error as e:
            print(e)
            return False
        return True
