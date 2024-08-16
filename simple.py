import sys
# Redirect stdout and stderr to a file
#sys.stdout = open('output.log', 'w')
#sys.stderr = open('error.log', 'w')
'''BUILD a simple LLM application'''
import os
import groq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

groq_client=groq.Groq(api_key=GROQ_API_KEY)

#Create your model endpoint
sys_prompt='You are a helpful virtual assistant.\
      Your goal is to provide useful and relevant\
          responses to my query'
models=['llama-3.1-405b-reasoning',
        'llama-3.1-70b-versatile',
        'llama-3.1-8b-instant',
        'mixtral=8x7b-322768'

]
def generate(model,query,temperature):
    response=groq_client.chat.completions.create(
        model=model,
        messages=[
                  {'role':'system','content':sys_prompt},
                  {'role':'user','content':query}
        ],
        response_format={'type':'text'},
        temperature=temperature
    
    )
    answers=response.choices[0].message.content
    return answers
#generate(models[2],"Lionel Messi or Cristiano Ronaldo?",0.1)
#if this script is being run directly i.e not imported do:
if __name__ == "__main__":
    model = models[2]
    query = "Why did South Western Cameroun leave Nigeria?"
    #print(f'Your API key is {GROQ_API_KEY}')
    print(generate(model, query, temperature=0.91))
