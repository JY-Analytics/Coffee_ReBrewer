# Coffee ReBrewer: An Interactive Tool to Find the Best Coffee in Town Using Aspect-Based Sentiment Analysis


## Description
Welcome to Coffee ReBrewer!

Our unique tool combines a NLP technique known as aspect-based sentiment analysis (ABSA) and an interactive Dash application to allow users to explore and discover the best cup of coffee.

**TODO: add more project description and an overview of the repo once its better organized**

**TODO: add gif of the application in action**


## Installation
This project includes instructions for both a simple local-server setup and a remote-server setup on AWS.

To run the minimal version on a local server, complete the following steps:
1. Clone the git repository.
2. Install the python requirements, either individually or with the requirments file ("pip install requirements.txt")


To get the original yelp dataset
1. Download the yelp data from https://www.yelp.com/dataset/download
2. Unzip the files and put it under ./Data/yelp_dataset.

## Execution
To run the Data Clean and Data Filter after unzip the yelp data set:
1. Data Clean: python3 dataClean.py 
Notes: This will generate the cleanup data into the same folder of the source file, not the ./Data folder
2. Data Filter: python3 abas_filtered.py
Notes: This will generate the filtered data into a csv file as well as the sentiment data in the file

Data Ingestion:
1. Currently we are using the mysql on AWS and it's hard coded. 
2. You can easily create an empty database and update the db server location in the mysqlproxy.py
3. Run: python3 mysqlproxy.py will create the tables and ingest the data into the database.

Model Evaluation
1. The model evaluation is done in modelTuner.py
2. Run python3 modelTuner.py, you can get the accuracy result on the terminal

Launch the server
1. Open the command prompt or terminal from the repository and run the following command to execute the Dash app: "python3 app_Dash.py"
2. Open the browser and navigate to the port where the app is running (provided by the terminal).


**TODO: project description reccomends publishing a demo via an unlisted youtube video**
