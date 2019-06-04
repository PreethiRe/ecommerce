from flask_restful import Resource, reqparse


from app import mysql

parser=reqparse.RequestParser()

from app import *


class Orders(Resource):
   
    def __init__(self):
        parser.add_argument('orderId', required=False)
        parser.add_argument('itemId', required=False)
        parser.add_argument('userId', required=False)
        parser.add_argument('quantity', required=False)
        parser.add_argument('price', required=False)
        
        

        

    def post(self):
        data = parser.parse_args()
        try:

            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "insert into orders(item_id, user_id,quantity,price ) "
                "values(%s,%s,%s,%s)",
                (data['itemId'], data['userId'],data['quantity'],data['price']))
            conn.commit()
            return {"message": "success", "statusCode": 1}
        except Exception as e:
            return {"message": e, "statusCode": 0}

    def get(self):

        mydata = parser.parse_args()

        conn = mysql.connect()
        cursor = conn.cursor()
        result = []
        

        cursor.execute("select * from orders ")

        data = cursor.fetchall()

        for i in data:

                result.append({'orderId': i[0], 'itemId': i[1],"userId":i[2],"quantity":i[3],"price":i[4]
                                    })

        if result != []:
            return {"data": result, "statusCode": 1}
        else:
            return {"message": "no data found", "statusCode": 0}

    
class Items(Resource):
    
    def __init__(self):
        parser.add_argument('itemName', required=False)
        parser.add_argument('itemId', required=False)
        parser.add_argument('price', required=False)
        parser.add_argument('stocks', required=False)
        
        
        
      
    def post(self):

        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            data = parser.parse_args()


            cursor.execute("insert into items(item_name,price,stocks) "
                           "values(%s,%s,%s)",
                           (data['itemName'],  data['price'],data['stocks']
                            ))

            conn.commit()
            return {"message": "success", "statusCode": 1}
        except Exception as e:
            return {"message": e, "statusCode": 0}

    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        data = parser.parse_args()
        if data.get("itemId"):
            cursor.execute("select * from items where item_id='"+str(data['itemId'])+"'")
        else:
            cursor.execute("select * from items")

        result = []
        mydata = cursor.fetchall()
        for i in mydata:
            result.append({"itemName": i[1], "itemId": i[0], "price": i[2],"stocks":i[3]})
        if result != []:
            return {"data": result, "statusCode": 1}
        else:
            return {"message": "no data found", "statusCode": 0}

    def put(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            data = parser.parse_args()
            
            cursor.execute("update items set item_name='" + str(data['itemName']) + "',stocks='" + str(
                data['stocks']) + "',price='" + str(data['price']) + "' where item_id='" + str(data['itemId']) + "' ")
            conn.commit()
            return {"message": "success", "statusCode": 1}
        except Exception as e:
            return {"message": e, "statusCode": 0}

    def delete(self):

        try:

            data = parser.parse_args()

            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute("delete from items where  item_id='" + str(
                data['itemId']) + "'")

            conn.commit()
            return {"message": "success", "statusCode": 1}
        except Exception as e:
            return {"message": e, "statusCode": 0}

