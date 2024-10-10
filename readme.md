
# 🌕 Web History Analysis for "Fall from Height" Regulations on the Moon 🏗️

## 📖 Overview
This project serves as an HCI (Human-Computer Interaction) test to study how participants respond to new challenges. The experiment involves asking questions related to "Fall from Height" regulations on the Moon and analyzing participants' web search activities to answer these questions. The goal is to track their problem-solving process and gather insights to help create new safety regulations for lunar construction.

## 📋 Prerequisites
- **Python 3.x** 🐍
- **Required Libraries**: `sqlite3`, `pandas`, `matplotlib`
- **Web History Access** 🌐: (e.g., Chrome's History file)
- **Protege for Ontology Creation** 🧩: Download from [Protege](https://protege.stanford.edu/)

## 🛠️ Installation

1. **Clone the Repository** 📂:
   ```bash
   git clone <repository-url>
   ```
2. **Install Required Libraries** 📦:
   ```bash
   pip install pandas matplotlib
   ```
3. **Set Up Protege** 🧩:
   - Download and install Protege from [Protege](https://protege.stanford.edu/).

## 🚀 Experiment Setup

### Step 1: 🗄️ Extract Web History Data  
   - Use the provided Python script to extract web history from the browser's SQLite database (e.g., Chrome's `History` file).
   - The script retrieves data such as the URL, title, visit count, and last visit time for each search.

### Step 2: 🧹 Preprocess the Data  
   - Clean the extracted data and convert timestamps into a human-readable format.
   - Filter relevant URLs that provide information about fall prevention regulations and lunar construction.

### Step 3: 🔍 Analyze Data and Track Participant Responses  
   - Use the analysis functions to identify how participants approach each question based on their search behavior.
   - Manually verify the results where necessary, noting the methods used by participants to solve the problems.

### Step 4: 🧩 Create an Ontology Using Protege  
   - Manually analyze the relevant web pages and participant responses to create an ontology that answers the five questions.
   - Use Protege to visually structure the ontology and represent relationships between concepts.

### Step 5: 📊 Draw an Interactive Knowledge Graph  
   - Utilize tools like `Graphviz` or `Neo4j` to design an interactive knowledge graph.
   - Incorporate insights from the ontology and web history analysis to illustrate connections between safety regulations, environmental factors, and solutions.

## 📝 Experiment Rules and Problem Descriptions

### ⚖️ Rules
   - Participants must answer each question within the specified time limit.
   - Automated tools, such as ChatGPT, are not permitted.
   - All searches should be conducted manually, and web history must be logged for analysis.

### ❓ Problems

1. **How can we create a preemptive regulation to prevent "fall from height" issues when building houses with locally sourced materials on the Moon? (10 min)**  
   - Explore existing building regulations and safety standards.
   - Propose new guidelines considering unique lunar conditions like low gravity and surface composition.

2. **What regulations are there to prevent fall accidents on Earth? (5 min)**  
   - Search for existing standards such as OSHA guidelines and building codes related to fall prevention.
   - Summarize key points, including scaffolding, harness systems, and guardrails.

3. **How are fall accidents different on the Moon? (5 min)**  
   - Identify differences due to the Moon's environment, including reduced gravity and the impact of spacesuits.
   - Analyze how these factors might change the nature of fall accidents and safety requirements.

4. **How can current regulations be applied on the Moon? (5 min)**  
   - Compare Earth's regulations with the lunar environment to assess necessary adaptations.
   - Discuss the challenges and possible solutions for implementing these safety standards.

5. **Draw an interactive knowledge graph (10 min)**  
   - Create a visual representation using gathered data and the developed ontology.
   - Display connections between regulations, risks, and safety measures in the context of both Earth and the Moon.

## ⚠️ Limitations
- Methods for extracting web history may require adjustments for different browsers (e.g., Firefox).
- Ontology creation involves manual effort and a degree of domain expertise.
- The analysis is restricted to the browsing history available during the experiment.
