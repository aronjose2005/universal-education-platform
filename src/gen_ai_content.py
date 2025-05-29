from transformers import pipeline
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK data
nltk.download('vader_lexicon')

# Generate personalized content using Llama (simulated with a smaller model)
def generate_content(student_data):
    generator = pipeline("text-generation", model="facebook/opt-350m")  # Llama placeholder
    prompt = f"Create educational content for a {student_data['learning_style']} learner: {student_data['text_input']}"
    content = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return content

# Sentiment analysis for tone adjustment
def adjust_tone(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    if sentiment["compound"] < 0:
        return f"Adjusted for positivity: {text}"
    return text
