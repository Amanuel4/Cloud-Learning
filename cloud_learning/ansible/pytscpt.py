import subprocess

username="yabu"
passwd= 'new123'
with open(r'adduser.yml', 'r') as file:
    
    data = file.read()
    
    

data = data.replace('username', username)
data = data.replace('passwd', passwd)

with open(r'adduser.yml', 'w') as file:
    
    file.write(data)
    
task1= 'cd ansible'
task2 = 'ansible-playbook adduser.yml'
subprocess.Popen(task2, shell=True)
        

with open(r'adduser.yml', 'r') as file:

    data = file.read()



data = data.replace(username,'username')
data = data.replace(passwd,'passwd')

with open(r'adduser.yml', 'w') as file:

    file.write(data)
