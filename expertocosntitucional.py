import streamlit as st
from langchain import HuggingFacePipeline
from langchain import PromptTemplate
from langchain import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
import torch
import torchvision
from src.encabezado import head






def page2():
    modelo ="Experto Constitucional"
    descripcion="Responde preguntas en relación a la constitución chilena rechazada"
    
    st.write(head(modelo, descripcion))

    # OJO! max_length tiene que ser suficiente como para tener el documento (chuck) + el prompt + el system prompt + respuesta generada !!!
    llm = HuggingFacePipeline.from_model_id(model_id="OpenAssistant/stablelm-7b-sft-v7-epoch-3", task="text-generation",
                                         model_kwargs={"temperature": 0.0, "max_length": 2048, 'device_map': 'auto'})
    template = """<|prompter|>{question}<|endoftext|><|assistant|>"""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "Qué dice el texto en relación a las neurodiversidades?"
    llm_chain.run(question)
    # This is a long document we can split up.
    with open('Doc/constidemo.txt', encoding='utf-8') as f:
        pg_work = f.read()
    
#print (f"You have {len([pg_work])} document")

        text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
        chunk_size = 150,
        chunk_overlap  = 20,
)

        texts = text_splitter.create_documents([pg_work])

    embeddings = HuggingFaceEmbeddings()

    query_result = embeddings.embed_query(texts[0].page_content)

    vectorstore = Chroma.from_documents(texts, embeddings)

    qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever(), return_source_documents=True)

    chat_history = []
    query = "Qué dice el texto en relación a las neurodiversidades?"
    result = qa({"question": query, "chat_history": chat_history})
    result["answer"]

    st.write()