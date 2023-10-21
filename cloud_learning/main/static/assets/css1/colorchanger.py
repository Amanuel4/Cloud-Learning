
with open('style.css', 'r') as file:
    
    data = file.read()
    
    

data = data.replace('#ff9f43', '#32a84e')
print(data)

with open('style.css', 'w') as file:
    
    file.write(data)