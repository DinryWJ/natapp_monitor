import anyio
import threading


def run_async(name, func, args):
    thread = threading.Thread(name= name, target=func, args=args)
    thread.start()
    

def run_async_anonymous(func, args):
    thread = threading.Thread(target=func, args=args)
    thread.start()