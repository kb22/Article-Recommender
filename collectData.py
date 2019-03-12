# Import libraries
import os
import argparse

# Import modules
from Modules.WikipediaCrawler import WikipediaCrawler

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--category', dest='category')
parser.add_argument('-d', '--depth', dest='depth')
values = parser.parse_args()

# Define variables based on arguments
if (values.depth and values.category):
    category = 'Category:' + str(values.category)
    search_depth = values.depth
else:
    print('Error: Please enter both category and depth')
    exit(1)

# Create data directory
if not os.path.exists('data'):
    os.makedirs('data')

# Collect data
crawler = WikipediaCrawler('data/wikiData.db')
crawler.collect_data(category, int(search_depth))
print("The database has been generated")
