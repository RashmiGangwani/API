from flask import Flask,request,jsonify
import mysql.connector as connection

app=Flask(__name__)

@app.route('/test')
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail")
    return "this is my first func for get {} {} {}".format(get_name,mobile_number,mail_id)

@app.route('/get_data')
def get_data():
        db_name = request.args.get("db_name")
        table_name = request.args.get("table_name")
        mydb = connection.connect(host="localhost", user="root", passwd="Asdfghjkl$1",database=db_name)
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(f"select * from {table_name}")
        data=cursor.fetchall()
        mydb.commit()

        return(jsonify(data))

if __name__=='__main__':
    app.run(port=5002)