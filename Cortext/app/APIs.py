# from Cortext.app.models import *
from .models import *

def student(username, password, id, first_name, last_name, school, agegroup):
    Student(username=username, password=password, id=id, first_name=first_name, last_name=last_name, school=school,
            agegroup=agegroup).save()


def teacher(username, password, id, first_name, last_name):
    Teacher(username=username, password=password, id=id, first_name=first_name, last_name=last_name).save()


def get_assignments_user(user_id):
    # assignment format:  [assignment id, name, teacher name, due date]
    # input: user id
    return [
        [0, "Write your opinion about school uniform", "Batya", "21-12-2019", "2 days"],
        [1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019", "7 days"],
    ]


# Return true if the user_id and password match and false if not
def attempt_login(user_id, password):
    student = Student.objects.filter(pk=user_id, password=password)
    if len(student) == 1:
        return True
    teacher = Teacher.objects.filter(pk=user_id, password=password)
    if len(teacher) == 1:
        return True
    return False


def get_user(user_id):
    # user format: [user id, name, type(1=teacher, 2=student)]
    details = []
    student = Student.objects.filter(pk=user_id)
    if len(student) == 1:
        student = student[0]
        details.append(user_id)
        details.append(student.first_name)
        details.append(2)
    teacher = Teacher.objects.filter(pk=user_id)
    if len(teacher) == 1:
        teacher = teacher[0]
        details.append(user_id)
        details.append(teacher.first_name)
        details.append(1)
    return details

def get_current_user():
    # like get_user, but return the current user that is logged in. Return None if 
    # not currently logged in.
    return get_user(0)

def is_connected():
    return get_user() != None

def get_assignment(assignment_id):
    if assignment_id == '0':
        return [0, "Write your opinion about school uniform", "Batya", "21-12-2019", "2 days"]
    if assignment_id == '1':
        return [1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019", "7 days"]

def get_questions_assignment(assignment_id):
    if assignment_id == '0':
        return [
                [0,"What is your opinion about school uniform?"],
            ]
    if assignment_id == '1':
        return [
                [1,"What does Dr. Cohen say the reason for World War I was?"],
                [2,"What does Dr. Cohen say can be done to prevent wars?"],
                [3,"What is your opinion about the article?"],
            ]

def get_classes_teacher(teacher_id):
    return [
            
            [0, "ז4", [
                [0, "Write your opinion about school uniform", "21-12-2019"],
                [2, "this question doesn't actually exist don't click it", "00-00-0000"]
            ]],
            [1, "ו5", [
                [1, "Summerize Dr. Cohen's article", "26-12-2019"]
            ]]
            
        ]

def get_submissions_assignment(assignment_id):
    if assignment_id == '0':
        return [
                [2,
                'Jordan',
                '20-12-2019',
                [
                    "my opinions is that school uniforms are good"    
                ]]
            ]
    if assignment_id == '1':
        return [
                [0,
                'Jordan',
                '20-12-2019',
                [
                    'He says the reason is capitalism',
                    'He says we need socialism',
                    'My opinion is that the article is wrong, capitalism is good',
                ]],
                [1,
                'Amit',
                '22-12-2019',
                [
                    'I don\'t know',
                    'He says rich people are evil or something',
                    'I don\'t have opinions on things',
                ]]
            ]


def get_assignment_submission(submissionid):
    if submissionid == '0':
        return ['1',  "Summerize Dr. Cohen's article", "26-12-2019"]
    if submissionid == '1':
        return ['1', "Summerize Dr. Cohen's article", "26-12-2019"]
    if submissionid == '2':
        return ['0', "Write your opinion about school uniform"]

def get_submission(submissionid):
    if submissionid == '0':
        return [0,
                'Jordan',
                '20-12-2019',
                [
                    'He says the reason is capitalism',
                    'He says we need socialism',
                    'My opinion is that the article is wrong, capitalism is good',
                ]]
    if submissionid == '1':
        return [1,
                'Amit',
                '22-12-2019',
                [
                    'I don\'t know',
                    'He says rich people are evil or something',
                    'I don\'t have opinions on things',
                ]]

    if submissionid == '2':
        return [2,
                'Jordan',
                '20-12-2019',
                [
                    "my opinions is that school uniforms are good"    
                ]]

