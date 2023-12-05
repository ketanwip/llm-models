from transformers import pipeline

# Create an NER pipeline
ner_pipeline = pipeline('ner', model="elastic/distilbert-base-cased-finetuned-conll03-english")

# Text to analyze
text = "Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California."

# Perform NER: Name, entity, recognition
entities = ner_pipeline(text)

# Print the entities
for entity in entities:
    print(f"Value: {entity['word']}, Entity: {entity['entity']}, Score: {entity['score']}")
