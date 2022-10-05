from flask import Flask, render_template, request
from master_pb2 import ProductCategory, ProductRequest
from master_pb2_grpc import ProductsStub
import grpc

app = Flask(__name__)

host = "localhost"
channel = grpc.insecure_channel(
    f"{host}:50051"
)
client = ProductsStub(channel)

@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        category = request.form.get('category')
        if category is not "0":
            product_req = ProductRequest(category=category)
            res = client.Recommend(product_req)
            # print(res.products)
            return render_template("home.html", products=res.products)
        return render_template("home.html")
    
    if request.method == "GET":
        return render_template("home.html")