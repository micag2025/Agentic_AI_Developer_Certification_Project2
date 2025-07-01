# Agentic AI Developer Certification: ...................... for Exploring Ready Tensor Publications 

![Image Logo]()

### Tags : AAIDC2025, Agentic AI, Certification Program, LangChain, RAG, (RAG Evaluation), Agentic Systems, AI Agents, Generation-Evaluation, Graph Workflows, LangGraph, Writer-Critic, Custom Tools, Tools, Tool Design, Tool Use, Tool Integration, Tool Testing, Agent Workflows, Flow Engineering, AI Orchestration, LLM Applications, LLM, Evaluation, (LLM Evaluation) LangSmith, Monitoring, Observability, OpenAI, Agent Collaboration, Agent Design, Agentic Architectures, Agentic Patterns, Model Context Protocol, MCP, Protocols, Multi-Agent Systems, AI System Design, AI Systems, Entity Extraction, Keyword Extraction, Modular AI Systems, Tag Extraction, Design Pattens, System Architecture, Tool-Argumented Agents, AI Collaboration, Role Assignment, Task Decomposition, AI Integration, Agent Testing, AI Evaluation, Evaluation, Agent Reliability, Human-in-the-Loop, LLM Testing, LLM-as-a-Judge, System Benchmarks, AI Evaluation, Evaluation Methods, Golden Datasets, Human-in-the-Loop, LLM-as-a-Judge, Red Teaming, Safety Benchmarks, Agent Evaluation, Evaluation Framework, Evaluation Metrics, Evaluation Strategy, Metric Selection 




### Co-Authors: chibueze.k.muoneke@gmail.com, nyajuaya.j.a@gmail.com 
### Models : [Github]()
### Dataset: [project_1_publications.json](https://drive.google.com/drive/folders/1HAqLXL2W-sh8hqoBb1iSauJ_0wZVRxB9)


## TL;DR

The Ready Tensor Publication Explorer is an advanced AI-powered tool that utilizes Retrieval-Augmented Generation (RAG) techniques to automate the handling of a sample 
dataset that contains Ready Tensor technical documentation. By leveraging RAG models, the system delivers accurate and context-aware responses to (natural language) user queries. 
Integrating OpenAI embeddings, semantic search capabilities, and a user-friendly interface, this tools offers a scalable and efficient solution for Ready Tensor users, developers, 
researchers, and organizations searching streamlined access to documentation resources enclosed in the Ready Tensor platform by exploring its contents and asking questions.   


## Tool Overview & Architecture

This project uses a sample dataset and is built around (is structured on) a modular LangChain-based pipeline.

**Sample Dataset:**  
A collection of 35 Ready Tensor publications, each of them characterised by `id`, `username`, `license`, `title`, and `publication description`. There are 6 types of licenses; 
27 publications use “MIT” or “CC”, the rest are “none” or missing. Under MIT/CC, reuse is permitted for open source projects.

**Features & Modules:**  
This project is structured on a modular LangChain-based pipeline in which each feature is mapped to the specific tool or module implementing it:

| Feature                                    | Tool / Library / Module                             |
|---------------------------------------------|-----------------------------------------------------|
| Prompt formulation                         | LangChain PromptTemplate                            |
| Vector store retrieval                      | Chroma Vector Database                              |
| LLM-generated response                     | OpenAI GPT-3.5/4 via LangChain                      |
| Document ingestion & embedding              | LangChain DocumentLoader, OpenAI Embeddings, Chroma |
| Minimal UI for interaction                  | Streamlit (or Flask/FastAPI as implemented)         |
| Example queries, retrieval, response eval   | LangChain Chains & Evaluators                       |
| Session-based memory/intermediate reasoning | LangChain ReAct, ConversationBuffer                 |

**Workflow:** 
The LangChain-based pipeline is designed to:
1. Generate/process user prompts  
2. Retrieve relevant content using Chroma  
3. Use Large Language Models (LLMs) for context-aware responses  
4. Ingest/index documentation into vector DB  
5. Offer user interface for interaction  
6. Support session memory and intermediate reasoning  TO BE VERIFIED
7. Enable example queries for validation  

The core workflow and system architecture of the application are illustrated in the following flowchart.  
![flowchart_modified](flowchart_modified.jpeg)


## Features

- **Automated Documentation Ingestion:** Efficient extraction and processing of Ready Tensor publications (while preserving structure).
- **Vector Database Storage (Chroma):** Fast, reliable embedding storage and retrieval.
- **Semantic Search (OpenAI Embeddings):** Intelligent, context-aware lookup for relevant documentation.
- **RAG-Based Q&A:** Contextually precise answers to user queries about publications.
- **Minimal UI:** Simple, interactive interface (for exploration).
- **Scalable and Fast:** Handles large datasets with quick indexing and retrieval.


## Installation Instructions
This pubblication has a `GitHub code repository` attached under the "Code" section.

> **Prerequisites:** Python 3.10+, pip, and access to the referenced dataset.

1. **Clone the repository**
   ```bash
   git clone https://github.com/
   cd ............
   git checkout dev
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Linux / macOS
   .\.venv\Scripts\activate         # Windows
   ```
3. **Set your environment variables:**
   ```bash
   export OPEN_API_KEY=your_open_api_key_here    # Linux / macOS
   set OPEN_API_KEY=your_open_api_key_here       # Windows
   ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
## Running the Application
   
1. **Launch the App**
   > _Note:_ The `sample dataset` is available in the "Datasets" section.
   ```bash
   streamlit run app/main.py
   ```
2. **Open in browser**  
   Streamlit will provide a local URL (usually http://localhost:8501). Open it in your browser.

You can now interact with the Ready Tensor Publication Explorer!
 
### Example UI Screenshots

####  Home Page
*The main landing page of the Ready Tensor Publication Explorer, showing a **search bar** (selectbox for choosing a publication title and viewing its details) before the **chat interface**.*

![Home Page](output_ui_homepage.jpeg)  


####   Publication Search
*The search bar interface where users can view and search publications by title. (OR The search bar filters publications by title and the selectbox lists all filtered titles)*  

![Publication Search](output_ui_search.jpeg)  

####  Publication Details  
*Detailed view of the content of the selected publication, selected by title (When a title is selected, its content is shown)*

![Publication Details](output_ui_publication_details.jpeg)  

####   Q&A Chat Interface  
*Interactive chat interface for asking questions about publications using the RAG-powered assistant.*  

![Q&A Chat Interface](output_ui_chat.jpeg)  
> _Note: When a user asks a question in the chat, the agent has access to the content of **all publications** and can retrieve information from any or all of them to answer the query. The chat input can be used to ask about any aspect of the dataset, including questions that span multiple publications. Therefore, the agent will use the full dataset to answer, not just the selected publication.

## Usage Examples
The assistant helps users explore and comprehend Ready Tensor publications. Example general queries might be:  
- **Get a summary:**  
  “What is VAE?”
- **Extract details from a paper:**  
  “What models or tools were used in these publications?”
- **Discuss limitations:**  
  “Are there any assumptions or limitations mentioned in these publications?”

**Use Cases:**

- **For Ready Tensor Users:** Summarize papers or topics, chat with publication content
- **In Academia:** Automate literature reviews, semantic search for proposals
- **For Developers/Engineers:** Extract code examples, compare models
- **In Enterprises/Institutions:** Knowledge management, research assistant for editors


## API Documentation
API keys are stored securely in environment variables (for secure access). The API exposes endpoints for querying and interacting with Ready Tensor publications using the RAG pipeline.
> _Note:_ _All endpoints require authentication using your `OPENAI_API_KEY`._


## References
- [LangChain](https://www.langchain.com/langchain)                 
- [Openai API](https://platform.openai.com/account/api-keys)
- [MIT Licence](https://opensource.org/license/mit)
- [CC Licenses](https://creativecommons.org/share-your-work/cclicenses/)
- [Streamlit](https://docs.streamlit.io/)               
- [Ready Tensor Certifications](https://app.readytensor.ai/hubs/ready_tensor_certifications)
- [Technical Evaluation Rubric](https://app.readytensor.ai/publications/WsaE5uxLBqnH)
- [Engage and Inspire: Best Practices for Publishing on Ready Tensor](https://app.readytensor.ai/publications/engage_and_inspire_best_practices_for_publishing_on_ready_tensor_SBgkOyUsP8qQ)
- [Markdown for Machine Learning Projects: A Comprehensive Guide](https://app.readytensor.ai/publications/markdown_for_machine_learning_projects_a_comprehensive_guide_LX9cbIx7mQs9)
- [The Open Source Repository Guide: Best Practices for Sharing Your AI/ML and Data Science Projects](https://app.readytensor.ai/publications/best-practices-for-ai-project-code-repositories-0llldKKtn8Xb)


## Contributing
We welcome contributions to improve the Ready Tensor Publication Explorer!

1. **Fork** the [GitHub repository]()
2. **Create a feature branch:**
   ```bash
   git checkout -b your-feature-name
   ```
3. **Commit and push your changes**
4. **Submit a Pull Request** and describe your contribution.

Please follow our code style and guidelines. For questions or suggestions, [open an issue](https://github.com/Joshua-Abok/rag_apk/issues).

### Future Implementations
We are actively seeking contributors who want to help implement and/or propose the following future features:

- **Advanced UI/UX:** Develop a more intuitive and visually appealing web interface.
- **Expanded Dataset Support:** Enable ingestion of additional publication formats and sources.
- **Fine-tuned LLM Models:** Incorporate domain-specific or fine-tuned LLMs for improved accuracy.
- **User Authentication & Profiles:** Add user management, history tracking, and personalization.
- **Integration with Ready Tensor Platform:** Seamlessly connect with Ready Tensor’s broader ecosystem and APIs.
- **Export & Reporting:** Allow users to export summaries or Q&A sessions in various formats (PDF, CSV, etc).
- **Feedback & Rating System:** Let users rate answers to improve system performance.

Feel free to suggest more ideas by opening an issue or starting a discussion!  For bug reports or feature requests, [open an issue](https://github.com). For general questions or share 
your thoughts, start a [comment](https://app.readytensor.ai/publications/....).


## License
This publication is licensed under the [MIT License](LICENSE).


## Contact
chibueze.k.muoneke@gmail.com, michelaagostini73@gmail.com, nyajuaya.j.a@gmail.com 


## Acknowledgments
This project is part of the **Agentic AI Developer Certification**  program by the [Ready Tensor](https://www.readytensor.ai). We appreciate the contributions of the Ready Tensor developer 
community for their guidance and contributions. 
