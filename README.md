# Agentic AI Developer Certification:LangGraph-Orchestrated Research Assistant for Ready Tensor

## Objective   
• Design and implement a system composed of multiple specialized agents that coordinate to accomplish a complex task, showcasing multi-agent, role-based behavior, and inter-agent collaboration.   
• Build a working multi-agent system that demonstrates transitioning from workflows to agents and designing multi-agent collaboration using orchestration frameworks    
• This project is designed and implemented a multi-agent system that demonstrates concepts such as:  
 - _Tool Integration_: Show how agents can extend their capabilities through built-in and custom tools    
 - _Multi-Agent Collaboration_: Design agents with distinct roles that communicate and coordinate effectively    
 - _Agent Orchestration_: Use an orchestration framework (LangGraph) for workflow management  

## Requirements 
• Use of LangGraph  orchestration framework     
• The system includes a Multi-Agent System:   
    - At least 3 agents (4? agents) with distinct roles working together        
    - Clear communication or coordination between agents        
    - Use a LangGraph orchestration framework    
• The system includes a Tool Integration:  
   - The system integrates at least 3 different tools    
   - Tools are built-in (LangChain tools) or custom implementations    
   - Tools extend capabilities beyond basic LLM responses (e.g., web search, math calculations, file processing, API calls, etc.)  
 
 Optional Enhancements:    
- Human-in-the-loop interactions      
- Use of communication protocol such as MCP  ( Use of Model Context Protocol (MCP): implement agent interfaces and communication patterns compatible with MCP to ensure interoperability, modularity, and persistence support)        
- Formal evaluation metrics and benchmarking against baselines           

## Deliverables 
• A multi-agent system with a clearly orchestrated workflow 
• Demonstration script or UI that showcases the collaboration 
• README explaining agent roles, task flow, and evaluation logic 


## Use Case 
Cross-Publication Insight Assistant    
Build a system that helps users explore patterns and trends across multiple AI/ML projects. The input is a list of Ready Tensor publications, plus an optional user query (e.g., tool usage, evaluation methods, task types).  
Support at least two of the following query patterns, each with multiple working examples:  
 - Aggregate (Map-Reduce) – e.g., “What % of these projects use LangGraph?”    
 - Compare & Contrast – e.g., “How do CrewAI and LangChain projects differ?”    
 - Find & Summarize (RAG) – e.g., “Show me projects that use vector DBs”
      
 🧠 Agents you might need:    
 - Project Analyzer – inspects individual repos/publications for relevant attributes    
 - Trend Aggregator – tallies, groups, or ranks signals across projects    
 - Comparator – compares two project groups based on defined criteria    
 - Summarizer – generates clear takeaways for the user    
 - Fact-Checker – ensures outputs are grounded in project content    
 🛠 Tools you might use:    
 Repo Reader / Parser · Keyword/Tag Extractor · RAG Retriever · Web Search    


## Repository Structure
```
TO BE ENCLOSED
```
