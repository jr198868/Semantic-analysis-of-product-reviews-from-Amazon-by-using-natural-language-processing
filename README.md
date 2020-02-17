# Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing

#### ABSTRACT:

This project aims to build a model for sentiment analysis for the different product reviews from Amazon. This project can allow me to assign a score to a block of text that tells us how positive or negative it is. 

In this project, several practical tools including the NLTK (natural language toolkit), sklear, BeautifulSoup, and matplotlib have been used. 




##### Standard of Procedure:

	The following is a shortlist of steps for this process:
	# Loading data (only look at the electronics category in this project)
	# XML parser (BeautifulSoup) to scrap the key "review_text"
	# Two passes: one to determine the vocabulary size and the index corresponds to which word and one to create vectors  
	# Collect the total number of the distinct words and remove the "stop words"
	# Assign values to each state of vector
	# Implement SKLearn classifier to use a logistic regression model to look at the weights of the learned model to get a score for each individual input word

	
##### The dataset in this project is about product reviews from Amazon and derives from the Johns Hopkins University’s Department of Computer Science.
##### Download the datasets here: http://www.cs.jhu.edu/~mdredze/datasets/sentiment/

![Screenshot](https://github.com/jr198868/Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing/raw/master/pictures/Top_10_positive_word_features.png)
![Screenshot](https://github.com/jr198868/Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing/raw/master/pictures/Top_10_negative_word_features.png)

![Screenshot](https://github.com/jr198868//Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing/raw/master/pictures/Training_accuracy_vs_Classification_rate.png)

##### The final results are slightly different every time I run this model. The final classification rate is around only 70% accuracy. By using the logistic regression model, the weights for the negative sentiment words had negative values and the weights for the positive sentiment words had positive values. This simple interpretability is losing if another powerful model has been used. Sometimes in machine learning, the interpretation is more important than the accuracy.     

![Screenshot](https://github.com/jr198868//Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing/raw/master/pictures/run1.png)

![Screenshot](https://github.com/jr198868//Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing/raw/master/pictures/run2.png)


***





