from flask import Flask, render_template, url_for, request
import data_processing_grpc_client
import data_access_grpc_client
import threading


tweet_list = []
tweet_list.append('Hello ddddworl!');
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tweet_list = tweet_list)

@app.route('/table')
def table():
    return render_template('table.html', tweet_list = tweet_list)

@app.route('/proc', methods = ['POST'])  
def label():
    tweet = request.values.get('tweet')
    print(tweet)
    return render_template('proc.html', result = data_processing_grpc_client.process(tweet))


clientActive = False

if __name__ == "__main__":
    if clientActive == False:
        thread = threading.Thread(target = data_access_grpc_client.start_server, args=(tweet_list, ))
        thread.start()
        clientActive = True
    
    app.run(host='0.0.0.0',debug = False, threaded = False)

# Tweet -> id, user, tweet, flags  => 
# Fields -> index.html
