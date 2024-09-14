# List of 30 common spam words/phrases
spam_keywords = [
    "free", "win", "winner", "cash", "prize", "limited time", "urgent", 
    "exclusive deal", "click here", "congratulations", "act now", "guarantee",
    "risk-free", "investment", "double your income", "no credit check", 
    "claim your prize", "amazing", "unlimited", "no obligation", "trial",
    "promise", "as seen on", "call now", "instant", "earn money", "credit card",
    "luxury", "confidential", "get rich", "refinance"
]

def calculate_spam_score(message):
    # Initialize the score and an empty list for triggering words
    spam_score = 0
    triggering_words = []

    # Convert the message to lowercase to make the search case-insensitive
    message_lower = message.lower()

    # Check for each spam keyword/phrase in the message
    for keyword in spam_keywords:
        if keyword in message_lower:
            spam_score += 1
            triggering_words.append(keyword)
    
    return spam_score, triggering_words

def spam_likelihood(spam_score):
    # Adjusted likelihood based on the actual spam score
    if spam_score == 0:
        return "Very Unlikely"
    elif spam_score <= 2:
        return "Unlikely"
    elif spam_score <= 5:
        return "Possible"
    elif spam_score <= 8:
        return "Likely"
    else:
        return "Very Likely"

def main():
    # Prompt user to enter an email message
    user_message = input("Enter an email message: ")

    # Calculate the spam score and the triggering spam words/phrases
    spam_score, triggering_words = calculate_spam_score(user_message)

    # Get the likelihood of the message being spam
    likelihood = spam_likelihood(spam_score)

    # Display the spam score and likelihood
    print("\nSpam Analysis Report:")
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood of being spam: {likelihood}")

    # Display the spam-causing words or phrases if any were found
    if triggering_words:
        print("\nThe following words/phrases triggered the spam score:")
        print(", ".join(triggering_words))
    else:
        print("\nNo suspicious spam words/phrases were found.")

if __name__ == "__main__":
    main()
