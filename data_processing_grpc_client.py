import processing_pb2 as pb2
import processing_pb2_grpc as pb2_grpc
import grpc
import time 

def process(tweet):
    channel = grpc.insecure_channel('processing:9091')
    stub = pb2_grpc.ProcessingStub(channel)
    result_future = stub.process.future(pb2.PrRequest(tweet = tweet))
    result = result_future.result()
    return result
    
  