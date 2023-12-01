# Coffee ReBrewer: An Interactive Tool to Find the Best Coffee in Town Using Aspect-Based Sentiment Analysis


## Description
Welcome to Coffee ReBrewer!

Our unique tool combines a NLP technique known as aspect-based sentiment analysis (ABSA) and an interactive Dash application to allow users to explore and discover the best cup of coffee.

The development is mainly based on python, and we use the plotly+Dash web framework. Most of the codes are put under the top directory which include the python class and functions for data clean, data filter, sentiment score analysis, data injestion, model evaluation and the web server. The Data folder is used to store the results from the data clean/filter/sentiment score and the original Yelp data set (not in the repo as it was 8.65 G). All of those data can be generated by our scripts from the original yelp dataset, however, it's cached here to speed up the web server's performance and furture evaluation experiment. Detail usage of the script can be found on Execution section.


## Installation
This project includes 2 versions of our application; 
* **app_mySQL_version.py** is the main version of our applicaiton. This version connects to our data on a mySQL database hosted on AWS through the mysqlproxy.py file.
* **app_local_data.py** connects directly to our pre-processed .csv files saved in the /Data folder. This version is a backup meant to maintain the app's functionality if we choose to stop maintaining the mySQL database in the future.


Both of versions can be installed as follows:
1. Clone the git repository.
2. Install the python requirements, either individually or by using the requirments file (```pip install requirements.txt```)


To get the original yelp dataset
1. Download the yelp data from https://www.yelp.com/dataset/download
2. Unzip the files and put it under ./Data/yelp_dataset.

## Execution
To run our application quickly (without reproducing our data processing steps), do the following;
1. Open the command prompt or terminal at the top-level of the repository and run the following command: 
    ```python3 app_mySQL_version.py```
2. Open your browser and navigate to the port where the app is running (provided by the terminal).

**Reproducing Our Data Processing and Model Evaluation Steps**

To run the Data Clean and Data Filter after unzipping the yelp data set:
1. Data Clean: ```python3 dataClean.py``` 
Notes: This will generate the cleanup data into the same folder of the source file, not the ./Data folder
2. Data Filter: ```python3 abas_filtered.py```
Notes: This will generate the filtered data into a csv file as well as the sentiment data in the file

Data Ingestion:
1. Currently we are using the mysql on AWS and it's hard coded. 
2. You can easily create an empty database and update the db server location in the mysqlproxy.py
3. Run: python3 mysqlproxy.py will create the tables and ingest the data into the database.

Model Evaluation
1. The model evaluation is done in modelTuner.py
2. Run ```python3 modelTuner.py```, to get the accuracy result on the terminal

