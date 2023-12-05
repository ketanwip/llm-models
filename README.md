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

Install Python: Ensure you have Python installed on your Mac. If not, you can download it from python.org.

Install Pip: Pip is Python's package installer. It's usually included with Python, but you can check by running python -m pip --version in your terminal.

Create a Virtual Environment (Optional but Recommended):
  Open Terminal.
  Navigate to the directory where you want your project.
  Create a virtual environment by running **python3 -m venv myenv** (replace 'myenv' with your desired environment name).
  Activate the environment with source **myenv/bin/activate**.

Install Hugging Face's Transformers Library:
With your virtual environment activated, install the transformers library by running **pip install transformers**.

Install PyTorch:
Visit PyTorch's Get Started Page (https://pytorch.org/get-started/locally/) to find the installation command tailored for your setup.
Select your preferences (OS, Package, Language, CUDA version if you have GPU support) and copy the generated command.
Run the copied command in your terminal to install PyTorch. (In my case it was **pip3 install torch torchvision torchaudio**)

