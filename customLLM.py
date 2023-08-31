from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import gradio as gr
import sys
import os

os.environ["OPENAI_API_KEY"] = ''

# Add convo history to preserve memory 
conversation_history = []

def construct_index(directory_path):
    # Parameters for the GPT Model
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('./index.json')

    return index

def chatbot(input_text):
    global conversation_history
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    # Update conversation history
    conversation_history.append(input_text)

    # Construct context from history
    context = "\n".join(conversation_history)

    # Query the index
    response = index.query(context, response_mode="compact")

    # Update conversation history
    conversation_history.append(response.response)

    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Ecommerce Chatbot")

index = construct_index("./docs")
iface.launch(share=True)