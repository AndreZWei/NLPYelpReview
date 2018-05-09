# NLPYelpReview

### Author: Boyang Lu, Zhangyang Wei, Jie Zhou

The project performs two tasks:

1. Extract food-related keywords from yelp reviews

2. Correlate yelp ratings with review sentiments


Data:
We used the data from http://www.yelp.com/dataset. We processed and serialized the data. The stored data files are in the data folder.


## Task 1: KeywordExtraction.py

### Part 0: Tokenize the reviews
### Part 1: Use nltk to find the unigram, bigram and trigram collocations
### Part 2: Use tf-idf to find the collocations that are specific to each document (business)
### Part 3: Find food-related collocations
#### Method 1: wordnet
#### Method 2: word2vec

#### Note: It takes a long time to run the entire program (~30 mins on my machine), but each part is designed to be tested separately, given the data needed. In the code before each part there is a section for reading in the data. To test the a single part of the program, uncomment the section for reading in the data and comment out all the other parts. The two methods in part 3 are not designed to be tested together. Please ensure that one method is commented out completely when testing the other one.


## Task 2: SentimentScore.py

#### We used the textblob sentiment function. The code can be directly executed and tested.
