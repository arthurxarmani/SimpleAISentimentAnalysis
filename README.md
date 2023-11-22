# 🤔 Sentiment Analysis with SiEBERT - English-Language Sentiment Classification

An example of performing sentiment analysis with Python Transformers. 

The model used is `siebert/sentiment-roberta-large-english`, demonstrating excellent results against a set of example reviews for a dog training course. 

The model classifies text, such as reviews, into "positive" or "negative" based on the language used.

It can 👉🏼 __can be directly used with your own text files__. 👈🏼 Text files are analyzed line by line. 

All tested reviews are in English. 🇬🇧

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install transformers.

```bash
pip install transformers
```

## Usage

```python
python main.py

# ---> Enter file path: dog_training_course_reviews_positive.txt

# NEGATIVE - Instructor was not attentive to the dogs, wouldn't recommend.
# NEGATIVE - Not a single technique from this course worked for my dog.
# NEGATIVE - Left the course more frustrated than when I started.
# NEGATIVE - The course had a few good points but overall was disappointing.
# NEGATIVE - Some techniques seemed useful, but generally, it was unsatisfactory.
# POSITIVE - The course was enlightening and my dog's behavior has improved.
# POSITIVE - I saw a significant positive change in my dog thanks to this course.
# POSITIVE - Well-structured training program with a knowledgeable instructor.
# POSITIVE - My dog is now obedient and well-behaved, all thanks to this course.
# POSITIVE - The course was a great investment, it helped us bond and learn.
# ...

```

```python
python test.py

# Runs a suite of tests on the various files and example cases in this repo.
# Tests demonstrate some sample capabilities of this model. 

# Tricky one to classify. Meets the customer's expectations, but has some drawbacks.
def longTextSlightlyPositive():
    slightly_positive_review = (
        "The dog training course was fairly standard and met my basic expectations. The lessons covered the usual commands and training techniques that are common in most training programs. "
        "The instructor was knowledgeable and provided clear instructions, but I didn't find any unique or particularly innovative methods being taught. My dog was able to learn the basics, such as sit, stay, and come, "
        "but I didn't notice a significant change in overall behavior. The course was organized and the materials were easy to follow, but it lacked the depth and customization I was hoping for. "
        "Overall, it was an adequate experience, suitable for someone who is just looking for fundamental training. I didn't encounter any major issues, but I also didn't feel particularly impressed by the end of the program. "
        "It's a decent course for beginners or for those who are new to dog ownership, but for someone with experience in dog training, it might not offer much beyond the basics."
    )
    assert analyze_sentiment(slightly_positive_review) == "POSITIVE"

def longTextNegative():
    negative_review = (
    "I was quite disappointed with the dog training course and felt it did not live up to the expectations set by its advertisements. The course content seemed outdated and the training methods were overly simplistic, "
    "offering little beyond basic commands that my dog already knew. The instructor, while knowledgeable, did not provide the personalized attention and advice that was promised. "
    "I struggled to see any real progress in my dog's behavior, and some of the techniques seemed to confuse rather than help my pet. The course also lacked structure and often felt disorganized, "
    "which made it challenging to follow along and stay engaged. Additionally, the support materials provided were minimal and not very useful. Overall, I regret enrolling in this course as it was a significant investment "
    "of time and money with very little to show for it. I was hoping for a transformative experience for my dog and me, but instead, I found myself frustrated and no better off than when I started."
    )
    assert analyze_sentiment(negative_review) == "NEGATIVE"
```

## Using this Model

```python
sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

def analyze_sentiment(text):
    result = sentiment_analysis(text)[0]
    return result['label']

```
😃 Check out more about this model on [Hugging Face](https://huggingface.co/siebert/sentiment-roberta-large-english).
Please cite [this paper](https://www.sciencedirect.com/science/article/pii/S0167811622000477) (Published in the [IJRM](https://www.journals.elsevier.com/international-journal-of-research-in-marketing)) when you use this model. 

## Sentiment Analysis 
Sentiment analysis helps in understanding opinions, attitudes, and emotions expressed in text. Here are some key instances where sentiment analysis is particularly valuable:

1. Customer Feedback Analysis: Businesses often rely on customer reviews and feedback to gauge satisfaction and identify areas for improvement. Sentiment analysis can automatically categorize this feedback as positive, negative, or neutral, providing quick insights into customer sentiment.

2. Social Media Monitoring: For brands and individuals who want to understand public perception, sentiment analysis can track and analyze social media posts and comments. This is useful for reputation management and marketing strategies.

3. Market Research: When launching new products or services, companies can use sentiment analysis to understand public reaction and reception. This helps in tailoring marketing strategies and product features.

4. Content Analysis: Media companies and content creators can use sentiment analysis to understand the emotional impact of their content, be it articles, videos, or other media.

5. Political Campaigns and Public Opinion: In politics, understanding public opinion is crucial. Sentiment analysis helps in analyzing speeches, social media posts, and news articles to gauge public sentiment towards policies, candidates, or events.

6. Customer Support Automation: Sentiment analysis can prioritize customer support tickets based on the sentiment expressed, ensuring that more critical or negative feedback is addressed promptly.

7. Financial Markets Analysis: Traders and analysts use sentiment analysis to gauge market sentiment from news articles, social media, and financial reports, which can influence trading decisions.

8. Healthcare and Patient Feedback: In healthcare, sentiment analysis can be used to analyze patient feedback, survey responses, and social media discussions about healthcare experiences and services.

By integrating sentiment analysis into these areas, one can gain deeper insights, respond more effectively to stakeholder needs, and make data-driven decisions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Alternate Features
By uncommenting `process_file_cli()`, you can receive a count of positive, neutral, and negative sentiment instead of having each line and it's sentiment printed out in full. This is useful when you only want to know the numerical result. 
```python
# Set up for the command line. 
# Can use count_sentiments in testing or other functions to avoid needing CLI input.
if __name__ == "__main__":
    process_file_cli_detailed()
    #process_file_cli()
```

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
