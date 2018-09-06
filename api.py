from flask import Flask,jsonify,request,json
import uuid

app=Flask('__name__')

all_users_list= []
answers=[]

@app.route('/api/add_user',methods=['POST'])
def  add_a_user():  
    data = request.get_json()    
    user_name=data['user_name']
    new_user={ 
            'user_name':user_name,
            'user_id': str(uuid.uuid1())
        }
    all_users_list.append(new_user)
    return jsonify({'user': new_user})

@app.route('/', methods=['GET'])
@app.route('/api/get_users',methods=['GET'])
def all_users_getter():
    return jsonify({'users': all_users_list})



            

    