def read_text():
    way_of_reading=int(input("Как вы хотите считать файл?(1 - целиком/2 - построчно): "))
    if way_of_reading==1:
        with open('example.txt', 'r') as file:
            content = file.read()
        print(content)
    else:
        with open('example.txt', 'r') as file:
            for line in file:
                print(line)

read_text()