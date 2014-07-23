from peewee import *

db = SqliteDatabase('blog.db')


class Author(Model):
	name = CharField(null = False)	
	email = CharField(null = False, unique=True)
	

class Post(Model):
	id = IntgerField(null = False, unique = True)
	message  = TextField(null = False)
	author = ForeignKeyField(User, related_name='post')
	
