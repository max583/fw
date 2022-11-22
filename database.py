import sqlite3

class Database:

    def __init__(self):
        self.connection = sqlite3.connect(f"fw.db")
        cursor = self.connection.cursor()
        result = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'words'")
        if result.fetchone() is None:
            cursor.execute("CREATE TABLE words(word text, status text)")
        result = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'parameters'")
        if result.fetchone() is None:
            cursor.execute("CREATE TABLE parameters(name text, value text)")
        self.connection.commit()
        self.__fill_cache()

    def add_word(self, word):
        cursor = self.connection.cursor()
        result = cursor.execute(f"SELECT word FROM words WHERE word = '{word}'")
        if result.fetchone() is None:
            result = cursor.execute(f"INSERT INTO words VALUES ('{word}','active')")
            self.connection.commit()
        else:
            result = cursor.execute(f"update words set status='active' where word = '{word}'")
            self.connection.commit()

    def update_word(self, old_word, new_word):
        cursor = self.connection.cursor()
        result = cursor.execute(f"update words set word = '{new_word}' where word = '{old_word}'")
        self.connection.commit()

    def delete_word(self, word):
        cursor = self.connection.cursor()
        result = cursor.execute(f"delete from words where word = '{word}'")
        self.connection.commit()

    def __fill_cache(self):
        cursor = self.connection.cursor()
        result = cursor.execute(f"select word from words where status = 'active' ORDER BY RANDOM() limit 100")
        self.words = result.fetchall()
        self.word_pointer = 0

    def get_word(self):
        if self.word_pointer >= 100 or self.word_pointer >= len(self.words):
            self.__fill_cache()
        if len(self.words) > 0:
            word = self.words[self.word_pointer][0]
        else:
            word = ''
        self.word_pointer += 1
        return word

    def __del__(self):
        self.connection.close()

    def set_parameter(self, name, value):
        cursor = self.connection.cursor()
        result = cursor.execute(f"SELECT name FROM parameters WHERE name = '{name}'")
        if result.fetchone() is None:
            result = cursor.execute(f"INSERT INTO parameters VALUES ('{name}','{value}')")
        else:
            result = cursor.execute(f"update parameters set value='{value}' where name = '{name}'")
        self.connection.commit()

    def get_parameter(self, name):
        cursor = self.connection.cursor()
        result = cursor.execute(f"SELECT value FROM parameters WHERE name = '{name}'")
        row = result.fetchone()
        if row is None:
            value = ''
        else:
            value = row[0]
        self.connection.commit()
        return value


if __name__ == '__main__':
    db = Database()
    for i in range(20):
        print(db.get_word())

    db.set_parameter('rapid_key','3623bee911msh93ad8449311d407p18d408jsnd1c153180d0a')