def get_answers(question):
    answers={"hello":"Hey, dude!", "what's up?":"thee best", "bye":"see u"}
    return answers[question.lower()]

question=input("Ask yuor question?")
print(get_answers(question))
