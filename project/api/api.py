
def exercise_temp(Region_name,Action,Action_number):
    result_json={'region_name':Region_name,'action_name':{}}
    temp_dic ={}
    for i in Action_number:
        if i.action_id not in temp_dic:
            temp_dic[i.action_id] = []
        else:
            temp_dic[i.action_id].append([i.quantity,i.weight])
            print(temp_dic[i.action_id])

    for l in Action:
        print('i.name={}'.format(l.name))
        print('i.id={}'.format(l.id))
        if l.id in temp_dic:
            result_json['action_name'][l.name]=temp_dic[l.id][0]
    return result_json