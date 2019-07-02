import _thread


RABBITMQ_ENDPOINT = "localhost"

QUEUE_NAME_COMMAND = 'command_queue'


from Requests.Receive import ListenToReceive


th = _thread.start_new(ListenToReceive(RABBITMQ_ENDPOINT, QUEUE_NAME_COMMAND, pure_simulation=False))
