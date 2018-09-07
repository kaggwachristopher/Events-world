from flask import Flask,jsonify,request,json
import uuid

app=Flask('__name__')

all_users_list= []

@app.route('/', methods=['GET'])
@app.route('/api/user',methods=['GET'])
def all_users_getter():
    return jsonify({'users': all_users_list}),200

@app.route('/api/user',methods=['POST'])
def  add_a_user():
    data=request.get_json()
    name=data['user_name']
    
    new_user={
            "user_id": str(uuid.uuid1()),
            "user_name":name
        }
    all_users_list.append(new_user)
    return jsonify({'message':'new user created'}),201
    
 

@app.route('/api/user/<user_id>',methods=['DELETE'])
def delete_user(user_id):
    for user in all_users_list:
        if str(user['user_id'])==str(user_id):
            all_users_list.remove(user)
            return jsonify({'message':'User successfully deleted'}),200
        else:
            return jsonify({'message':'User doesnt exist'}),404



            

    
