import time
import zmq
import base64

# consumer
def consumer():
    context = zmq.Context()
    # recieve work

    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://10.0.0.13:5557")
    receiving_dir = '../../images/received/'
    while True:
        meta_data = consumer_receiver.recv_json()
        saving_path = receiving_dir+meta_data['filename']
        message = consumer_receiver.recv()
        with open(saving_path, 'wb') as f:
            bytes = bytearray(base64.b64decode(message))
            f.write(bytes)

consumer()
