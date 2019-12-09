from models import *

def get_assignments_user(user_id):
	# assignment format:  [assignment id, name, teacher name, due date]
	# input: user id
	return [[0, "Write your opinion about school uniform", "Batya", "21-12-2019"]]

def get_user(user_id):
	return Student(id=user_id, name='Batya')