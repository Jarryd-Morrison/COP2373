#imports the text file with the responses.
import random

#defines the variable get_random_responses and states where to get it from.
def get_random_response(file_path='random.txt'):
    try:
        # Open the file and read all lines into a list
        with open(file_path, 'r') as file:
            responses = file.readlines()

        # Returns a random response
        return random.choice(responses)
    except FileNotFoundError:
        return "The file 'random.txt' was not found."

#Asks the user for a yes or no question.
while True:
       question = input("Ask the magical 8 Ball a question (type 'exit' to quit): ")
       #If response is exit then the loop breaks
       if question == 'exit':
           print("Goodbye!")
           break
       #if the response is not exit, gets random answer from txt file and prints it.
       else:
           random_response = get_random_response()
           print(random_response)
           


    

