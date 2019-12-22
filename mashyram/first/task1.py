"""
Вхідні дані:  -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-);
Результат: список слів (у нижньому регістрі), що містить кожне друге слово та кількість його повторів
Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Виклик функції: find_most_frequent('Hello, Hello, my dear Mom! I want play and play and football')
Повертає: [ [Hello,2] , [dear,1] , [I,1] , [play,2] ,[ football,1] ]
"""

import re

re_text = re.compile("^\w*\s*\,*\.*\:*\;*\!*\?*\-*$")

def validator(pattern, prompt):
    text  = input(prompt)
    while not bool(pattern.match(text)):
        text = input(prompt)
    return text


def find_most_frequent(promt):
    task = str(validator(re_text(promt)))
    return task

string = validator("Enter string: ")

for i in string:
    list = [ ]