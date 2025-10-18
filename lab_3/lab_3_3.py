def read_text():
    try:
        way_of_reading=int(input("Как вы хотите считать файл?(1 - целиком/2 - построчно): "))
        file_name = input("Введите название файла: ")
        if way_of_reading==1:
            with open(file_name, 'r') as file:
                content = file.read()
            print(content)
        else:
            with open(file_name, 'r') as file:
                for line in file:
                    print(line)

    except FileNotFoundError:
        print("Такого файла не существует, извините(")

read_text()