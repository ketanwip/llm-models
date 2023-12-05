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
