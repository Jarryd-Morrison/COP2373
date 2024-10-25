import re

def split_into_sentences(text):
    sentences = []
    sentence = ""
    
    for i, char in enumerate(text):
        sentence += char  # Accumulate characters in the current sentence
        
        # Check for end of sentence markers (., ?, !) followed by either whitespace or uppercase
        if char in ".!?" and (i + 1 < len(text) and (text[i + 1] == " " or text[i + 1].isupper())):
            sentences.append(sentence.strip())
            sentence = ""  # Reset for the next sentence
    
    # Append any remaining text as a sentence if not empty
    if sentence:
        sentences.append(sentence.strip())
    
    return sentences

def display_sentences_with_count(sentences):
    print("\nThe sentences are:\n")
    for idx, sentence in enumerate(sentences, start=1):
        print(f"{idx}. {sentence}")
    
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    print("Enter text to analyze:")
    text = input()
    sentences = split_into_sentences(text)
    display_sentences_with_count(sentences)

main()
