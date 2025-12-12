#1. Дана строка. Подсчитать общее количество содержащихся в ней строчных 
# латинских и русских букв. 
# 2. Дана строка-предложение на русском языке. Подсчитать количество содержащихся 
# в строке знаков препинания.

#1
def count_lowercase_letters(text):
    try:
        if not isinstance(text, str):
            print("Ошибка: Входные данные должны быть строкой.")
            return 0
        
        count = 0
        
        for char in text:
            if char.islower():
                count += 1
                
        return count

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return 0


#2
def count_punctuation(sentence):
    try:
        if not isinstance(sentence, str):
            print("Ошибка: Входные данные должны быть строкой.")
            return 0
        punctuation_marks = '.,;:-?!()[]{}<>"\'/'
        count = 0
        for char in sentence:
            if char in punctuation_marks:
                count += 1
                
        return count

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return 0