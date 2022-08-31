from flask import Flask,request,jsonify
import pymongo
import certifi

app=Flask(__name__)

client = pymongo.MongoClient("mongodb://rashmi:12345@ac-boqpqol-shard-00-00.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-01.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-02.hmmlux9.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyhkb5-shard-0&authSource=admin&retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test

database = client['taskdb']
collection = database['mongo_api']

@app.route('/mongo',methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return(jsonify(str("successfully inserted")))

@app.route('/update/mongo',methods=['POST'])
def update():
    if request.method=='POST':
        get_name=request.json['get_name']
        collection.update_one({name,number},{'$set': {get_name:number+100}})
        return(jsonify(str("successfully updated")))


if __name__=='__main__':
    app.run(port=5001)