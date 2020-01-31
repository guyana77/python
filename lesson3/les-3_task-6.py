# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(string):
    result = string.capitalize()
    return result


print(int_func('привет'))


def allcap_func(string):
    string = string.split()
    new_string = []
    for item in string:
        new_string.append(int_func(item))
    return ' '.join(new_string)


print(allcap_func('Привет, как дела?'))
