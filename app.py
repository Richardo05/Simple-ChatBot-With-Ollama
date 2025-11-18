from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import langchain
from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import requests

app = Flask(__name__)

# class Answer(BaseModel):
#     answer: str = Field(description='Answer to the question')

try:
    model = Ollama(model='gemma3:1b')

    # output_parser = JsonOutputParser(pydantic_object=Answer)

    template = """
        You are a helpful and concise AI assistant. Answer the user's question clearly.
    
        QUESTION: {question}

        ANSWER: 
    """

    # prompt = PromptTemplate(
    #     template=template,
    #     input_variables=["question"],
    #     partial_variables={"format_instructions": output_parser.get_format_instructions()},
    # )
    prompt = PromptTemplate.from_template(template)

    chain = prompt | model

    print('Ollama Langchain initialized with model: gemma:2b')

except Exception as e:
    print(f"ERROR: Could not initialize Ollama/LangChain.")
    print(f"Details: {e}")
    chain = None


@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/inference', methods=['POST'])
def ineference():
    data = request.json

    user_input = data.get('prompt') or data.get('question')

    response = chain.invoke({'question': user_input})
    print(response)
    return jsonify({'answer': response})

if __name__ == '__main__':
    print("Starting Ollama Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)

