from transformers import pipeline

# https://huggingface.co/siebert/sentiment-roberta-large-english
sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")

# This function reads a file and returns the text content as an array of lines.
# Each line is a string in the array.
def read_file(file_path):
    """
    Reads a file and returns the text content as an array of lines.
    Each line is a string in the array.
    """
    with open(file_path, 'r') as f:
        return f.readlines()
    
def analyze_sentiment(text):
    """
    Analyzes the sentiment of a string of text using the model. 
    Returns "POSITIVE", "NEGATIVE".
    """
    result = sentiment_analysis(text)[0]
    return result['label']