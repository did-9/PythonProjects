def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a {noun1} hwo like to {verb1}.
.....
And {noun2} is good at {verb2}
...
"""

print(story)

