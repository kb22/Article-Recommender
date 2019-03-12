import sqlite3
import wptools
import re
from bs4 import BeautifulSoup


class WikipediaCrawler:

    def __init__(self, db_file):
        self.categories = []
        self.conn = sqlite3.connect(db_file)
        cursor = self.conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS wikiData (id text, category text, url text, content text)')
        self.conn.commit()
        self.cursor = self.conn.cursor()

    def insert_page_content(self, id, category, url, content):
        self.cursor.execute('INSERT INTO wikiData VALUES (?, ?, ?, ?)',
                            (id, category, url, content))
        self.conn.commit()

    def get_ids(self):
        return [id for id in self.cursor.execute('SELECT id FROM wikiData')]

    def get_urls(self):
        return [url for url in self.cursor.execute('SELECT url FROM wikiData')]

    def collect_data(self, category, depth):
        if depth:
            print("Extracting data for subcategories of {} at depth {}".format(
                category, depth))
            cat = wptools.category(category)
            cat_members = cat.get_members()

            if 'members' in cat_members.data.keys():
                for cat_member in cat_members.data['members']:
                    if cat_member['pageid'] not in self.get_ids():
                        try:
                            page = wptools.page(
                                pageid=cat_member['pageid']).get_parse()
                            url = page.get_query().data['url']
                            text = BeautifulSoup(
                                page.data['wikitext'], 'html.parser').get_text()
                            clean_text = re.sub(
                                r'\s*{.*}\s*|\s*\[.*\]\s*', '', text)
                            print('Saving page with Id: {} and URL: {}'.format(
                                cat_member['pageid'], url))
                            self.insert_page_content(
                                cat_member['pageid'], category, url, clean_text)
                        except Exception as e:
                            print("Exception occured: {}".format(e))

            if 'subcategories' in cat_members.data.keys():
                sub_cats = cat_members.data['subcategories']
                for sub_cat in sub_cats:
                    self.categories.append(sub_cat)
                    self.collect_data(sub_cat['title'], depth - 1)
