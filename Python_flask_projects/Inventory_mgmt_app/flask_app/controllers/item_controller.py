from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.item_model import Items

@app.route('/items/new')
def new_recipe_form():
    log_user = User.get_by_id({'id':session['user_id']})
    return render_template('new_sighting.html', log_user=log_user)


@app.route('/items/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Items.validator(request.form):
        return redirect('/items/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Items.create(data)
    return redirect('/dashboard')

@app.route('/items/<int:id>')
def one_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    this_item = Items.get_by_id({'id':id})
    log_user = User.get_by_id({'id':session['user_id']})

    return render_template('sighting_one.html', this_item=this_item, log_user=log_user)

@app.route('/items/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    this_item = Items.get_by_id({'id':id})
    log_user = User.get_by_id({'id':session['user_id']})
    return render_template("sighting_edit.html", this_item=this_item, log_user=log_user)
    
@app.route('/items/<int:id>/update', methods=['POST'])
def update_sighting(id):
    if not Items.validator(request.form):
        return redirect(f'/items/{id}/edit')
    item_data = {
        **request.form,
        'id':id
    }
    Items.update(item_data)
    return redirect('/dashboard')

@app.route('/items/<int:id>/delete')
def delete_recipe(id):
    Items.delete({'id':id})
    return redirect('/dashboard')
    
