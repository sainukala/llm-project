from langchain_helper import get_few_shot_db_chain
import streamlit as st

st.title("Transaction Data: Q&A")

question = st.text_input("Ask me something: ")
if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)
    #response
    st.header("Here we go: ")
    st.code(response)
    #code
#    sql_query = chain.run(question)
#    st.subheader("SQLResult: ")
#    st.code(sql_query)
    #warning
    st.warning("Note: The output provided may not always be accurate as the system is continuously learning and evolving. Your understanding and patience are appreciated.")

