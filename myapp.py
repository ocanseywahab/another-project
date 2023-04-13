# Create a welcoming messsage for a student MIS web 
from getpass import getpass 
student_fullName = input('Enter your full name: ')
student_id = int(getpass('Enter your student ID: '))
student_pin = int(input('Enter your pin: '))
print(f'Welcome to MIS, {student_id}')
print(f'Mr.{student_fullName}, you have successfully logged into your MIS\n How can we be of help?')