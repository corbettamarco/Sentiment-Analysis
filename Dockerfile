# Use the Python 3.7 slim image
FROM python:3.7-slim

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Create a working directory
WORKDIR /sentiment_analysis

# Copy the requirements file
COPY requirements.txt /sentiment_analysis/

# Install Python modules needed by the Python app
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary corpora for TextBlob
RUN python -m textblob.download_corpora && \
    python -c "import nltk; nltk.download('omw-1.4')"

# Copy the application files into the container
COPY app.py /sentiment_analysis/
COPY templates /sentiment_analysis/templates/
COPY database /sentiment_analysis/database/


# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "/sentiment_analysis/app.py"]
