"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for
from .forms import PropertyForm
from .models import Property
from werkzeug.utils import secure_filename
import os
from flask import flash
from app.models import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")



@app.route('/properties/create', methods=['GET', 'POST'])
def NewProperty():
    form = PropertyForm()
    if form.validate_on_submit():
        filename = None
        if form.photo.data:
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
        property = Property(
            title=form.title.data,
            property_type=form.property_type.data,
            num_bedrooms=form.num_bedrooms.data,
            num_bathrooms=form.num_bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            description=form.description.data,
            photo=filename
        )
        db.session.add(property)
        db.session.commit()
        flash('Property added successfully', 'success')
        return redirect(url_for('home'))
    return render_template('NewProperty.html', form=form)

@app.route('/properties')
def properties():
    all_properties = Property.query.all()
    return render_template('Properties.html', properties=all_properties)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
