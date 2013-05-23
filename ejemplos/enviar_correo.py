#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

from email.message import Message
from smtplib import SMTP

gmail_user = 'tuusuario@gmail.com'
gmail_password = 'tu contraseña'

# Creamos el mensaje
msg = Message()
msg['to'] = 'euribates+test@gmail.com'
msg['from'] = 'euribates@gmail.com'
msg['subject'] = 'Esto es una prueba!'
msg.set_payload('Hola, mundo\n\n-- Juan')

# Lo enviamos
print('Enviando correo', end=' ')
smtpserver = SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
smtpserver.sendmail(gmail_user, msg['to'], msg.as_string())
smtpserver.close()
print('[OK]')