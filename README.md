# python-in-a-bottle
Experimental Flask/Python/Angular App

## Resources

* http://flask.pocoo.org/

* https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/#Dependencies

* https://medium.com/@balramchavan/angular-python-flask-full-stack-demo-27192b8de1a3

* http://flask.pocoo.org/docs/1.0/installation/

* http://flask.pocoo.org/docs/1.0/quickstart/

* https://github.com/ismtabo/sample-flask-angular/blob/master/sample-flask-angular/main.py

* https://linuxhint.com/install\_npm\_debian/

* https://www.npmjs.com/package/@angular/cli

* https://www.freecodecamp.org/news/learn-how-to-create-your-first-angular-app-in-20-min-146201d9b5a7/

## Snippets


    ng --version
    npm install --save-dev @angular/cli@latest
    ng --version

For everyone else getting stuck here, the correct update command now seems to be: npm install --save-dev @angular/cli@latest

    export FLASK_ENV=development
    flask run



    @app.route('/<path:path>', methods=['GET'])
    def static_proxy(path):
      return send_from_directory('./', path)
    
    
    @app.route('/')
    def root():
      return send_from_directory('./', 'index.html')

