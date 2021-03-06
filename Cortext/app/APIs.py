# from Cortext.app.models import *
from .models import *
import datetime

current_request = None

def set_request(request):
    global current_request
    current_request = request

def create_student(id, password, first_name, last_name, school, agegroup):
    Student(password=password, id=id, first_name=first_name, last_name=last_name, school=school,
            agegroup=agegroup).save()


def create_teacher(id, password, first_name, last_name):
    teacher_object = Teacher.objects.filter(id=id)
    if len(teacher_object) == 0:
        Teacher(password=password, id=id, first_name=first_name, last_name=last_name).save()
    raise Exception("Teacher already exits")

def create_school(id, name, password):
    School(password=password, name=name, id=id).save()
#f
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
        current_request.session['username'] = user_id
        return True
    teacher = Teacher.objects.filter(pk=user_id, password=password)
    if len(teacher) == 1:
        current_request.session['username'] = user_id
        return True
    school = Teacher.objects.filter(pk=user_id, password=password)
    if len(school) == 1:
        current_request.session['username'] = user_id
        return True
    return False


def get_user(user_id):
    # user format: [user id, name, type(1=teacher, 2=student)]
    details = []
    student = Student.objects.filter(pk=user_id)
    if len(student) == 1:
        student = student[0]
        details.append(user_id)
        details.append(str(student))
        details.append(2)
    teacher = Teacher.objects.filter(pk=user_id)
    if len(teacher) == 1:
        teacher = teacher[0]
        details.append(user_id)
        details.append(str(teacher))
        details.append(1)
    #TODO- get admins too. admins should have 1 more field in their details, their school id
    # [id, name, 3, scool_id]

    return details if len(details) != 0 else None


def get_current_user():
    # like get_user, but return the current user that is logged in. Return None if 
    # not currently logged in.

    return get_user(current_request.session['username'])


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
    if questions:
        return [[q.question_id, q.content] for q in questions]
    return None


# get assignments grouped by class for a teacher id
def get_class_name(class_id):
    #int_to_letters = {"01": "א", "02": "ב", "03": "ג", "04": "ד", "05": "ה", "06": "ו", "07": "ז", "08": "ח", "09": "ט",
    #                  "10": "י", "11": "יא", "12": "יב", "22": "יב"}
    #class_number = class_id[-1] if class_id[8] == '0' else class_id[8:10]
    #return int_to_letters[class_id[6:8]] + class_number
    return "ג4"


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
    a = assignments(teacher_id=get_current_user()[0], description=title, due_date=due_date)
    a.save()
    assignment_class(assignment_id=a.assignment_id, class_id='0').save()
    for q in questions:
        Question(assignment_id=a.assignment_id, content=q).save()
    all_students=Student.objects.all()
    for s in all_students:
        sub = Submission(student_id=s.id, assignment_id=a.assignment_id)
        sub.save()
        for q in Question.objects.filter(assignment_id=sub.assignment_id):
            Answers(submission_id=sub.submission_id, question_id=q.question_id, content="").save()

# Disconnect the current user (remove from session).
def logout_current_user():
    current_request.session['username'] = None


# Create a submission for the assignment with the given answers.
def create_submission(assignment, answers):
    pass


# Save the new answers to the submission.
#mark
def change_answers(submission, answers):
    s = Submission.objects.filter(pk=submission)[0]
    dbans = Answers.objects.filter(submission_id=submission)
    for i in range(len(answers)):
        Answers.objects.filter(pk=dbans[i].pk).update(content=answers[i])
        dbans[i].save()
    pass

def get_submission_student(assignment_id):
    curr_student = get_current_user()
    curr_submission = Submission.objects.filter(assignment_id=assignment_id, student_id=curr_student[0])[0]
    res = get_submission(curr_submission.submission_id)
    res.remove(curr_student[1])
    return  res
    # [submissionid, sub_date, answers]
    # return current student submission for that assignment


# Get array of teachers belonging to the school.
# Array of users, each format like get_user() format.
def get_teachers_school(school_id):
    #gets all school classes id
    school_classes = [cls.id for cls in Class.objects.filter(school_id = school_id)]
    teachers_id = []
    all_teachers = []
    for c in school_classes:
        #Gets all teacher id_s of specific class
        teachers_id = [t.teacher_id for t in teacher_class.objects.filter(class_id=c)]
    #requires a merge of similar teachers id
    teachers_id = list(set(teachers_id))
    for i in teachers_id:
        all_teachers.append(get_user(i))
    return all_teachers


def get_students_school(school_id):
    #gets all school classes id
    school_classes = [cls.id for cls in Class.objects.filter(school_id = school_id)]
    students_id = []
    all_students = []
    for c in school_classes:
        #Gets all studentsid_ of specific class
        students_id = [s.student_id for s in class_student.objects.filter(class_id=c)]
    #requires a merge of similar teachers id
    students_id = list(set(students_id))
    for i in students_id:
        all_students.append(get_user(i))
    return all_students





# Set the teachers of the school to all the teachers in the array teachers.
# Some of the teachers in the array may already be in the database, 
# so this function needs to check it and not add them if that is the case.
# The teacher format is:
# [id, name]
# OR
# [id, name, password].
# If the former is used, don't change the teacher's password.
# If the later is used, change the teacher's password to the given password.
def set_teachers_school(school_id, teachers):
    for teacher in teachers:
        tmp_id = teacher[0]
        teacher_object = Teacher.objects.filter(id=tmp_id)
        if len(teacher_object) == 0:
            first_name, last_name = teacher[1].split()
            create_teacher(tmp_id, teacher[2], first_name, last_name)
            teacher_school(school_id=school_id, teacher_id=tmp_id).save()
        else:
            if len(teacher) == 3:
                teacher_object.update(password=teacher[2])
            if len(teacher_school.objects.filter(teacher_id=tmp_id)) == 0:
                teacher_school(school_id=school_id, teacher_id=tmp_id).save()

def set_students_school(school_id, students):
    for student in students:
        tmp_id = student[0]
        student_object = Student.objects.filter(id=tmp_id)
        if len(student_object) == 0:
            first_name, last_name = student[1].split()
            create_student(tmp_id, student[2], first_name, last_name)
            student_school(school_id=school_id, teacher_id=tmp_id).save()
        else:
            if len(student) == 3:
                student_object.update(password=student[2])
            if len(student_school.objects.filter(student_id=tmp_id)) == 0:
                student_school(school_id=school_id, teacher_id=tmp_id).save()


