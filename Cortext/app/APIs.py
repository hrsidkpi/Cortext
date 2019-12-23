# from Cortext.app.models import *
from .models import *

def create_student( id, password,first_name, last_name, school, agegroup):
    Student(password=password, id=id, first_name=first_name, last_name=last_name, school=school,
            agegroup=agegroup).save()


def create_teacher(id,password,  first_name, last_name):
    Teacher(password=password, id=id, first_name=first_name, last_name=last_name).save()


# return weather the user id is already registered
def user_exists(user_id):
    return True

def get_assignments_user(user_id):
    # assignment format:  [assignment id, name, teacher name, due date]
    # input: user id
    return [
        [0, "Write your opinion about school uniform", "Batya", "21-12-2019", "2 days"],
        [1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019", "7 days"],
    ]


# Return true if the user_id and password match and false if not
# if login successful, remember the logged in user (in session).
# get_current_user() should work after this.
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
    return get_user(5)

# Already implemented, no need to change
def is_connected():
    return get_user() != None

# get data on assignment from assignment id
def get_assignment(assignment_id):
        # format: [assignment_id, title, teacher name, due date, time left (formatted for printing)]
    if assignment_id == '0':
        return [0, "Write your opinion about school uniform", "Batya", "21-12-2019", "2 days"]
    if assignment_id == '1':
        return [1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019", "7 days"]

# Get a list of questions for the assignment id
def get_questions_assignment(assignment_id):
    # format:[  [question_id, question_text] , ...  ]
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


# get assignments grouped by class for a teacher id
def get_classes_teacher(teacher_id):

    # class format: [class_id, class_name, [assignment 1, assignment 2, ...]]
    # assignment format: [assignment id, title, due date]

    return [
            
            [0, "ז4", [
                [0, "Write your opinion about school uniform", "21-12-2019"],
                [2, "this question doesn't actually exist don't click it", "00-00-0000"]
            ]],
            [1, "ו5", [
                [1, "Summerize Dr. Cohen's article", "26-12-2019"]
            ]]
            
        ]

# get all submissions for an assignment
def get_submissions_assignment(assignment_id):
    # submission format: [submission_id, submitting student name, submission date, list of answers]

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


# get assignment from a submission id
def get_assignment_submission(submissionid):
    # assignment format: [id, title, due date]
    if submissionid == '0':
        return ['1',  "Summerize Dr. Cohen's article", "26-12-2019"]
    if submissionid == '1':
        return ['1', "Summerize Dr. Cohen's article", "26-12-2019"]
    if submissionid == '2':
        return ['0', "Write your opinion about school uniform", "12-12-1212"]

# get a submission from submission id
def get_submission(submissionid):
    #submission format: [id, student name, submission date, list of answers]
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


def logout():
    pass
    #Remove the current user from the session

