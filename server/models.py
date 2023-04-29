from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('name')
    def validate_name(self, key, address):
        names = [author.name for author in Author.query.all()]
        if not address:
            raise ValueError("failed simple name validation")

        if address in names:
            raise ValueError("error validating")
        return address

    @validates('phone_number')
    def validate_number(self, key, address):
        if not len(address) == 10:
            raise ValueError("failed simple phone # validation")
        
        return address
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("No clickbait found")
        return title
    
    
    @validates('content')
    def validate_content(self, key, address):
        if len(address) < 250:
            raise ValueError("failed simple content validation")
        return address
    
    @validates('summary')
    def validate_summary(self, key, address):
        if len(address) >= 250:
            raise ValueError("failed simple  summary validation")
        return address
    
    @validates('category')
    def validate_category(self, key, address):
        if address not in ["Fiction", "Non-Fiction"]:
            raise ValueError("failed simplee category validation")
        return address




    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
