import prompt


def greetings_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def get_user_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer
