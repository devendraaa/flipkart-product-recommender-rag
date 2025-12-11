from langchain_groq import ChatGroq
from langchain.retrievers.re_phraser import RePhraseQueryRetriever
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from flipkart.config import Config

class RAGChainBuilder:
    def __init__(self,vector_store):
        self.vector_store=vector_store
        self.model = ChatGroq(model=Config.RAG_MODEL , temperature=0.5) # main brain for llm , groq.
        self.history_store={}

    def _get_history(self,session_id:str) -> BaseChatMessageHistory: # custom message memory
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory() # stores memory, local memory storage
        return self.history_store[session_id]
    
    def build_chain(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k":3})
        # advance prompt format for bots and control conversation style 
        context_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and user question, rewrite it as a standalone question."),
            # insert history to prompt, memory slot in prompt.
            MessagesPlaceholder(variable_name="chat_history", optional=True), 
            ("human", "{input}")  
        ])
        qa_prompt = ChatPromptTemplate.from_messages([
            (
        "system",
        """
You are **Flipkart Genie**, a highly creative shopping expert.

Your job is to generate **engaging, high-quality product recommendations** using ONLY the provided context.

### 🎯 STRICT RULES:
- ALWAYS write a short, exciting intro line  
- ALWAYS write 3–4 **creative benefit-focused bullets** per product  
- ALWAYS describe **why the product is good**, not just features  
- ALWAYS sound like a friendly expert, not a robot  
- NEVER hallucinate outside the context  
- NEVER repeat the same wording  
- NEVER give flat bullets like “Good sound quality” — rewrite creatively  

### 🎨 STYLE YOU MUST USE:
- Smart, energetic, enthusiastic  
- Easy-to-read formatting  
- Clear value-focused descriptions  
- Add emojis to make it engaging  

### 🧱 OUTPUT TEMPLATE (MANDATORY):

**✨ Top Picks for Your Query**

{{% for product in products %}}
**{{ product.name }}**  
- ⭐ {{ product.point1 }}  
- 🎧 {{ product.point2 }}  
- 🔋 {{ product.point3 }}  
- 🎯 {{ product.point4 }}  

{{% endfor %}}

**💡 Final Recommendation**  
A short, helpful closing line tailored to the user's need.

---

The context contains product titles, specs and reviews.  
Extract product names automatically and produce the most relevant top recommendations.

CONTEXT:
{context}

QUESTION:
{input}
        """
    ),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}")
            ])

        # improve query or make query smarter , ex : complete query if user enter incomplete query.
        history_aware_retriever = RePhraseQueryRetriever.from_llm(
            llm=self.model,
            retriever=retriever,
            prompt=context_prompt
        )

        # insert document into llm , or gives llm the context
        question_answer_chain = create_stuff_documents_chain(
            self.model , qa_prompt
        )
        # Make RAG Pipeline, connect search + llm.
        rag_chain = create_retrieval_chain(
            history_aware_retriever,question_answer_chain
        )
        # Actual Conversation memory, Remember Everything.
        return RunnableWithMessageHistory(
            rag_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )


