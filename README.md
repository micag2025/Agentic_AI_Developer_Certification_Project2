# Agentic_AI_Developer_Certification_Project2 _Module2


• Focus: Multi-Agent Workflows, Communication, LangGraph 
• Theme: Collaborative Problem Solving

## Objective 
• Design and implement a system composed of multiple specialized agents that coordinate to accomplish a complex task, showcasing multi-agent, role-based behavior, and inter-agent collaboration. 

## Requirements 
• Use of LangGraph or similar orchestration framework 
• At least two distinct agents with: Different roles (e.g., planner vs executor), Defined communication channels or memory sharing 
• Use of Model Context Protocol (MCP): implement agent interfaces and communication patterns compatible with MCP to ensure interoperability, modularity, and persistence support 
• A goal-driven flow: agents must work together to solve a user-defined problem or task (e.g., travel planner, multi-document summarizer, multi-turn form filler) 

## Deliverables 
• A multi-agent system with a clearly orchestrated workflow 
• Demonstration script or UI that showcases the collaboration 
• README explaining agent roles, task flow, and evaluation logic 
• Optional logs or performance summaries

 This project wraps up Module 2 by having you build a working multi-agent system that demonstrates the key concepts from Weeks 5-7: transitioning from workflows to
 agents and designing multi-agent collaboration using orchestration frameworks

  Project Objectives
 In this project, you'll design and implement a multi-agent system that demonstrates your mastery of the core Module 2 concepts:
 - Tool Integration: Show how agents can extend their capabilities through built-in and custom tools  
 - Multi-Agent Collaboration: Design agents with distinct roles that communicate and coordinate effectively  
 - Agent Orchestration: Use an orchestration framework (LangGraph, CrewAI, AutoGen, or similar) for workflow management

 Your system must include:  
 Required Components:  
 1. Multi-Agent System (minimum 3 agents)
    - At least 3 agents with distinct roles working together  
    - Clear communication or coordination between agents  
    - Use an orchestration framework (LangGraph, CrewAI, AutoGen, or similar)
 2. Tool Integration
     - Your system should integrate at least 3 different tools
     - Tools can be built-in (LangChain tools) or custom implementations
     - Tools should extend capabilities beyond basic LLM responses (e.g., web search, math calculations, file processing, API calls, etc.)  
 Optional Enhancements:  
 Human-in-the-loop interactions  
 Use of communication protocol such as MCP  
 Formal evaluation metrics and benchmarking against baselines


Cross-Publication Insight Assistant 🔍
 Build a system that helps users explore patterns and trends across multiple AI/ML projects. The input is a list of GitHub repos or Ready Tensor publications, plus an optional user query (e.g., tool usage, evaluation methods, task types).
 Support at least two of the following query patterns, each with multiple working examples:  
 Aggregate (Map-Reduce) – e.g., “What % of these projects use LangGraph?”  
 Compare & Contrast – e.g., “How do CrewAI and LangChain projects differ?”  
 Find & Summarize (RAG) – e.g., “Show me projects that use vector DBs”  
 🧠 Agents you might need:    
 Project Analyzer – inspects individual repos/publications for relevant attributes  
 Trend Aggregator – tallies, groups, or ranks signals across projects  
 Comparator – compares two project groups based on defined criteria  
 Summarizer – generates clear takeaways for the user  
 Fact-Checker – ensures outputs are grounded in project content  
 🛠 Tools you might use:  
 Repo Reader / Parser · Keyword/Tag Extractor · RAG Retriever · Web Search  

Project Publication 📝
 Create a short publication on the Ready Tensor platform that:
 Describes your project, what it does, and how it works
 Follows best practices from our Technical Evaluation Rubric for the
 Tool / App / Software Development category
 Meets at least 70% of the listed criteria

Project GitHub Repository 🗂
 Submit a repo that:
 📄 
Contains clean, working code for your multi-agent system
 Defines roles and communication flows between agents
 Includes setup instructions and sample interactions
 Meets the “Essential” level of our repo evaluation rubric
 Satisfies at least 70% of the Essential criteria
 
