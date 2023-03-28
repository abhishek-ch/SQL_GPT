import openai
import os
openai.api_key = os.environ.get('OPENAI_API_KEY') 

def create_openapi_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "I would like you to be my data anlysts and generate accurate sql query for the question"},
                {"role": "assistant", "content": prompt}
            ]
        )
    code = response.choices[0].message.content
    result = '```sql\n' + code + '\n```'
    print(result)


def build_query_prompt(schema_details,query):

    input_str=f"""
    {schema_details}

    I would like you to be my data anlysts and generate accurate sql query for the question
    {query}

    - Make sure the query is postgres compitiable
    - Ensure case sensistivity
    - Ensure NULL check
    - Do not add any special information or comment, just return the query

    The expected output is code only. Always use table name in column reference to avoid ambiguity
    """

    return input_str


query = "grab the department ID and number of employees for each department from the employee table, but only if the employee count is greater than 3"

with open('constant.txt') as f:
    example_schema = f.readlines()

full_prompt = build_query_prompt(example_schema, query=query)
create_openapi_completion(full_prompt)