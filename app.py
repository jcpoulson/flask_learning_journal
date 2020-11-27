import models
import form

from flask import Flask, render_template, url_for, redirect, g

app = Flask(__name__)
app.secret_key = 'sknvns-vo w-nvpoenovwenovwpovn s'


@app.before_request
def before_request():
    """connnect to the database"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """close the connection to the database"""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries')
def index():
    posts = models.Post.select().order_by(models.Post.id.desc())
    return render_template('index.html', posts=posts)


@app.route('/entries/new', methods=["GET", "POST"])
def new():
    """initialize the post form and 
    create a post from the given data on the form"""
    post = form.PostForm()
    if post.validate_on_submit():
        models.Post.create_post(
            title=post.title.data,
            date=post.date.data,
            time_spent=post.time_spent.data,
            learned=post.learned.data,
            resources=post.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', postForm=post)


@app.route('/entries/<int:id>')
def detail(id):
    """Select the post by ID and display it to the screen"""
    post = models.Post.select().where(models.Post.id == id).get()
    return render_template('detail.html', post=post)


@app.route('/entries/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    """initialize the postForm and 
    update the current form with that new form data"""
    postForm = form.PostForm()
    if postForm.validate_on_submit():
        post = models.Post.select().where(models.Post.id == id).get()
        post.title = postForm.title.data
        post.date = postForm.date.data
        post.time_spent = postForm.time_spent.data
        post.learned = postForm.learned.data
        post.resources = postForm.resources.data
        post.save()
        return redirect(url_for('index'))
    return render_template('edit.html', postForm=postForm)


@app.route('/entries/<int:id>/delete')
def delete(id):
    """Grab the current post by ID and delete the instance of that post"""
    post_to_delete = models.Post.select().where(models.Post.id == id).get()
    post_to_delete.delete_instance()
    return redirect(url_for('index'))

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=5500, host=0.0)
