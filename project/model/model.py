from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SECRET_KEY']='a19830614'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:a19830614@120.55.60.84:3306/fitness' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db =SQLAlchemy(app)


##部位
class Regions(db.Model):
    __tablename__ = 'region'
    id = db.Column('id',db.Integer,primary_key=True)
    name =db.Column('name',db.String(32))

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        #print(self.name)
        return '<Regin %r>'%self.name

##动作

class Action(db.Model):
    __tablename__ ='action'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(32))
    region_id =db.Column('region_id',db.Integer,db.ForeignKey('regions.id'))

    def __init__(self,id,name,region_id):
        self.id = id
        self.name = name
        self.region_id = region_id


    def __repr__(self):
        print(self.name)
        return '<Action %r>'%self.name



#记录
class Record(db.Model):
    __tablename__ ='record'
    id = db.Column('id',db.Integer,primary_key=True)
    plan_time=db.Column('plan_time',db.String(32))
    act_time=db.Column('act_time',db.String(32))
    #table名字
    action_id=db.Column('action_id',db.Integer,db.ForeignKey('action.id'))
    quantity=db.Column('quantity',db.Integer)
    weight=db.Column('weight',db.Integer)


    def __init__(self,plan_time,act_time,action_id,quantity,weight):
        self.plan_time = plan_time
        self.act_time = act_time
        self.action_id = action_id
        self.quantity = quantity
        self.weight = weight

    def __repr__(self):
        #print(self.plan_time)
        return '<Record %r>'%self.action_id
