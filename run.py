from flaskblog import create_app

app = create_app() # default config

if __name__ == '__main__':
	app.run(debug=True)