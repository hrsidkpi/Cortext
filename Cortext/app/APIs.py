
def get_assignments_user(user_id):
	# assignment format:  [assignment id, name, teacher name, due date]
	# input: user id
	return [
		[0, "Write your opinion about school uniform", "Batya", "21-12-2019"],
		[1, "Summerize Dr. Cohen's article", "Batya", "26-12-2019"],

	]

# Return true if the user_id and password match and false if not
def attempt_login(user_id, password):
	if user_id == "322780800" and password == "123":
		return True
	return False

def get_user(user_id):
	# user format: [user id, name]
	return [user_id, name]