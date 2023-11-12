import math
from collections import Counter
from datasets import load_dataset

def calculate_surprise(text):
    word_count = len(text.split())
    word_freq = Counter(text.split())
    entropy = 0
    
    for word, freq in word_freq.items():
        prob = freq / word_count
        entropy += -prob * math.log(prob, 2)
    
    return entropy

def calculate_burst(text):
    word_count = len(text.split())
    unique_word_count = len(set(text.split()))
    burst = unique_word_count / word_count
    return burst

def calculate_compatibility(text):
    dataset = load_dataset("reddit")
    score = 0
    words = text.split()

    for word in words:
        count = sum(1 for data in dataset['train'] if word in data['text'])
        score += count

    compatibility = score / len(words)
    return compatibility

def detect_ai_text(text):
    surprise = calculate_surprise(text)
    burst = calculate_burst(text)
    compatibility = calculate_compatibility(text)
    probability = (surprise + burst + compatibility) / 3
    threshold = 0.5

    if probability > threshold:
        print("This text is written by an AI.")
    else:
        print("This text is written by a human.")

text = "Bu metin, yapay zeka tarafından yazılmıştır. Bu metnin şaşkınlık, patlama ve uyumluluk değerleri yüksektir. Bu metni okuyan insanlar, bunun bir yapay zeka üretimi olduğunu anlayabilirler."
detect_ai_text(text)
