
from concurrent import futures
import time

import grpc

import image_pb2
import image_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class Greeter(image_pb2_grpc.GreeterServicer):

    def printimage(self, request, context):
        return image_pb2.imageReply(message=request.name)
 


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
