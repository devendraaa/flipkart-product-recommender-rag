🛒 Flipkart Product Recommender (RAG-based AI System)

An end-to-end Retrieval-Augmented Generation (RAG) based product recommendation system for Flipkart-style e-commerce data.
The system leverages LangChain, Groq LLM, and AstraDB Vector Store to provide context-aware, history-aware, and accurate product recommendations, deployed using Docker and Kubernetes with production-grade monitoring.

🚀 Problem Statement

E-commerce platforms like Flipkart host millions of products and reviews.
Traditional keyword-based search often fails to deliver context-aware, personalized, and conversational recommendations.

This project addresses that gap by building a RAG-powered AI recommender that:

understands user intent,

retrieves relevant product knowledge,

and generates human-like, helpful recommendations using LLMs.

🧠 Solution Overview

This system combines vector-based retrieval with LLM reasoning to recommend products intelligently.

High-level flow:

User submits a query (e.g., “Best headphones under ₹2000 with good bass”)

Query is rewritten using history-aware retriever

Relevant product data is fetched from AstraDB Vector Store

Retrieved context is injected into Groq LLM

LLM generates concise, creative, and grounded recommendations

🏗️ Architecture

User
  ↓
Flask Web UI
  ↓
LangChain RAG Pipeline
  ├── Query Rephraser (History-aware)
  ├── AstraDB Vector Store (Embeddings)
  ├── Context Retrieval
  └── Groq LLM (Response Generation)
  ↓
Dockerized Application
  ↓
Kubernetes (GCP)
  ↓
Prometheus (Monitoring & Metrics)

🛠️ Tech Stack
AI / LLM

Groq LLM – ultra-fast inference

LangChain – RAG orchestration

HuggingFace Embeddings – vector generation

Data & Retrieval

AstraDB Vector Store – scalable vector search

History-aware Retriever – context preservation

Backend & Deployment

Flask – web application

Docker – containerization

Kubernetes (Minikube / GCP) – orchestration

kubectl – cluster management

Observability

Prometheus – application monitoring

Custom metrics – request count, latency

Version Control

GitHub

✨ Key Features

🔍 RAG-based product recommendations

🧠 History-aware conversational retrieval

✍️ Creative, LLM-generated product summaries

⚡ Low-latency responses using Groq

🐳 Fully containerized with Docker

☸️ Kubernetes-based scalable deployment

📊 Production monitoring using Prometheus

🔄 Modular, extensible architecture

📌 Example Use Cases

“Best Bluetooth headphones under ₹3000”

“Compare these with Sony models”

“Which one has better battery life?”

“Is it good for gaming?”

The system remembers conversation context and responds accordingly.

📈 Production Readiness

This project is designed with real-world deployment considerations:

Stateless application containers

Vector database for scalable retrieval

Kubernetes orchestration

Monitoring for performance and reliability

Clean separation of ingestion, retrieval, and generation layers

🧠 What I Learned

Designing and implementing RAG pipelines for real-world data

Building history-aware conversational AI systems

Integrating LLMs with vector databases

Deploying AI systems using Docker & Kubernetes

Monitoring AI applications using Prometheus

Debugging real-world deployment issues (image pull errors, cluster configs)


Conversation history is preserved for follow-up questions

🔮 Future Improvements

Add real-time data ingestion (scraping / APIs)

Implement RAG evaluation (RAGAS)

Add Grafana dashboards

Improve UI/UX

Multi-model routing for cost optimization

👤 Author

Devendra Umesh Chavan
AI Engineer
Founder – Saavo Avinya Pvt Ltd

⭐ Why This Project Matters

This project demonstrates:

LLM engineering

RAG system design

Cloud-native deployment

Production observability

End-to-end AI application thinking

It reflects how modern AI systems are built and deployed in industry, not just demos.
