from flask import Flask, json, request, abort
from config import db
from bson.objectid import ObjectId
from flask_cors import CORS

app= Flask(__name__)
CORS(app) #warning this disables CORS policy



@app.get("/")
def home():
    return "hello from flask"
# this is just an example
# @app.post("/")
#def homePost():
#    return "hello from flask post"

#Endpoints
@app.get("/test")
def test():
    return "hello from the test server"

# Endpoint using JSON
@app.get("/api/about")
def aboutGet():
    name={"name": "Samuel"}
    return json.dumps(name)

@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""

#by creating the farewell message
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:black>Goodbye {name}!</h1>"""

# ############################################
products=[]

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# @app.get("/api/products")
# def get_products():
#     products_db=[]
#     cursor=db.products.find({})
#     for prod in cursor:
#         products_db.append(fix_id(prod))
#     return json.dumps(products_db)

# @app.post("/api/products")
# def save_products():
#     item=request.get_json()
#     print(item)
#     # products.append(item)
#     db.products.insert_one(item)
#     return json.dumps(item)

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item=request.get_json()
    if 0<=index <=len(products):
        products[index]=updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item=request.get_json()
    if 0<=index <=len(products):
        delete_products=products.pop(index)
        return json.dumps(delete_products)

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field=request.get_json()
    if 0<=index <=len(products):
        updated_field[index].update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"
    



#Final Report
@app.get("/api/catalog")
def get_catalog():
    catalog_db=[]
    cursor=db.catalog.find({})
    for product in cursor:
        if "title" in product:
            catalog_db.append(fix_id(product))
    return json.dumps(catalog_db)

@app.post("/api/catalog")
def save_list():
    item=request.get_json()
    print(item)
    db.catalog.insert_one(item)
    return json.dumps(fix_id(item))

@app.delete("/api/catalog/<string:index>")
def delete_catalog(index):
    db.catalog.delete_one({"_id":ObjectId(index)})
    return json.dumps(index)

@app.get("/api/reports/total")
def get_total():
    total = 0
    cursor = db.catalog.find({})
    for product in cursor:
        price = product.get('price') or product.get('Price')
        if price and isinstance(price, (int, float)):
            total += float(price) 
    return json.dumps(total)


@app.get("/api/products/<string:category>")
def get_products_by_category(category):
    cursor=db.catalog.find({"category":category})
    products_db=[]
    for product in cursor:
        if "category" in product and product["category"]==category:
            print(product)
            products_db.append(fix_id(product))
    if len(products_db)==0:
            return "No products in that category"
    return json.dumps(products_db)



###########################
#########COUPONS###########
###########################

@app.post("/api/coupons")
def save_coupon():
    item=request.get_json()
    db.coupons.insert_one(item)
    return json.dumps(fix_id(item))

@app.get("/api/coupons")
def get_coupons():
    coupons_db=[]
    cursor = db.coupons.find({})
    for coupon in cursor:
        coupons_db.append(fix_id(coupon))
    return json.dumps(coupons_db)

@app.get("/api/coupons/<code>")
def validate_coupon(code):
    coupon=db.coupons.find_one({"code":code})
    if coupon == None:
        print("Error: invalid coupon")
        return abort(404, "Invalid Code")
    
    return json.dumps(fix_id(coupon))




app.run(debug=True)

