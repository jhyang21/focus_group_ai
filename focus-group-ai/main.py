from pydantic import BaseModel
from openai import OpenAI
from persona import Persona 

client = OpenAI()

# Get what the objective of the focus group is
objective = "I want to know what potential MBA candidates think about Stanford."
 
# Ask if there are restrictions
restrictions = "I want the focus group to be comprised only of young professionals in diverse industries with 4-6 years of experience."

class Archetypes(BaseModel):
    archetype1: str 
    archetype2: str
    archetype3: str
    archetype4: str
    archetype5: str
    archetype6: str
    archetype7: str
    archetype8: str
    
class Persona(BaseModel):
    fullname: str
    age: str
    race_ethnicity: str
    education_level: str
    income: str
    personality: str
    priorities: str
    values: str
    
class Questions(BaseModel):
    opening_question: str
    key_question1: str
    key_question2: str
    key_question3: str
    key_question4: str
    key_question5: str
    key_question6: str
    ending_question: str

# Decide what 8 personalities/demographics will be in the focus group
def generateListOfArchetypes(objective, restriction):
    
    prompt = [{"role": "system", "content": '''You are an expert on focus groups who excels at building and recruiting ideal focus groups. 
                                                Given the following objective and restrictions, give 8 ideal archetypes of individuals to be recruited for the focus group'''},
            {"role": "user", "content": f'''Objective: {objective}.
                                            Restriction: {restriction}'''}]
    
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=prompt,
        response_format=Archetypes,
    )
   
    return prompt, completion.choices[0].message.parsed


# Create a personality
def generatePersona(prompt: str, archetype: str): 
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": '''Based on the previous chat and archetype given, create a persona that is both realisitic and feasible.'''},
            {"role": "user", "content": f'''Previous Chat: {prompt}
                                            Archetype: {archetype}'''}
        ],
        response_format=Persona,
    )
   
    return completion.choices[0].message.parsed

# Come up with Focus Group Questions
def generateQuestions():
    prompt = [{"role": "system", "content": '''You are an expert on focus groups who excels at building and recruiting ideal focus groups. 
                                                Given the following objective, come up with 1 opening question, 6 key questions, 1 ending quesiton.'''},
            {"role": "user", "content": f'''Objective: {objective}.'''}]
    
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=prompt,
        response_format=Questions,
    )
   
    return prompt, completion.choices[0].message.parsed

# Generate answer to one question given persona
def generateAnswer(persona, question, answer):
    pass

# Generate Report for each question based on the personality 
def generateReport():
    pass



# Allow interaction with each participant

### MAIN ###
message, archetypes = generateListOfArchetypes()
personas = []
for key in archetypes:
    personas.append(generatePersona(message,archetypes[key]))

for persona in personas:
    print(persona)
    
print()