from flask_restx import Namespace,Resource

order_namespace = Namespace('orders',description="Namespace for orders")

@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self):
        pass

    def post(self):
        pass


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self,order_id):
        pass

    def post(self,order_id):
        pass

    
    def delete(self,order_id):
        pass


@order_namespace.route('/user/<int:user_id>/order/<int:order_id')
class GetSpecificOrderByUser(Resource):
    def get(self,user_id,order_id):
        pass



@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):

    def get(self,user_id):


        pass


@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    def patch(self,order_id):
        """
        
        """