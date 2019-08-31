
from flask import Flask,jsonify,request
from datetime import datetime
from api.api import exercise_temp
from model.model import *
import pickle
import json


@app.route('/')
def Show_Last_Time_Workout():
    ##在这里会展示上一次的锻炼数据
    #查询最后一次锻炼的时间
    time=Record.query.order_by(Record.act_time.desc()).first()

    #print(str(time.act_time).replace('00:00:00',''))
    #查询最后一次锻炼时间的记录
    times =str(time.act_time).replace('00:00:00','')
    print(times)
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
                result_json['action_name'][i.name].append([h.plan_time,h.act_time,h.action_id,h.weight])
    result={}
    result['data']=result_json
    return jsonify(result)
    #return json.dumps(result_json,ensure_ascii=False)


@app.route('/show_a_new_workout',methods=['GET'])
def Show_A_New_Workout():
    ##在这里会展示一次新的锻炼
    exercise_list=['胸','背','肩','手臂']
    time=Record.query.order_by(Record.act_time.desc()).first()
    times =str(time.act_time).replace('00:00:00','')
    print(times)
    last_workout = Regions.query.join(Action, Regions.id == Action.region_id).join(Record,Action.id == Record.action_id).filter(Record.act_time == times).all()
    p = exercise_list.index(last_workout[0].name)
    if(p<len(exercise_list)-1):
        p=p+1
    else:
        p=0
    today_workout = Action.query.join(Regions, Action.region_id == Regions.id).filter(Regions.name==exercise_list[p]).all()
    ###存在问题
    today_workout_number= Record.query.join(Action,Record.action_id == Action.id).filter(Record.act_time == times).all()
    ##exercise_list[p]:用于说明今天需要锻炼的部位
    ##today_workout:锻炼动作
    ##today_workout_number:锻炼动作的次数
    result ={}
    result['data']= exercise_temp(exercise_list[p],today_workout,today_workout_number)
    return jsonify(result)

##处理
@app.route('/save_workout_data',methods=['POST'])
def Save_Workout_Data():
    ##保存此次锻炼结果
    temps = request.get_json()
    print(temps)
    #组成新对象进行保存
    for key,value in temps['action_name'].items():
            action =Action.query.filter(Action.name == key).all()
            for l in value:
                temp=Record(l[0],l[1],action[0].id,l[2],l[3])
                db.session.add(temp)
    db.session.commit()
    db.session.close()
    return 'success to save a workout'




if __name__ == '__main__': 
    app.run()
