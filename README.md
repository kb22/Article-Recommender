# Article-Recommender
Using LDA, the project recommends Wikipedia articles based on a search query.

## File Structure
- **config.yml:** It includes the details for paths of various models and data resources which we will need
- **collectData.py:** It includes the code to fetch Wikipedia articles based on a `category` and the `depth` of search
- **generateLDA.py:** It includes the code to generate the LDA Model and also store it inside **data** folder
- **evaluate.py:** It includes the code to use the LDA Model to evaluate on a query string and recommend articles 
- **Pipfile.lock:** It includes the dependency information for easily setting up the environment using `pipenv`
- **README.md:** It includes the documentation for this repository
- **.gitignore:** Includes a list of files and folders to be ignored by git
- **LICENSE:** It includes the license information
- **Modules**
  - **\_\_init.py\_\_:** Makes the `Modules` folder accessible as module in Python
  - **WikipediaCrawler.py:** Uses `wptools` to fetch Wikipedia pages and stores them to a **wikiData.db** database inside **data** folder
  - **Cleaner.py:** It defines a class with a set of methods that can pre-process and clean the text
  - **Content.py:** It defines a class to pre-process the data as well as get information from the database
- **sample_images**
  - **recommendations.png:** Sample output of the model for the search query *Machine learning applications*
  
## Usage

### Data collection
Collect the data by invoking **collectData.py**. The file expects two arguments:
  - category: The category for which you want to search the articles
  - depth: The depth to which the search must take place
  
```
python collectData.py --category "Machine Learning" --depth 2
```

It creates a new folder **data** which includes a file **wikiData.db** with all the collected articles information including **id**, **category**, **url**, and **content**.

### Generate LDA Model
By running the **generateLDA.py** file, the LDA model is generated. It also stores the models and information inside **data** folder as **lda_model**, **dictionary** and **corpus**. Use the folloing command to run the file:

```
python generateData.py
```

### Recommend Articles
Next, by invoking the **evaluator.py**, articles can be recommended. It extects one argument:
  - query: The text query based on which you want to search for articles
  
```
python evaluator.py --query "Machine learning applications"
```
 
The above command will give the output as some key words identified from the phrase and top 10 most relevant Wikipedia articles based on the search query.
 
### Sample Output for query "Machine learning applications"

![recommendations](https://github.com/kb22/Article-Recommender/blob/master/sample_images/recommendations.png)
 
