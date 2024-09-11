# Sentiment Analysis
Sentiment Analysis app built using Textblob deployed through flask and docker with SQLite Database.

## To run the docker of the app:
	
	1. Build the docker image : docker buildx build . (sudo might be needed)
	2. Run the container : docker run -p 8888:5000 --name sentiment_analysis sentiment_analysis

**Now the docker is running on http://172.17.0.2:5000.**

## Usage:

	1. Enter a text and click "Submit" to receive the sentiment of the sentence as output.
	2. Colors help identfy positive, neutral or negative sentiment.
	3. The inputs and outputs are memorized in an SQLite DB and visible in another view accessed by clicking "View Data".


## Further development
	
	The app could be distributed on AWS installing the container on an EC2 instance and accessed via its public IP. SQLite could be replaced by a RDS using MySQL or PostgreSQL.

