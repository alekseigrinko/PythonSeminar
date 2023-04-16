answers = {
    'привет': 'Приветствую Вас, задайте свой вопрос, а я постараюсь найти на него ответ!',
    'зовут': 'Моё имя <Ответик>, рад с Вами познакомиться!',
    'имя': 'Моё имя <Ответик>, рад с Вами познакомиться!',
    'hi': 'Приветствую Вас, задайте свой вопрос, а я постараюсь найти на него ответ!',
    'name': 'Моё имя <Ответик>, рад с Вами познакомиться!'
}

def getAnswer (question: str, answers: dict):
    keys = question.split()
    options = []
    for k in keys:
        for a in answers.keys():
            if k.lower() == a.lower():
                options.append(answers.get(a))
    if len(options) == 0:
        print('Я пока не знаю ответа на такой вопрос, задайте вопрос еще раз!')
        x = input('Нажмите 1, чтобы научить меня давать ответ на данный вопрос, или <Enter> для продолжения для продолжения: ')
        if x == '1':
            newKey = input('Введите ключ-слово вопроса для поиска на него ответа, оно должно состоять из одного слова: ')
            newValue = input('Какой ответ на это ключ-слово я должен дать?: ')
            answers[newKey] = newValue
            return answers
    else:
        print('/n'.join(options))
        return answers

key = True
while key:
    question = str(input("Введите вопрос либо 0 для выхода: "))
    if question == '0':
        key = False
    else:
        answers = getAnswer(question, answers)