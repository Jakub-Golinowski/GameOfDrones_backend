from threading import Thread
import websocket
import json

try:
    import thread
except ImportError:
    import _thread as thread

current_request = {}

def my_on_message(ws, message):
    global current_request
    current_request = json.loads(message)


def my_on_error(ws, error):
    print(error)


def my_on_close(ws):
    print("### closed ###")


def my_on_open(ws):
    print("### started the thread ###")


class InvoliWorker(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        abort = False
        current_req = None
        ws = None

    def run(self):
        print('Running the web socket to wss://hackzurich.involi.live/ws_recorded/')

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://hackzurich.involi.live/ws_recorded/",
                                  on_message = my_on_message,
                                  on_error = my_on_error,
                                  on_close = my_on_close)
        ws.on_open = my_on_open
        ws.run_forever()





# Run following code when the program starts
if __name__ == '__main__':
    # Declare objects of MyThread class
    involi_worker = InvoliWorker()
    involi_worker.setName('InvoliWorker 1')

    involi_worker.run()

    print('Main Terminating...')