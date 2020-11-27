from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Post(Model):
    id = AutoField(primary_key=True, unique=True)
    title = TextField(unique=True)
    date = DateField()
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE

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
            print("Post already exists")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    Post.create_post(
        'First Post', 
        '2020-11-26', 
        1, 
        'About Flask', 
        'Team Treehouse')
    DATABASE.close()