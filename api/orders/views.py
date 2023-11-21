from flask_restx import Namespace,Resource

order_namespace = Namespace('orders',description="Namespace for orders")

@order_namespace.route('orders')
class HelloOrder(Resource):

    def get(self):
        return {"message":"djfkasdnkajsndfjk"}
    
