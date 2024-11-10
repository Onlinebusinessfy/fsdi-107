from flask import Flask, json, request


app= Flask(__name__)

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
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item=request.get_json()
    print(item)
    products.append(item)
    return json.dumps(item)

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

app.run(debug=True)