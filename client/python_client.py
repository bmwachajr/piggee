import requests
import json

microservice_url = 'http://localhost:8000/translate/pig_latin'

print('Welcome to the python piglatin cli client')
print("+++++++++++++++++++++++++++++++++++++++++")

print("Instructions: ")
instruction = input("Enter c to continue and q to quit: ")


while instruction.lower() == 'c':
    print('Enter the text to translate to pig latin: ')
    text = input()
    print("+++++++++++++++++++++++++++++++++++++++++")

    try:
        response = requests.post(
            microservice_url,
            data={'text': text}
        )

        translation = json.loads(response.content)
        print(translation['translation'])


    except Exception as e:
        breakpoint()
        print('Something went very wrong')

    print("+++++++++++++++++++++++++++++++++++++++++")
    instruction = input("Enter c to continue and q to quit: ")


print("Goodbye")