from flaskr.__init__ import create_app
app = create_app()
if __name__ == "__main__": 
    print(app.secret_key)
    app.run()
