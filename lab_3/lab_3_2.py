def write_text():
    way_of_writing=int(input("Как вы хотите записать текст в файл?(1 - с нуля/2 - добавить): "))
    if way_of_writing==1:
        with open('user_input.txt', 'w') as file:
            text=input("Введите текст: ")
            file.write(text+'\n')
            print("Текст успешно записан)))")
    else:
        with open('user_input.txt', 'a') as file:
            text = input("Введите текст: ")
            file.write(text+'\n')
            print("Текст успешно записан)))")

write_text()