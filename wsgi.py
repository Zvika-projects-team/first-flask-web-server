from flaskr.__init__ import create_app

if __name__ == "__main__": 
    app = create_app()   
    print(app.secret_key)
    app.run()
