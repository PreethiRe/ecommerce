# Ecommerce API Reference

##Orders

#Add Orders 

Post http://127.0.0.1:5000/orders

Body {"itemId":"1","userId":"1","quantity":"1","price":"2500"}

Response:
{
    "statusCode": 1,
    "message": "success"
}

#Get Orders

Get http://127.0.0.1:5000/orders

Response:
{
    "statusCode": 1,
    "data": [
        {
            "userId": "1",
            "price": "2500",
            "quantity": "1",
            "orderId": 1,
            "itemId": 1
        }
    ]
}

##Items

#Add Items

Post http://127.0.0.1:5000/items

Content-Type:application/json

Body:
{"itemName":"laptop","price":"25000","stocks":"5"}

Response:
{
    "statusCode": 1,
    "message": "success"
}

#Update Items

Put http://127.0.0.1:5000/items

Content-Type:application/json

Body:
{"itemName":"laptop","price":"2500","stocks":"5","itemId":"1"}

Response:
{
    "statusCode": 1,
    "message": "success"
}

#Get item list/particular item:

Get http://127.0.0.1:5000/items

Get http://127.0.0.1:5000/items?itemId=1

Response:
{
    "statusCode": 1,
    "data": [
        {
            "itemId": 1,
            "price": "5",
            "itemName": "laptop",
            "stocks": "2500"
        }
    ]
}

#Delete Items

Delete http://127.0.0.1:5000/items
Content-Type:application/json
Body:
{"itemId":"1"}

Response:
{
    "statusCode": 1,
    "message": "success"
}

