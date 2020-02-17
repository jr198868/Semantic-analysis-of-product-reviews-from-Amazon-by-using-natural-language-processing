# Semantic-analysis-of-product-reviews-from-Amazon-by-using-natural-language-processing

## 3. Recent Projects

### 3.1 Predicting the potential for organohalide respiration in wastewater? Comparison of intestinal and wastewater microbiomes

##### ABSTRACT:
This study aims to assess the potential organohalide respiration capacity in wastewater biosolids by investigating actively organohalide respiring bacteria with a focus on organohalide respiration of PCBs and PCE. Subsequently, it was evaluated if the OHR microbial populations in biosolids were similar to those present in intestinal human biofilms by applying a bioinformatic approach. The OHR populations of the communities were analyzed from existing American and Chinese human intestinal microbiomes. The overall groups Proteobacteria, Bacteroides, Actinobacteria, and Firmicutes phyla dominated the microbiomes in all datasets. The OHR groups in biosolids and intestinal biofilms included Dehalogenimonas, Dehalobacter, Desulfitibacter, Desulfovibrio, Sulfurospirillum, Clostridium, and Comamonas. The results of this study showed that several OHR phyla were present in all samples independent of origin. Wastewater and intestinal microbiomes also contained OHR phyla. 

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


### 3.3 Compression of 16s-rRNA sequence by using enhanced Run-length encoding

	
![Screenshot](https://github.com/jr198868/Compression-of-16s-rRNA-sequence-by-using-enhanced-run-length-encoding/raw/master/materials/Graphic_abstract_5.jpg)

![Screenshot](https://github.com/jr198868/Compression-of-16s-rRNA-sequence-by-using-enhanced-run-length-encoding/raw/master/materials/Graphic_abstract_6.jpg)

##### Encoding code: https://github.com/jr198868/Compression-of-16s-rRNA-sequence-by-using-enhanced-run-length-encoding/blob/master/code/Enhanced%20run-length%20encoding%20code

##### Decoding code:

##### Standard of Procedure:

	Step 1: Sequence cleaning 
	Step 2: Run-length encoding and append the encoded data into the final_seq_data 
	step 3: Construct modified (enhanced) Run-length encoding 
	Step 4: level II encoding for the sequence compression
	Step 5.1: Find the commonly repeated subsequence with 6 characters 
	Step 5.2: Construct the index (str(i) +'*') which will be used to "encode" the repeated sequences
	Step 5.3: Construct a dictionary {Commonly repeated subsequence: index}
	Step 6: Run level II encoding
	

##### This project is still ongoing! More cases of the commonly repeated subsequence other than 6 characters will be discussed.

***
## 4. Software Engineering Projects

#### 4.1 Using a multipleprocess calculation (Distributed computing) to achieve a factorial function (09/2019)

- Used **BaseManager** to implement data sharing across multiple processes

- Used **BaseManager** module to allow other users/computers accessing the data by using a Queue to pass messages back and forth

code: https://github.com/jr198868/Using-a-mutipleprocess-calculation-to-achieve-a-factorial-function-from-1-to-100 

#### 4.2 Scraping Data of Software Development Engineer from LinkedIn Profiles (08/2019)

- Used **Selenium** to complete login form and navigate to various pages including completing the username and password fields and clicking the login button 

- Used **Scrapy CrawlSpider** to collect data from LinkedIn profiles 

code: https://github.com/jr198868/Scraping-Data-of-Software-Development-Engineer-from-LinkedIn-Profiles 

#### 4.3 Instagram Prototype (Raymond Insta) (05/2019-08/2019)

- Created a web-based application has the same functionality as Instagram by using VS code, including features such as **registration**, **posting**, **commenting**, and **following**

- Designed required models (User, Post, Comment, Like, and User Connections). Used <r>**Ajax**<r> to create dynamic views

- Implemented backend with **Django**, database with **SQLite**

code: https://github.com/jr198868/Raymond_Insta 

***
## 6. COURSERA Online Education

- Practical Machine Learning [(Link)](https://www.coursera.org/learn/practical-machine-learning/home/welcome)
- The Data Scientist’s Toolbox [(Link)](https://www.coursera.org/learn/data-scientists-tools/home/welcome)
- Developing Data Products [(Link)](https://www.coursera.org/learn/data-products/home/welcome)
- Regression Models [(Link)](https://www.coursera.org/learn/regression-models/home/welcome)
- Statistical Inference [(Link)](https://www.coursera.org/learn/statistical-inference/home/welcome)
- Reproducible Research [(Link)](https://www.coursera.org/learn/reproducible-research/home/welcome)
- Exploratory Data Analysis [(Link)](https://www.coursera.org/learn/exploratory-data-analysis/home/welcome)
- Getting and Cleaning Data [(Link)](https://www.coursera.org/learn/data-cleaning/home/welcome)
- R Programming [(Link)](https://www.coursera.org/learn/r-programming/home/welcome)





