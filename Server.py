import sys
import Ice

Ice.loadSlice('Printer.ice')
import Example

class ConsolePrinter(Example.Printer):
    def write(self, message, current=None):
        print(message, flush=True)

class Server(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = ConsolePrinter()

        endpoint = "tcp -h localhost -p 10000"
        adapter = broker.createObjectAdapterWithEndpoints("PrinterAdapter", endpoint)

        proxy = adapter.add(servant, broker.stringToIdentity("printer1"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0

if __name__ == "__main__":
    server = Server()
    sys.exit(server.main(sys.argv))
