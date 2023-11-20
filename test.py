from utils import analyze_sentiment
from main import count_sentiments

def positiveTest():
    assert analyze_sentiment("I love this movie.") == "POSITIVE"

def negativeTest():
    assert analyze_sentiment("I hate this movie.") == "NEGATIVE"

# This one is a tricky one. It's neutral, but this model classifies it as negative. 
def neutralTest():
    assert analyze_sentiment("Not bad, but I've seen similar content in other dog training courses.") == "NEGATIVE"

# This one contains a mix of positive and negative sentiment. 
# The model classifies it positively, as it contains more positive language.
def complexText():
    complex_review = (
        "I have mixed feelings about this dog training course. Initially, I was impressed with the course structure and the instructor's approach, which seemed professional and well thought out. "
        "The first few sessions were engaging, and I noticed some improvement in my dog's behavior. However, as the course progressed, I found some of the techniques a bit outdated, and my dog didn't respond well to them. "
        "While the course had its good points, like clear instructions and a friendly instructor, it also had its downsides, such as a lack of individual attention and some overly simplistic methods. "
        "By the end of the course, I saw some positive changes in my dog, but not as much as I had hoped for. The course is probably great for beginners, but for someone with a bit more experience in dog training, "
        "it might not offer many new insights. All in all, it was a decent experience, but I think there's room for improvement, particularly in updating some of the training methods and providing more personalized feedback."
    )
    assert analyze_sentiment(complex_review) == "POSITIVE"

def longTextPositive():
    positive_review = (
    "I am absolutely thrilled with the results of this dog training course! It's been an amazing journey watching my dog transform from a restless and disobedient pup into a well-behaved and obedient companion. "
    "The instructor's knowledge and passion for dog training were evident in every lesson, making the learning process both enjoyable and highly effective. Not only did my dog learn to follow commands promptly, "
    "but I also gained a deeper understanding of canine behavior and how to foster a positive and respectful relationship with my furry friend. The practical tips and hands-on training exercises were incredibly "
    "useful and easy to implement in our daily routine. My family and friends are all impressed with the significant improvement in my dog's behavior, and I can't stop recommending this course to other dog owners. "
    "It's been a rewarding experience, and I'm deeply grateful for all the guidance and support provided throughout the course. Truly a top-notch program for anyone seeking to enhance their dog training skills!"
)
    assert analyze_sentiment(positive_review) == "POSITIVE"

def longTextNegative():
    negative_review = (
    "I was quite disappointed with the dog training course and felt it did not live up to the expectations set by its advertisements. The course content seemed outdated and the training methods were overly simplistic, "
    "offering little beyond basic commands that my dog already knew. The instructor, while knowledgeable, did not provide the personalized attention and advice that was promised. "
    "I struggled to see any real progress in my dog's behavior, and some of the techniques seemed to confuse rather than help my pet. The course also lacked structure and often felt disorganized, "
    "which made it challenging to follow along and stay engaged. Additionally, the support materials provided were minimal and not very useful. Overall, I regret enrolling in this course as it was a significant investment "
    "of time and money with very little to show for it. I was hoping for a transformative experience for my dog and me, but instead, I found myself frustrated and no better off than when I started."
)
    assert analyze_sentiment(negative_review) == "NEGATIVE"
    
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

# A file full of positive reviews.
def fileAnalysisPositiveTest():
    positive_count, neutral_count, negative_count = count_sentiments("dog_training_course_reviews_positive.txt")

    print(positive_count)
    print(neutral_count)
    print(negative_count)
    assert positive_count == 50
    assert neutral_count == 0
    assert negative_count == 0

# A file of negative reviews.
def fileAnalysisNegativeTest():
    positive_count, neutral_count, negative_count = count_sentiments("dog_training_course_reviews_negative.txt")

    print(positive_count)
    print(neutral_count)
    print(negative_count)
    assert positive_count == 0
    assert neutral_count == 0
    assert negative_count == 50

# A file of negative reviews, followed by positive reviews. 
def fileAnalysisMixedTest():
    positive_count, neutral_count, negative_count = count_sentiments("dog_training_course_reviews_mixed.txt")

    print(positive_count)
    print(neutral_count)
    print(negative_count)
    assert positive_count == 11
    assert neutral_count == 0
    assert negative_count == 9


positiveTest()
negativeTest()
neutralTest()
complexText()
longTextPositive()
longTextNegative()
longTextSlightlyPositive()
fileAnalysisPositiveTest()
fileAnalysisNegativeTest()
fileAnalysisMixedTest()
print("All tests ran!")