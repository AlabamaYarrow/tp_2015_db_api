from app import app
from flask import g, request, jsonify

def executeQuery(query):
	cur = g.db_conn.cursor()
	cur.execute(query)
	g.db_conn.commit()
	return cur


@app.route('/')
@app.route('/db/api')
def index():
	return 'Welcome to DB api!'


@app.route('/db/api/clear')
def clear():	
	query = 'TRUNCATE TABLE forum'
	executeQuery(query)	
	return jsonify (code = 0, response = 'OK')


############
#forum

@app.route('/db/api/forum/create')
def forumCreate():	
	name = request.args.get('name')
	short_name = request.args.get('short_name')
	user = request.args.get('user')	

	if not name or not short_name or not user:
		return jsonify(code = 3, response = 'Missing parameters')
	query = "INSERT INTO forum (name, short_name, user) \
			 VALUES ('%s', '%s', '%s')" \
			 % (name, short_name, user) 
	cur = executeQuery(query)
	
	return	jsonify(code = 0,	response = dict(
									id = cur.lastrowid,	
									name = name, 
									short_name = short_name, 
									user = user
								))


@app.route('/db/api/forum/details')
def forumDetails():
	forum = request.args.get('forum')	
	if not forum:
		return jsonify(code=3, response='Forum not specified')
	related = request.args.getlist('related')
	user = 0
	'''
	if 'user' in related:
		user = 1

	if user:
		query = ""
	else:
		query = ""
	'''
	#query = ''
	return 'ok'
