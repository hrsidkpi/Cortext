def Student(username, password, id, first_name, last_name, school, agegroup):
    Student(username=username, password=password, id=id, first_name=first_name, last_name=last_name, school=school,
            agegroup=agegroup).save()


def Teacher(username, password, id, first_name, last_name):
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
    if user_id == "322780800" and password == "123":
        return True
    return False


def get_user(user_id):
    # user format: [user id, type(1=teacher, 2=student) name]
    return [user_id, "Jordan", 1]

def get_assignment(assignment_id):
    if assignment_id == '0':
        return [0, "Write your opinion about school uniform", "Batya", "21-12-2019", "2 days"]
    if assignment_id == '1':
        return [1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019", "7 days"]

def get_questions_assignment(assignment_id):
    if assignment_id == '0':
        return [
                "What is your opinion about school uniform?",
            ]
    if assignment_id == '1':
        return [
                "What does Dr. Cohen say the reason for World War I was?",
                "What does Dr. Cohen say can be done to prevent wars?",
                "What is your opinion about the article?",
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
                'jordan',
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
        