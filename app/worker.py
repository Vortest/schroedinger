import abc
import threading,Queue,time,sys,traceback
from app import browser_manager
from app import state_builder

class  Worker(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.Qin  = Queue.Queue()
        self.Qout = Queue.Queue()
        self.Qerr = Queue.Queue()
        self.Pool = []
        
    def start(self):
        for i in range(self.num_threads):
             thread = threading.Thread(target=self.process_queue)
             thread.start()
             self.Pool.append(thread)

    def stop(self):
        for i in range(len(self.Pool)):
            self.Qin.put(('stop',None))
        while self.Pool:
            time.sleep(1)
            for index,the_thread in enumerate(self.Pool):
                if the_thread.isAlive():
                    continue
                else:
                    del self.Pool[index]
                break

    @abc.abstractmethod
    def process_item(self, value):
        return

    def process_queue(self):
        flag='ok'
        while flag !='stop':
            try:
                flag,value=self.Qin.get()
                print "Processing %s %s" % (value,flag)
                if flag=='ok':
                    results = self.process_item(value)
                    self.Qout.put(results)
            except Exception as e:
                print "Exception: %s " % str(e)
                self.Qerr.put(self.err_msg())


    def get_all(self):
        try:
            while 1:
                yield self.Qout.get_nowait()
        except Queue.Empty:
            pass

    def err_msg(self):
        trace= sys.exc_info()[2]
        try:
            exc_value=str(sys.exc_value)
        except:
            exc_value=''
        return str(traceback.format_tb(trace)),str(sys.exc_type),exc_value

    def put(self,data,flag='ok'):
        self.Qin.put([flag,data])

    def get(self,): return self.Qout.get()
