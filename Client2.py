import sys 
import Ice
Ice.loadSlice('Printer.ice')
import Example

class Client2(Ice.Application):
    def run(self, argv):
        endpoint = "tcp -h localhost -p 10000"
        proxy = self.communicator().stringToProxy("printer1:" + endpoint)
        printer = Example.PrinterPrx.checkedCast(proxy)
    
        if not printer:
            raise RuntimeError('Invalid Proxy')
        
        message = input("Ingrese el mensaje a imprimir: ")
        
        printer.write(message)
    
        return 0

if __name__ == "__main__":
    app = Client2()
    sys.exit(app.main(sys.argv))