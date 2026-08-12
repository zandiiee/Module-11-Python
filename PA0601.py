import random

def creatingStudentRef():

    studentRef = "ST"
    for i in range(1,2):
        num = str(random.randint(1000, 9999))
        studentRef = studentRef + num
    return studentRef

ID = creatingStudentRef()
print(f'Student Reference :{ID}')

def creatingVerification():

    verify = ""
    for i in range(1,5):
        num = str(random.randint(1, 10))
        verify = verify + num
    return verify

VC = creatingVerification()
print(f'Verification Code: {VC}')
