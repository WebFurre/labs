def read_text():
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)

read_text()