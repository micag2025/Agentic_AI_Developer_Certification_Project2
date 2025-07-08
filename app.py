
# app.py  (Main Streamlit App)

"""
Streamlit UI for comparing scientific publications.
"""

import os
import json
import streamlit as st
from dotenv import load_dotenv
from explorer import PublicationExplorer

# Load .env file
load_dotenv()

# Load keys
openai_key = os.getenv("OPENAI_API_KEY", "")
tavily_key = os.getenv("TAVILY_API_KEY", "")

# Streamlit UI
st.set_page_config(page_title="Publication Comparator", layout="wide")
st.title("📊 Scientific Publication Comparator")

# Display masked keys
with st.sidebar:
    st.subheader("🔐 API Keys")
    st.write("✅ OPENAI_API_KEY loaded." if openai_key else "❌ OPENAI_API_KEY not found.")
    st.write("✅ TAVILY_API_KEY loaded." if tavily_key else "❌ TAVILY_API_KEY not found.")
    if openai_key:
        st.text(f"OPENAI: {openai_key[:5]}{'*' * (len(openai_key) - 10)}{openai_key[-5:]}")
    if tavily_key:
        st.text(f"TAVILY: {tavily_key[:5]}*****")

# Load publications
pub_dir = "sample_publications"
pub_files = sorted(f for f in os.listdir(pub_dir) if f.endswith(".txt"))

pub1 = st.selectbox("Select Publication 1", pub_files, key="pub1")
pub2 = st.selectbox("Select Publication 2", pub_files, key="pub2")

query_options = [
    "Tool Usage", "Evaluation Methods", "Task Types", "Datasets", "Results", "Other (custom)"
]
query_choice = st.selectbox("Select a query type", query_options)
user_query = st.text_input("Or type your custom query:", "") if query_choice == "Other (custom)" else query_choice

if st.button("🚀 Run Comparison"):
    explorer = PublicationExplorer()
    state = {
        "pub1_path": os.path.join(pub_dir, pub1),
        "pub2_path": os.path.join(pub_dir, pub2),
        "user_query": user_query,
        "pub1_profile": "",
        "pub2_profile": "",
        "comparison": "",
        "trends": "",
        "summary": "",
        "fact_check": "",
        "extra_info": "",
        "lnode": "",
        "count": 0
    }
    result = explorer.graph.invoke(state)

    # Display results
    st.subheader("✅ Summary")
    st.text_area("Summary", result["summary"], height=300)

    with st.expander("📘 Fact Check"):
        st.text_area("Fact Check", result["fact_check"], height=300)

    with st.expander("🧠 Enrichment"):
        st.text_area("ReAct Agent Output", result.get("extra_info", "[No enrichment]"), height=300)
