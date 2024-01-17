import json
from flask import Flask,jsonify
import psycopg2
import pandas as pd

app = Flask(__name__)

@app.route('/') # route for the index page
def index():
    # print("Hello")
    # result = {
    #     "msg":"Hello World!"
    # }
    # return jsonify(result)
    # Connect to the database
    connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="postgres", password="120698")

    # Create a cursor
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT * FROM customer")

    # Fetch the result
    result = cursor.fetchall()
    print(result)

    table_result = pd.DataFrame(result,columns=['Customer_id', 'First Name','Last Name','Age'])
    print(table_result)
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Return the result as a response
    return f"{result}"

@app.route('/fetchdata')
def fetchdata():
    connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="postgres", password="120698")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchall()
    table_result = pd.DataFrame(result,columns=['Customer_id', 'First Name','Last Name','Age'])
    # data = []
    # for i in table_result.index:
    #     data.append({"customer_id": str(table_result.loc[i,"Customer_id"]) ,
    #                  "first_name":table_result.loc[i,"First Name"],
    #                  "last_name":table_result.loc[i,"Last Name"],
    #                  "age":table_result.loc[i,"Age"]
    #                  })
        
    # result_dic = {"data":data}
    json_output = json.loads('{"status":"", "message":"" }')
    customer_list=json.loads(table_result.to_json(orient='records'))
    json_output['status_cd'] = 200
    json_output['data'] = customer_list
    json_output['success'] = 'true'
    json_output['message'] = 'list retrieved successfully.'
    cursor.close()
    connection.close()
    return jsonify(json_output)


@app.route('/insertdata')
def insertdata():
    connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="postgres", password="120698")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer (customer_id,first_name,last_name,age) VALUES (2,'Smith','Warner',24)")
    connection.commit()

    return "DATA INSERTED"

@app.route('/joins')
def fetchdataJoins():
    connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="postgres", password="120698")
    cursor = connection.cursor()
    query = """select customer.customer_id,customer.first_name,customer.last_name,customer.age,orders.item,orders.quantity,
        orders.amount from customer inner join orders on customer.customer_id = orders.customer_id;"""
    
    cursor.execute(query)
    results = cursor.fetchall()
    table_results = pd.DataFrame(results,columns=['Customer_id', 'First Name','Last Name','Age','Item Ordered','Quantity','Amount'])
    json_output = json.loads('{"status":"", "message":"" }')
    list=json.loads(table_results.to_json(orient='records'))
    json_output['status_cd'] = 200
    json_output['data'] = list
    json_output['success'] = 'true'
    json_output['message'] = 'list retrieved successfully.'
    cursor.close()
    connection.close()
    return jsonify(json_output)

@app.route('/user/<username>') # dynamic url
def show_user(username): 
    # Greet the user 
     print(f'Hello {username} !')
     result = {
        "msg":f'Hello {username} !'
     }
     return jsonify(result)
   

# Additionally, we can also use a converter to convert the variable to a specific data type. By default, it is set to string values. To convert use <converter:variable_name> and following converter types are supported.

# string: It is the default type and it accepts any text without a slash.
# int: It accepts positive integers.
# float: It accepts positive floating-point values.
# path: It is like a string but also accepts slashes.
# uuid: It accepts UUID strings.

@app.route('/post/<int:id>') 
def show_post(id): 
    # Shows the post with given id. 
    result = {
        "msg":f'This post has the id {id}'
    }
    return jsonify(result)
     

@app.route('/hello')
def hello():
    return "Hello"

@app.route('/dataframe')
def dataframe(): 
    mydatasets = {
        'cars' : ["BMW","VOLVO","FORD"],
        'passings':[3,7,5]
    }
    myvar = pd.DataFrame(mydatasets)
    print(myvar)
    return "dataframe"

if __name__ == '__main__':
    app.run(debug=True)   # set debug to False for production env 