from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8005), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def adder_function(x, y):
        result = x+y
        print(result)
        return result

    def multiplier_function(x, y):
        result = x*y
        print(result)
        return result
    
    def power_function(x, y):
        result = x**y
        print(result)
        return result
    
    def divider_function(x, y):
        result = x/y
        print(result)
        return result
    
    def subtracter_function(x, y):
        result = x-y
        print(result)
        return result
    
    server.register_function(adder_function, 'add')
    server.register_function(multiplier_function, 'multiply')
    server.register_function(power_function, 'power')
    server.register_function(divider_function, 'divide')
    server.register_function(subtracter_function, 'subtract')

    server.serve_forever()