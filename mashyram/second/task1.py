"""
Вивести всі великі літери
"""

print ("Введіть текст")
S = input()
word = [S.split( )]
upperletters = [i for i in word if i.isupper()]
print(upperletters)