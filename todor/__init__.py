from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)

    # Project configuration
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'developer',
        SQLALCHEMY_DATABASE_URI='sqlite:///todolist.db'
    )
    
    db.init_app(app)
    
    # Register Blueprint
    from . import todo
    app.register_blueprint(todo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    # Normal Routes
    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()
    
    return app
