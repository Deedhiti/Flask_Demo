from flask import Flask
from DBConfig import DatabaseConfig
from Api import api, mysql
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MYSQL_HOST'] = DatabaseConfig().get_config()['localhost']
app.config['MYSQL_USER'] = DatabaseConfig().get_config()['root']
app.config['MYSQL_PASSWORD'] = DatabaseConfig().get_config()['aninditadey15@']
app.config['MYSQL_DB'] = DatabaseConfig().get_config()['employees']

mysql.init_app(app)

app.register_blueprint(api)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
