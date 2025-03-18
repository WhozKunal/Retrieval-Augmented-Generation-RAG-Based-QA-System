# COVID-19 FAQ RAG Chatbot

This project is a **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit** for answering COVID-19 related questions using a large FAQ dataset.

## Features
- **Efficient Retrieval:** Utilizes **FAISS** for fast similarity search.
- **LLM-Powered Generation:** Uses **Flan-T5**, **GPT-3.5**, or **LLaMA-2-7B** for enhanced response generation.
- **User-Friendly Interface:** Interactive chatbot interface built with **Streamlit**.

---

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo-link.git
cd Thrity
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

---

## Usage
- Enter your query in the text box.
- The chatbot will retrieve the most relevant answer from the FAQ dataset.
- It will then rephrase the answer using the selected LLM for improved clarity.

---

## Screenshot
Here's a preview of the chatbot interface:

![Chatbot Interface](Screenshot%202025-03-18%20151339.png)

---

## Dataset Details
- Source: **COVID-19 FAQ Dataset**
- Format: JSON structured data with question-answer pairs.

---

## Troubleshooting
### Torch Event Loop Error (Windows)
If you encounter this error:
```
RuntimeError: no running event loop
```
Add the following code at the top of `app.py`:
```python
import sys
import asyncio
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

---

## Contributing
Feel free to fork this repository, submit issues, or suggest improvements.

