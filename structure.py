
#Question 1

def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return not stack  


#Question 2

def remove_duplicates(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result


#Question 3
import string

def word_frequency(sentence):
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).lower()

    
    words = sentence.split()

    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict