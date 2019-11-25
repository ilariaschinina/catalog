#activate_this = '/home/pooka/.local/share/virtualenvs/catalog-app.schinina.eu-jJb4-PyL/bin/activate'
#with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(1, '/var/www/catalog-app.schinina.eu')

from application import app as application
