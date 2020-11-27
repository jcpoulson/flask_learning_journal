from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Post(Model):
    id = AutoField(primary_key=True, unique=True)
    title = TextField()
    date = DateField()
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    @classmethod
    def create_post(cls, title, date, time_spent, learned, resources):
        try:
            cls.create(
                title=title,
                date=date,
                time_spent=time_spent,
                learned=learned,
                resources=resources
            )
        except IntegrityError:
            raise ValueError("Post already exists")

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    Post.create_post(
        'First Post', 
        '11/26/2020', 
        2, 
        'About Flask', 
        'Team Treehouse')
    DATABASE.close()