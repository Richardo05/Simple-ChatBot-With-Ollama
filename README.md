# Simple-ChatBot-With-Ollama

## Setup Instruction

**1. Install Ollama and pull model**
   
   Download Ollama from [Ollama website](https://ollama.com/download/windows)
   
   After installed, go to command prompt and pull the model
   ```
ollama pull gemma3:1b
```

**2. Clone Repository**
```
git clone https://github.com/Richardo05/Simple-ChatBot-With-Ollama.git
cd Simple-ChatBot-With-Ollama
```

**3. Install Python Dependencies**
- Create New Virtual Environtment
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- Install Python Dependencies
  ```
  pip install Flask langchain langchain-community langchain-core
  ```

## Run the Application
```
python app.py
```
The application will start, you can press one of the link the pops up on the terminal

example: http://127.0.0.1:5000

## Testing
Go to text input, write a prompt, and click 'Send' button.

Wait, and you will see the response inside the chat box
