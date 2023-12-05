from transformers import pipeline

# Create a question answering pipeline
qa_pipeline = pipeline('question-answering', model="distilbert-base-uncased-distilled-squad")

# Context paragraph
context = """Albert Einstein was a German-born theoretical physicist. He developed the theory of relativity, 
one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence 
on the philosophy of science."""

# Function to ask questions
def ask_question():
    # Get the user's question
    question = input("Enter your question: ")

    # Get the answer
    answer = qa_pipeline(question=question, context=context)
    print(f"Answer: {answer['answer']}")

    # Ask if the user has more questions
    more = input("Do you have another question? (yes/no): ")
    if more.lower() == 'yes':
        ask_question()

# Start the questioning process
ask_question()
