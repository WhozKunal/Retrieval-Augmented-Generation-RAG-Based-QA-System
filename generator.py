from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
gen_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Generate response
def generate_response(answer):
    prompt = f"Rephrase the following answer:\n\nAnswer: {answer}"
    result = gen_pipeline(prompt, max_length=200)
    return result[0]['generated_text']
