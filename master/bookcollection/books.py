from concurrent import futures

import grpc
from master_pb2 import (
    ProductCategory,
    ProductsList,
    ProductResponse,
)

import master_pb2_grpc

products_by_category = {
    ProductCategory.HOME_APPIENTS: [
        ProductsList(product_name="Chaire", price=100, rating=4),
        ProductsList(product_name="Table", price=100, rating=4),
        ProductsList(product_name="Dining table", price=100, rating=4),
        ProductsList(product_name="Bed", price=100, rating=4),
        ProductsList(product_name="Curtons", price=100, rating=4),
        ProductsList(product_name="Glass", price=100, rating=4),
    ],
    ProductCategory.ELECTRONICS: [
        ProductsList(product_name="Mobile", price=200, rating=4),
        ProductsList(product_name="Tablets", price=100, rating=4),
        ProductsList(product_name="Laptop", price=100, rating=4),
        ProductsList(product_name="Telivision", price=100, rating=4),
        ProductsList(product_name="Charger", price=100, rating=4),
    ],
    ProductCategory.BEAUTY: [
        ProductsList(product_name="Lipstiks", price=100, rating=4),
        ProductsList(product_name="Powder", price=100, rating=4),
        ProductsList(product_name="Eye brows", price=100, rating=4),
        ProductsList(product_name="Spray", price=100, rating=4),
    ]
}


class ProductService(
    master_pb2_grpc.ProductsServicer
):
    def Recommend(self, request, context):
        if request.category not in products_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "category not exist")
        

        return ProductResponse(products=products_by_category[request.category])
        

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_ProductsServicer_to_server(
        ProductService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()