import os
import json
from dotenv import load_dotenv
import openai

class Copilot:

    def clear_text(self, text):
        a = text
        b = a.split()
        c = " ".join(b)

        return c

    def get_answer(self, question):
        prompt = question
        
        load_dotenv()

        openai.api_key = "PASTE YOUR OPEN AI API"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )

        json_object = response

        # Convert the JSON object to a JSON string
        json_string = json.dumps(json_object)

        # Parse the JSON string using json.loads()
        parsed_json = json.loads(json_string)

        text = parsed_json['choices'][0]['text']
        cleared_text = self.clear_text(text)
        # cleared_text = response.choices[0].text
        return text
        # return response.choices[0].text
    
copilot = Copilot()
a = copilot.get_answer("Напиши функцию на C++ для обхода графа в ширину")
print(a)
