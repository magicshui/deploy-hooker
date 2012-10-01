import flask
import os
import sys
from flaks import *

app = Flask(__name__)

app.debug = True


folder_temp = '/home/ubuntu/temp'
folder_vzi = '/var/www/vzi'



@app.route('/vzi',methods=['GET','POST'])
def route_index():
	os.popen('cd /var/www/vzi')
	os.popen('git pull')
	return 'done'
