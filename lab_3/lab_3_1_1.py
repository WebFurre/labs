def read_text():
    with open('example.txt', 'r') as file:
        content = file.read()
    print(content)
read_text()