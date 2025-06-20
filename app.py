import pandas as pd
import faiss
from langchain_community.llms import Ollama
import gradio as gr
from sentence_transformers import SentenceTransformer, models
import os
import csv

# Загрузка данных
print("Загрузка данных...")
df = pd.read_csv("products.txt")  
descriptions = df["description"].tolist()

# Создание эмбеддингов и индекса FAISS
print("Создание эмбеддингов и индекса FAISS...")
model_path = "C:/Users/Donete/Documents/Projets/Drone/projet4/all-MiniLM-L6-v2"

if not os.path.exists(model_path):
    raise FileNotFoundError("Папка шаблона не существует")

# Загрузка SentenceTransformer вручную (без HuggingFace Hub)
word_embedding_model = models.Transformer(model_path)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
embed_model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

# Эмбеддинги и индекс
embeddings = embed_model.encode(descriptions)
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
faiss_index.add(embeddings)

# Загрузка модели Mistral через Ollama
print("Загрузка модели Mistral через Ollama")
llm = Ollama(model="mistral")

# Функция генерации аннотации
def annotate(description, k=3):
    query_emb = embed_model.encode([description])
    D, I = faiss_index.search(query_emb, k)
    similar_descs = "\n".join(descriptions[i] for i in I[0])
    
    prompt = f"""
Ты — интеллектуальный помощник, который создает короткую, ясную и полезную аннотацию для карточки товара.

Описание товара:
{description}

Похожие товары:
{similar_descs}

Сформулируй краткую аннотацию (1-2 предложения).
"""
    annotation = llm.invoke(prompt).strip()

    #Автоматическое сохранение в annotations. csv
    with open("annotations.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([description, annotation])

    return annotation


# Интерфейс Gradio
iface = gr.Interface(
    fn=annotate,
    inputs=[
        gr.Textbox(lines=3, label="Описание товара"),
        gr.Slider(1, 5, value=3, step=1, label="Количество похожих товаров")
    ],
    outputs=gr.Textbox(label="Сгенерированная аннотация"),
    title="Автоматическая аннотация товаров (RAG + Mistral через Ollama)",
    description="Введите описание товара. Система сгенерирует короткую аннотацию на основе похожих товаров."
)

# Запуск интерфейса
if __name__ == "__main__":
    iface.launch()
