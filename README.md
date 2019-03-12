# Article-Recommender
Using LDA, the project recommends Wikipedia articles based on a search query.

## File Structure
- **collectData.py:** It includes the code to fetch Wikipedia articles based on a `category` and the `depth` of search
- **Pipfile.lock:** It includes the dependency information for easily setting up the environment using `pipenv`
- **README.md:** It includes the documentation for this repository
- **Modules**
  - **\_\_init.py\_\_:** Makes the `Modules` folder accessible as module in Python
  - **WikipediaCrawler.py:** Uses `wptools` to fetch Wikipedia pages and stores them to a **wikiData.db** database inside **data** folder
  
## Usage

### Data collection
Collect the data by invoking **collectData.py**. The file expects two arguments:
  - category: The category for which you want to search the articles
  - depth: The depth to which the search must take place
  
```
python collectData.py --category "Machine Learning" --depth 2
```

It creates a new folder **data** which includes a file **wikiData.db** with all the collected articles information including **id**, **category**, **url**, and **content**.
