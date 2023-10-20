from app import app, db
from app.models import User, Post


# Add database instance and models to a flask shell session
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)
