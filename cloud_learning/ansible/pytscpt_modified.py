import subprocess

username = "amanu"
passwd = 'new123'

#task1= 'cd ansible'
task2 ='ansible-playbook adduser.yml --extra-vars "username=username passwd=passwd" '
subprocess.Popen(task2, shell=True)
        

