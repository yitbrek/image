from __future__ import print_function

import grpc
from PIL import Image
import image_pb2
import image_pb2_grpc


def run():
    im=raw_input("enter file path: ")
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_pb2_grpc.GreeterStub(channel)
        response = stub.printimage(image_pb2.imageRequest(name=im))
    
    
    img = Image.open(response.message).convert('L')
    img.show()

if __name__ == '__main__':
    run()
