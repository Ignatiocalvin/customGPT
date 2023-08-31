# customGPT
Ecommerce chatbot using GPT's model hosted on gradio. The chatbot is able to read custom data from the user in the form of CSVs and pdfs. The chatbot has memory and is able to answer previous questions based on the conversation history. The chatbot is also able to answer questions about the data it has been trained on.

## Installation
Install the necessary dependencies:

```pip install langchain```

```pip install openai```

```pip install gradio```

```pip install gpt_index```

## Run
Once repository is cloned locally, go to the project directory and run ```gradio customLLM.py```. The terminal will then return the addresses gradio is hosting on.

## Attention
If you encounter the error: 

```ImportError: cannot import name 'BaseLanguageModel' from 'langchain.schema'```

Then you will need to change ```from langchain.schema import BaseLanguageModel``` to ```from langchain.base_language import BaseLanguageModel``` in the base.py file of your gpt-index directory.


## WIP
- Using chainlit to create a UI for the chatbot.
