# Sentiment Analysis
Sentiment Analysis app built using Textblob deployed through flask and docker with SQLite Database.

To run the docker of the app:
	
	1. Build the docker image : sudo docker buildx build .
	2. Run the container :   docker run -p 8888:5000 --name sentiment_analysis sentiment_analysis

	Now the docker is running on http://172.17.0.2:5000.




