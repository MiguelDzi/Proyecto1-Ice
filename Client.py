import sys 
import Ice
Ice.loadSlice('Printer.ice')
import Example

class Client(Ice.Application):
    def run(self, argv):
        endpoint = "tcp -h localhost -p 10000"
        proxy = self.communicator().stringToProxy("printer1:" + endpoint)
        printer = Example.PrinterPrx.checkedCast(proxy)
    
        if not printer:
            raise RuntimeError('Invalid Proxy')
    
        printer.write('Hello World!')
    
        return 0

sys.exit(Client().main(sys.argv))

