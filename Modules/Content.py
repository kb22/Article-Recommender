import sqlite3
from Modules.Cleaner import Cleaner


class Content:

    def __init__(self, db_file):
        self.categories = []
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cleaner = Cleaner()

    def get_ids(self):
        return [id for id in self.cursor.execute('SELECT id FROM wikiData')]

    def get_urls(self):
        return [url for url in self.cursor.execute('SELECT url FROM wikiData')]

    def get_page_by_id(self, id):
        return str(self.cleaner.clean_text(self.cursor.execute('SELECT content FROM wikiData WHERE id=?', id)
                    .fetchone()[0]))

    def get_url_by_id(self, id):
        return str(self.cursor.execute('SELECT url FROM wikiData WHERE id=?', id).fetchone()[0])

    def __iter__(self):
        for id in self.get_ids():
            page = self.get_page_by_id(id)
            yield self.cleaner.clean_text(page).split()
