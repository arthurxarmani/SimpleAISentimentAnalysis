from utils import read_file, analyze_sentiment

def count_sentiments(file_path):
    """
    Core function to process the file and count sentiments.
    Will return a tuple of positive, neutral, and negative counts.
    """
    positive_count = 0
    neutral_count = 0
    negative_count = 0

    text = read_file(file_path)
    for line in text:
        sentiment = analyze_sentiment(line)
        if sentiment == "POSITIVE":
            positive_count += 1
        elif sentiment == "NEUTRAL":
            neutral_count += 1
        elif sentiment == "NEGATIVE":
            negative_count += 1

    return positive_count, neutral_count, negative_count

def process_file_cli():
    """
    Wrapper function for command-line interaction.
    """
    file_path = input("Enter file path: ")
    positive, neutral,negative = count_sentiments(file_path)
    print(f"Positive: {positive}")
    print(f"Neutral: {neutral}")
    print(f"Negative: {negative}")  


def process_file_cli_detailed():
    """
    Wrapper function that shows each line and its sentiment.
    """
    file_path = input("Enter file path: ")
    lines = read_file(file_path)
    for line in lines:
        sentiment = analyze_sentiment(line)
        print(f"{sentiment} - {line}")

if __name__ == "__main__":
    """
    Set up for the command line and detailed output. 
    Ex: POSITIVE - The course was a great investment, it helped us bond and learn.
    Can use count_sentiments() for testing or other inside other functions to avoid needing CLI input.
    """
    process_file_cli_detailed()
    #process_file_cli()
