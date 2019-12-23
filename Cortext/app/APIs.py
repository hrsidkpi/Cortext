# from Cortext.app.models import *
from .models import *
import datetime


def create_student(id, password, first_name, last_name, school, agegroup):
    Student(password=password, id=id, first_name=first_name, last_name=last_name, school=school,
            agegroup=agegroup).save()


def create_teacher(id, password, first_name, last_name):
    Teacher(password=password, id=id, first_name=first_name, last_name=last_name).save()


# return weather the user id is already registered
def user_exists(user_id):
    return len(Student.objects.filter(pk=user_id)) == 1


def get_assignments_user(user_id):
    # assignment format:  [assignment id, name, teacher name, due date]
    # input: user id
    ret = []
    subs = Submission.objects.filter(student_id=user_id)
    all_assignments = [sub.assignment_id for sub in subs]
    for assignment_id in all_assignments:
        ret.append(get_assignment(assignment_id))
    return ret


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

    #return get_user(322780800)
    return get_user(234567890)


# Already implemented, no need to change
def is_connected():
    return get_current_user() != None


# get data on assignment from assignment id
# format: [assignment_id, title, teacher name, due date, time left (formatted for printing)]
def get_assignment(assignment_id):
    curr_assignment = assignments.objects.filter(pk=assignment_id)
    if len(curr_assignment) == 0:
        return None
    curr_assignment = curr_assignment[0]
    curr_teacher = Teacher.objects.filter(pk=curr_assignment.teacher_id)[0]
    today = datetime.date.today()
    diff = curr_assignment.due_date.date() - today
    days = diff.days
    return [assignment_id, curr_assignment.description, str(curr_teacher),
            curr_assignment.due_date.strftime("%d/%m/%Y, %H:%M:%S"),
            str(days) + " days"]


# Get a list of questions for the assignment id
# format:[  [question_id, question_text] , ...  ]
def get_questions_assignment(assignment_id):
    questions = Question.objects.filter(assignment_id=assignment_id)
    return [[q.question_id, q.content] for q in questions]


# get assignments grouped by class for a teacher id
def get_class_name(class_id):
    int_to_letters = {"01": "א", "02": "ב", "03": "ג", "04": "ד", "05": "ה", "06": "ו", "07": "ז", "08": "ח", "09": "ט",
                      "10": "י", "11": "יא", "12": "יב"}
    class_number = class_id[-1] if class_id[8] == '0' else class_id[8:10]
    return int_to_letters[class_id[6:8]] + class_number


def get_classes_teacher(teacher_id):
    # class format: [class_id, class_name, [assignment 1, assignment 2, ...]]
    # assignment format: [assignment id, title, due date]
    teacher_classes = teacher_class.objects.filter(teacher_id=teacher_id)
    ret = []
    for c in teacher_classes:
        new_class = [c.class_id, get_class_name(c.class_id)]
        assignments = assignment_class.objects.filter(class_id=c.class_id)
        assignments_ids = [assignment.assignment_id for assignment in assignments]
        assignments_list = [get_assignment(assignment_id)[0:2] + [get_assignment(assignment_id)[3]] for assignment_id in
                            assignments_ids]
        new_class.append(assignments_list)
        ret.append(new_class)
    return ret


# get all submissions for an assignment
def get_submissions_assignment(assignment_id):
    # submission format: [submission_id, submitting student name, submission date, list of answers]

    submissions = Submission.objects.filter(assignment_id=assignment_id)
    return [get_submission(s.submission_id) for s in submissions]


# get assignment from a submission id
# assignment format: [assignment_id, title, due date]
def get_assignment_submission(submissionid):
    submission = Submission.objects.filter(pk=submissionid)[0]
    assignment = assignments.objects.filter(pk=submission.assignment_id)[0]
    return [assignment.assignment_id, assignment.description, assignment.due_date]


# get a submission from submission id
def get_submission(submissionid):
    submission = Submission.objects.filter(pk=submissionid)[0]
    sub_student = Student.objects.filter(pk=submission.student_id)[0]
    answers = Answers.objects.filter(submission_id=submissionid)
    answers = [a.content for a in answers]
    sub_date = submission.sub_date
    return [submissionid, str(sub_student), sub_date, answers]


# Create a new assignment with the title due_date and questions.
# title is a string, due_date is a stirng, questions is an array of strings.
def create_assignment(title, due_date, questions):
    pass

# Disconnect the current user (remove from session).
def logout():
    pass

# Create a submission for the assignment with the given answers.
def create_submission(assignment, answers):
    pass

# Save the new answers to the submission.
def change_answers(submission, answers):
    pass