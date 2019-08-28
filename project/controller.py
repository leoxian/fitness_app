
from flask import Flask
from datetime import datetime
#from tables import Regions
from flask_sqlalchemy import SQLAlchemy
import json

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


    def __init__(self,id,name)
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

    def __init__(self,id,name,region_id)
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


    def __init__(self,id,plan_time,act_time,action_id,quantity,weight)
        self.id = id
        self.plan_time = plan_time
        self.act_time = act_time
        self.action_id = action_id
        self.weight = weight

    def __repr__(self):
        #print(self.plan_time)
        return '<Record %r>'%self.action_id


@app.route('/')
def Show_Last_Time_Workout():
    ##在这里会展示上一次的锻炼数据
    #查询最后一次锻炼的时间
    time=Record.query.order_by(Record.act_time.desc()).first()
    #print(str(time.act_time).replace('00:00:00',''))
    #查询最后一次锻炼时间的记录
    times =str(time.act_time).replace('00:00:00','')
    workout_time_list=Record.query.filter(Record.act_time==times).all()
    #根据最后一次锻炼时间的action_id查出相应的action
    temp_set=set()
    for i in workout_time_list:
        temp_set.add(i.action_id)
    workout_list=[]
    for i in temp_set:
        workout_list.extend(Action.query.filter(Action.id==i).all())
        
    Region = Regions.query.filter(Regions.id==workout_list[0].region_id).first()
    #print(Region)
    result_json={'region_name':Region.name,'action_name':{}}
    for i in workout_list:
        result_json['action_name'][i.name]=[]
        for h in workout_time_list:
            if h.action_id ==i.id:
                print(h)
                result_json['action_name'][i.name].append(h)
    print(result_json)
    return 'hello world'
    #return json.dumps(result_json,ensure_ascii=False)


@app.route('/show_a_new_workout')
def Show_A_New_Workout():
    ##在这里会展示一次新的锻炼
    exercise_list=['胸','背','肩','手臂']
    time=Record.query.order_by(Record.act_time.desc()).first()
    times =str(time.act_time).replace('00:00:00','')
    last_workout = Regions.query.join(Action, Regions.id == Action.region_id).join(Record,Action.id == Record.action_id).filter(Record.act_time == times).all()
    p = exercise_list.index(last_workout[0].name)
    if(p<len(exercise_list)-1):
        p=p+1
    else:
        p=0
    today_workout = Action.query.join(Regions, Action.region_id == Regions.id).filter(Regions.name==exercise_list[p]).all()
    ###存在问题
    today_workout_number= Records.query.join(Action,Records.action_id == Action.id).filter(Record.act_time == times).all()

    exercise_temp(exercise_list[p],today_workout,today_workout_number)
    return 'hello world'


@app.route('./save_workout_data',method=['POST'])
def Save_Workout_Data():
#     ##保存此次锻炼结果
    temp = request.get_data()
    temps = json.loads(temp)

    ##组成新对象进行保存
    for i in temps['action_name']:
        #for h in i:











    return ''





if __name__ == '__main__': 
    app.run()

def exercise_temp(Region_name,Action,Action_number):
    result_json={'region_name':Region_name,'action_name':{}}
    for i in Action:
        result_json['action_name'][i.name]=[]
        for h in Action_number:
            if h.action_id ==i.id:
                result_json['action_name'][i.name].append(h)
            break
    return result_json
