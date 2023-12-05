# llm-models (DistilBert)
## How it works

Tokenization
The pipeline first tokenizes the input text. Tokenization involves breaking down the text into smaller pieces, or tokens. These tokens can be words or subwords or even characters, depending on the tokenizer's settings. In the case of DistilBERT, it usually breaks down text into word pieces.

Converting Tokens to Input IDs
The tokenizer then maps each token to an ID based on DistilBERT's vocabulary (it has fixed vocab). This step effectively turns your text into a sequence of numbers that the model can understand.

Processing by the Model
The sequence of input IDs is then fed into the DistilBERT model. The model processes this input through its multiple layers of neural networks. Each layer performs complex calculations and transformations on the input data.
The model outputs predictions for each token, indicating whether it believes each token is part of a named entity and, if so, what type of entity it is (e.g., person, organization, location).

Output Generation
The pipeline then collects these predictions and maps them back to the original text. It groups tokens corresponding to the same entity and labels them with the entity type.


# Installation and Setup (for Mac)
To set up DistilBERT locally on a Mac, you can follow these steps:

1. Install Python: Ensure you have Python installed on your Mac. If not, you can download it from python.org.

2. Install Pip: Pip is Python's package installer. It's usually included with Python, but you can check by running python -m pip --version in your terminal.

3. Create a Virtual Environment (Optional but Recommended):
  Open Terminal.
  Navigate to the directory where you want your project.
  Create a virtual environment by running **python3 -m venv myenv** (replace 'myenv' with your desired environment name).
  Activate the environment with source **myenv/bin/activate**.

4. Install Hugging Face's Transformers Library:
With your virtual environment activated, install the transformers library by running **pip install transformers**.

5. Install PyTorch:
Visit PyTorch's Get Started Page (https://pytorch.org/get-started/locally/) to find the installation command tailored for your setup.
Select your preferences (OS, Package, Language, CUDA version if you have GPU support) and copy the generated command.
Run the copied command in your terminal to install PyTorch. (In my case it was **pip3 install torch torchvision torchaudio**)

# Internet Requirement
In the codes used in this experiment, the model and tokenizer are fetched from Hugging Face's online model repository the first time you run the script. Here's how it works:

Initialization of the Pipeline:
When the line **pipeline('question-answering', model="distilbert-base-uncased-distilled-squad")** is executed, the transformers library checks if the specified model ("distilbert-base-uncased-distilled-squad") is available locally. If the model is not already downloaded on your system, it will be fetched from Hugging Face's online model repository and cached locally. This involves downloading the pre-trained model weights and any necessary configuration files.

Subsequent Use:
Once the model is downloaded and saved in your local cache, subsequent runs of the script will use the locally stored version. It will not download the model again unless you clear the cache or update the model version in your script.

Internet Requirement:
An internet connection is required for the initial download of the model. After the first download, no internet connection is needed, as the model will run locally using the cached version.

Model Storage:
The downloaded models are typically stored in a directory like ~/.cache/huggingface/transformers/ on your system.
This mechanism allows users to easily access and utilize a wide range of pre-trained models without having to manually download and configure them, making it convenient to start with NLP tasks using state-of-the-art models.

## Other NLP tasks that can be done
Code in this repo, does question/answering, sentiment check and Name-entity-recognition NLP tasks. distilBERT can do more tasks

Text Summarization: Generate a concise and fluent summary of a longer text.

Translation (limited compared to specialized models): Translate text from one language to another, although for complex translations, models specifically trained for translation tasks are more effective.

Text Generation (limited compared to models like GPT-3): Generate text based on a given prompt. DistilBERT can be used for this, but it's not its primary strength.

Feature Extraction: Use the model to convert text into feature vectors that can then be used in various machine learning applications.

Language Modeling: Predict the likelihood of a sentence or continuation of a sentence, useful in tasks like text completion or auto-correction.

Paraphrasing: Generate paraphrases of a given sentence. This might require additional fine-tuning or specific setups.

Semantic Similarity: Assess how similar two pieces of text are in terms of their meaning.
