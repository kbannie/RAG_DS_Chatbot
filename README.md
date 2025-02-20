# 🤖 DS Chatbot

This project is a chatbot designed to provide users with information about the academic regulations of **Duksung Women’s University**. The chatbot leverages **Retrieval-Augmented Generation (RAG) and LangChain** to retrieve relevant data and generate accurate, context-aware responses.

## Installation & Usage
### 1. Set up Python Environment
Create and activate a virtual environment.

```bash
python3.10 -m venv {env_name} 
source {env_name}/bin/activate
```

### 2. Install Dependencies
Install the required Python packages. To load .hwp files, you need to additionally install [langchain-teddynote](https://github.com/teddylee777/langchain-teddynote). Also, it requires Python 3.10 or higher.

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a .env file in the project root directory and add your OpenAI API key, LANGCHAIN_API_KEY and PINECONE_API_KEY. 


### 4. Run the Chatbot (Streamlit)
Launch the chatbot interface using Streamlit.
```bash
streamlit run chat.py
```

## References
- Regulation Source : [Duksung Women's University Academic Regulations](https://rule.duksung.ac.kr/lmxsrv/main/main.do)
- Data Storage : [Google Drive](https://drive.google.com/drive/folders/1gbaiF2jGaYUOm6-O_ETSQLeOuOnlHBi6?usp=sharing)
- Notion Page : [DS Chatbot - Notion](https://kabeenportfolio.notion.site/DS-Chatbot-19ed35bbb00b806bbbafef96d748f81d)
