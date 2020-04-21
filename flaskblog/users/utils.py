import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = secrets.token_hex(8) + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	
	i = Image.open(form_picture)
	w, h = i.size
	left, top, right, bottom = 0, 0, w, h
	if (w > h):
	  left = (w - h) / 2
	  right -= (w - h) / 2
	else:
	  top = (h - w) / 2
	  bottom -= (h - w) / 2
	i = i.crop((left, top, right, bottom))
	i.save(picture_path)

	return picture_fn


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='noreply10665@gmail.com', recipients=[user.email])
	msg.body = f'''To reset your password, go to the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this password reset request, ignore this email.
'''
	mail.send(msg)

