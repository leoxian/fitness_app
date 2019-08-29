
def exercise_temp(Region_name,Action,Action_number):
    result_json={'region_name':Region_name,'action_name':{}}
    for i in Action:
        result_json['action_name'][i.name]=[]
        for h in Action_number:
            if h.action_id ==i.id:
                result_json['action_name'][i.name].append(h)
            break
    return result_json