import data_access_pb2_grpc, data_access_pb2
import grpc
import time 

def start_server(tweet_list):
    channel = grpc.insecure_channel('data:9090')
    stub = data_access_pb2_grpc.TweetServiceStub(channel)
    print("Start!!!!")
    while True:
        try:
            for i in stub.request(data_access_pb2.TweetRequest(flag = True)):
                tweet_list.append(i)
            break
        except Exception as e:
            print("GRPC Data Connection Failed!!")
            time.sleep(5);
  

