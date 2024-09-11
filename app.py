from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from textblob import TextBlob
import time
from database import config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config.Config)
Bootstrap(app)
db = SQLAlchemy(app)  # Initialize Flask-SQLAlchemy

# Define the database model for storing analysis results
class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    text = db.Column(db.Text, nullable=False)  # Text of the analysis
    sentiment = db.Column(db.Float)  # Sentiment score
    subjectivity = db.Column(db.Float)  # Subjectivity score
    token_count = db.Column(db.Integer)  # Number of tokens in the text

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html') 

# Route for analyzing the text input
@app.route('/analyze', methods=['POST'])
def analyze():
    start = time.time()  # Start time for analysis
    
    if request.method == 'POST':
        rawtext = request.form['rawtext']  # Retrieve raw text from the form
        blob = TextBlob(rawtext)  # Create a TextBlob object for sentiment analysis
        
        received_text = blob  # Store the TextBlob object for rendering
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity  # Get sentiment and subjectivity
        number_of_tokens = len(list(blob.words))  # Count the number of tokens in the text
        
        end = time.time()  # End time for analysis
        final_time = end - start  # Time taken for the analysis

        # Write data to the database
        analysis = Analysis(
            text=rawtext,
            sentiment=blob_sentiment,
            subjectivity=blob_subjectivity,
            token_count=number_of_tokens,
        )
        db.session.add(analysis)  # Add the record to the session
        db.session.commit()  # Commit the session to save the record

    # Render the index page with analysis results
    return render_template('index.html', received_text=received_text, number_of_tokens=number_of_tokens,
                           blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity,
                           final_time=final_time)

# Route to view the data stored in the database
@app.route('/view_data')
def view_data():
    analyses = Analysis.query.all()  # Query all records from the Analysis table
    return render_template('view_data.html', analyses=analyses)  # Render the view_data template with analysis records

# Function to initialize the database
def init_db():
    with app.app_context():
        db.create_all()  # Create the database tables

# Run the application
if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(host="0.0.0.0", port=5000)  # Run the Flask application on all network interfaces at port 5000
