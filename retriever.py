import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load COVID FAQ dataset
def load_data(file_path):
    with open(file_path, 'r', encoding='utf8' ) as file:
        data = json.load(file)
    questions = []
    answers = []
    for entry in data['data']:
        for paragraph in entry['paragraphs']:
            for qa in paragraph['qas']:
                questions.append(qa['question'])
                answers.append(qa['answers'][0]['text'])
    return questions, answers

# Create embeddings
def create_index(questions):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(questions, convert_to_tensor=True).cpu().detach().numpy()
    
    # Build FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    return index, embeddings

# Retrieve answer
def retrieve_answer(query, questions, answers, index):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().detach().numpy()
    
    # Search in FAISS index
    distances, indices = index.search(query_embedding, 1)
    return questions[indices[0][0]], answers[indices[0][0]]
