with open('practice.txt', 'r') as file:
    data = file.read()

new_data = data.replace('Python' ,"java")
print(new_data)