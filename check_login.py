from templates.config import conn

cur = conn.cursor()
def is_null(username,password):
	if(username==''or password==''):
		return True
	else:
		return False

def is_existed(username,password,teacher_is):
	sql="SELECT * FROM user WHERE username ='%s' and password ='%s' and teacher_is='%s'" %(username,password,teacher_is)
	conn.ping(reconnect=True)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

def exist_user(username):
	sql = "SELECT * FROM user WHERE username ='%s'" % (username)
	conn.ping(reconnect=True)
	cur.execute(sql)
	conn.commit()
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

