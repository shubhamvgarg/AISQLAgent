import streamlit as st
from graph.graph_builder import build_agent

st.set_page_config(page_title="AskSQL", layout="wide")

st.title("💬 AskSQL")
st.write("Ask questions in plain English and get SQL results.")

query = st.text_input("Enter your question:")

if st.button("Run Query"):
    if query:
        agent = build_agent()

        with st.spinner("Thinking..."):
            response = agent.invoke({
                "question": query
            })

        if response.get("error"):
            st.error(response["error"])
        else:
            st.subheader("Generated SQL")
            st.code(response["validated_sql"], language="sql")

            st.subheader("Results")
            st.write(response["result"])
