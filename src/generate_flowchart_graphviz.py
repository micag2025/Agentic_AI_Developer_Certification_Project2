# generate_graphviz_flowchart.py

"""
Generates a vertical Graphviz PNG diagram of the LangGraph orchestration flow
and saves it to the docs/ directory.

Agent Roles and Specializations:
Z: Ready Tensor dataset      - Prepares/loads the dataset for analysis
A: select_pub1               - Selects the first publication
C: select_pub2               - Selects the second publication
B: analyze_pub1              - Analyzes the first publication
D: analyze_pub2              - Analyzes the second publication
E: compare                   - Compares both analyzed publications
F: aggregate_trends          - Aggregates trends from comparison
G: summarize                 - Summarizes aggregated findings
H: fact_check_node           - Fact-checks summarized information
I: END                       - Workflow completion
"""

import os
from graphviz import Digraph
from IPython.display import Image, display

# Define output path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)
#from paths import DOCS_DIR
from paths import SRC_DIR

OUTPUT_PATH = os.path.join(DOCS_DIR, "publication_flowchart")

# Agent descriptions for clarity
agent_descriptions = {
    'Z': 'Prepare/load the Tensor dataset for analysis',
    'A': 'Select the first publication for analysis',
    'C': 'Select the second publication for analysis',
    'B': 'Analyze the first publication',
    'D': 'Analyze the second publication',
    'E': 'Compare analysis results of both publications',
    'F': 'Aggregate trends/findings from the comparison',
    'G': 'Summarize the aggregated trends',
    'H': 'Fact-check the summary for accuracy',
    'I': 'End state (workflow completion)'
}

# Create the flowchart
dot = Digraph(comment="LangGraph Flowchart", format='png')
dot.attr(rankdir='TB', fontsize='12')

# Nodes with annotated roles and specializations in comments and as tooltips
dot.node('Z', 'Ready Tensor dataset', shape='folder', style='filled', fillcolor='lightgray', tooltip=agent_descriptions['Z'])  # Prepare/load the Tensor dataset
dot.node('A', 'select_pub1', tooltip=agent_descriptions['A'])  # Select the first publication
dot.node('C', 'select_pub2', tooltip=agent_descriptions['C'])  # Select the second publication
dot.node('B', 'analyze_pub1', tooltip=agent_descriptions['B'])  # Analyze the first publication
dot.node('D', 'analyze_pub2', tooltip=agent_descriptions['D'])  # Analyze the second publication
dot.node('E', 'compare', tooltip=agent_descriptions['E'])  # Compare the analysis results
dot.node('F', 'aggregate_trends', tooltip=agent_descriptions['F'])  # Aggregate trends from comparison
dot.node('G', 'summarize', tooltip=agent_descriptions['G'])  # Summarize the aggregated trends
dot.node('H', 'fact_check_node', tooltip=agent_descriptions['H'])  # Fact-check the summarized information
dot.node('I', 'END', shape='doublecircle', tooltip=agent_descriptions['I'])  # Workflow completion

# Edges
dot.edge('Z', 'A')
dot.edge('Z', 'C')
dot.edge('A', 'B')
dot.edge('C', 'D')
dot.edge('B', 'E')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')


# Generate PNG only (no .md, no .gv)
output_png_path = dot.render(filename=OUTPUT_PATH, view=False)
print(f"✅ PNG flowchart saved to: {output_png_path}")

# Display for notebooks or interactive shell
if __name__ == "__main__":
    display(Image(filename=output_png_path))
