# Data

The data set comes from Airline Reporting Carrier Dataset - IBM Developer. 

https://developer.ibm.com/exchanges/data/all/airline/

The dataset is of United States flights with data spanning from 1987 to 2020, reported to the United States Bureau of Transportation Statistics.
The dataset consist of 194,385,636 flights records in total.

The dataset contains information on nearly 200 million US flights between the years 1987 to 2020.
It contains basic information about each flight (such as date, time, departure airport, arrival airport) and, if applicable, the amount of time the flight was delayed and information about the reason for the delay. 
This dataset can be used to predict the performance of flight(s) and/or carrier(s). In particular, it can be used to predict the likelihood of a flight arriving on time.

# Data Wrangling

In order to bring the number of tuples within a reasonable range, we decided to work with the most recent data from 2011 onwards, containing approximately 58M records.  
The dataset has 109 columns, some of which were dropped.
The data had anomalies  where a flight had one origin but at the same time had multiple destinations (for the same date and CRSDepTime). Since it was a small set of records, we decided to drop these records altogether. 
Duplicate records were also present. They naturally had to be fixed before going any further.
A great proportion of flights had no more than 2 diversions. Thus, we decided to remove diversions 3, 4 and 5, since most of those were empty.  

# MongoDB schema

Proposed a document-oriented model that is pivoted around the destination airports\
Used the attributes that hold the information about flight delays, cancellations and diversions.
Each document in the collection is a destination airport having information about all the flights that landed on that particular airport, the category that the flight falls under (delayed, cancelled or diverted) and the origin airport of the respective flights in the collection.

# Itemset Mining

Identified association rules over data of the year period 2019-20.
A transaction comprises of the route taken by a flight operator where the flight operator is the itemset.
Created a new relation which consisted of the  different routes identified by a unique id and the flight operator flying that route.
Converted the relation from a tall format to a wide format.
Made use of mlxtend library in order to run the apriori algorithm  on the relation above to find frequent itemsets with a minimum support of 0.025 (2.5%).
Performed association rule mining on the frequent itemsets with a confidence of 0.75 (75%).

# Model-

Flight Cancellation probabilistic model using random forest and XGBoost


