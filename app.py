from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
print('sqlite:///' + os.path.join(basedir, 'data.sqlite'))


class Resource(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    state = db.Column(db.String)
    mailing_address = db.Column(db.String)
    zip_code = db.String(db.String)
    city_state = db.Column(db.String)
    phone = db.Column(db.String)
    site = db.Column(db.String)
    name = db.Column(db.String)
    other_resources = db.Column(db.String)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        value = request.get_json(force=True)
        value = value['state']
        resources = Resource.query.all()
        result = []
        for item in resources:
            
            name = item.state
            name_lst = name.split(' ')
            abbrev = ''
            for word in name_lst:
                abbrev += word[0]
            abbrev = abbrev.upper()
            
            if value == abbrev:
                result.append(item)
                break
        print(result)
        return render_template('index.html',result = len(result))
    print('here')
    return render_template('index.html',result=0)





if __name__=='__main__':
    manager.run()