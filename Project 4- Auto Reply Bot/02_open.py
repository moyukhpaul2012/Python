from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
Your command here
'''
completion = client.chat.completions.create(
  model="your_gpt_model",
  messages=[
    {"role": "system", "content": "Your description to the AI model"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)