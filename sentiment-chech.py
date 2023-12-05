from transformers import pipeline

# Create a sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

# Text to analyze
text = "feeling down today"

# Perform sentiment analysis
result = sentiment_pipeline(text)

# Print the result
print(result)
