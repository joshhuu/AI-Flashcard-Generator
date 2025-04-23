import re
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("valhalla/t5-base-qg-hl")
model = AutoModelForSeq2SeqLM.from_pretrained("valhalla/t5-base-qg-hl").to(DEVICE)

def generate_question(answer: str, context: str) -> dict:
    """Generate a question given the answer and context paragraph."""
    # Case-insensitive replace, wrap only first match
    pattern = re.compile(re.escape(answer), re.IGNORECASE)
    if not pattern.search(context):
        raise ValueError(f"Answer '{answer}' not found in context.")
    highlighted = pattern.sub(f"<hl> {answer} <hl>", context, count=1)

    prompt = f"generate question: {highlighted}"
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)

    outputs = model.generate(
        **inputs,
        max_length=64,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    question = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"question": question, "answer": answer}
