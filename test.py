import openai
import urllib3

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": "How can i run a startup company?"},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ]
)

print(completion.choices[0].message)

# print(urllib3.__version__)