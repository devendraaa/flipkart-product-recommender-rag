# 🛒 Flipkart Product Recommender (RAG-based AI System)

> An **end-to-end Retrieval-Augmented Generation (RAG)** product recommendation system for Flipkart-style e-commerce data, built with **LangChain, Groq LLM, and AstraDB**, and deployed using **Docker & Kubernetes** with **production-grade monitoring**.

---

## 🚀 Problem Statement

E-commerce platforms host millions of products and reviews.  
Traditional keyword-based search often fails to deliver:

- Context-aware results  
- Personalized recommendations  
- Conversational search experience  

This project solves that problem using **RAG + LLMs**.

---

## 🧠 Solution Overview

The system combines **vector-based retrieval** with **LLM reasoning** to generate intelligent product recommendations.

### High-level Flow:
1. User submits a query  
2. Query is rewritten using a **history-aware retriever**  
3. Relevant product data is fetched from **AstraDB Vector Store**  
4. Retrieved context is injected into **Groq LLM**  
5. LLM generates concise, creative, and grounded responses  

---


## 🏗️ Architecture

User
↓
Flask Web UI
↓
LangChain RAG Pipeline
├── Query Rephraser (History-aware)
├── AstraDB Vector Store
├── Context Retrieval
└── Groq LLM (Response Generation)
↓
Dockerized Application
↓
Kubernetes (GCP / Minikube)
↓
Prometheus (Monitoring & Metrics)


---

## 🛠️ Tech Stack

### AI / LLM
- **Groq LLM** – ultra-fast inference  
- **LangChain** – RAG orchestration  
- **HuggingFace Embeddings**

### Data & Retrieval
- **AstraDB Vector Store**
- **History-aware retriever**

### Backend & Deployment
- **Flask**
- **Docker**
- **Kubernetes (Minikube / GCP)**
- **kubectl**

### Observability
- **Prometheus** – application monitoring

---

## ✨ Key Features

- 🔍 RAG-based product recommendations  
- 🧠 History-aware conversational retrieval  
- ✍️ Creative, LLM-generated product summaries  
- ⚡ Low-latency inference using Groq  
- 🐳 Fully containerized with Docker  
- ☸️ Scalable Kubernetes deployment  
- 📊 Production-grade monitoring  

---

## 📌 Example Use Cases

- “Best Bluetooth headphones under ₹3000”  
- “Compare these with Sony models”  
- “Which one has better battery life?”  
- “Is it good for gaming?”  

➡ The system **remembers conversation context** for follow-up queries.

---

## 📈 Production Readiness

Designed with real-world deployment in mind:

- Stateless containers  
- Scalable vector retrieval  
- Kubernetes orchestration  
- Observability-first approach  
- Clean separation of RAG components  

---

## 🧠 What I Learned

- Designing **real-world RAG pipelines**  
- Building **history-aware conversational AI**  
- Integrating **LLMs with vector databases**  
- Deploying AI systems on **Docker & Kubernetes**  
- Monitoring AI workloads using **Prometheus**  
- Debugging real production issues  

---

## 🔮 Future Improvements

- Real-time data ingestion (APIs / scraping)  
- RAG evaluation (RAGAS)  
- Grafana dashboards  
- Improved UI/UX  
- Multi-model routing  

---

## 👤 Author

**Devendra Umesh Chavan**  
**AI Engineer**  
Founder – *Saavo Avinya Pvt Ltd*

---

## ⭐ Why This Project Matters

This project demonstrates:

- LLM engineering  
- RAG system design  
- Cloud-native deployment  
- Production observability  
- End-to-end AI system thinking  

> *A realistic example of how modern AI applications are built and deployed in industry.*


