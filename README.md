# Focus Group Generator

## Overview
This project automates the process of designing and conducting focus groups using AI tools. It includes generating archetypes, creating detailed personas, designing custom questions, simulating participant answers, and generating comprehensive reports. The framework is particularly suited for qualitative research and community engagement studies.

## Key Features
- **Archetype Generation**: Automatically create diverse participant profiles based on a given objective and restrictions.
- **Persona Creation**: Generate realistic, detailed personas for each archetype, including demographics, values, and priorities.
- **Custom Questions**: Design tailored focus group questions aligned with your study’s goals.
- **Simulated Answers**: Generate participant responses to questions based on their personas.
- **Comprehensive Reports**: Produce full focus group reports summarizing findings, insights, and recommendations.

## Usage

### Step 1: Define Objective and Restrictions
Set the focus group objective and participant restrictions:
```python
objective = "I want to know what people think about Emory University students."
restriction = "I want to only recruit people who exaggerate."
'''
### Step 2: Generate Archetypes
Generate 8 archetypes of focus group participants:
```python
message, archetypes = generateListOfArchetypes(objective, restriction)
'''
### Step 3: Create Personas
Generate realistic personas based on the archetypes:
```python
personas = generatePersonas(message, archetypes)
'''
### Step 4: Design Questions
Create focus group questions tailored to your objective:
```python
questions = generateQuestions(objective)
'''
### Step 5: Simulate Answers
Generate participant responses to the focus group questions based on their personas:
```python
for key in personas:
    generateAnswers(personas[key], questions)
'''
### Step 6: Generate Reports
Compile a comprehensive focus group report based on the personas and their simulated responses:
```python
generateReport(objective, personas)
generateReportDocument()
'''
