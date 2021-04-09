class electronic_device:

        usage= "easy"

        def functionality(self, ):
         return f"These are made to be used {self.usage}"

class pocket_gadget(electronic_device):
        handle= "useful"
        carry= "anyplace"

        def usability(self):
         return f"These are made to be used {self.handle} and it can be carried over to {self.carry}"

class phone(pocket_gadget):

         view= "eyecatchy"
         weight ="very light"

         def quality(self):
          return f"These  device is very {self.view} and very {self.weight} in hand "
chip= electronic_device()
radio=pocket_gadget()
mobile=phone()
print(radio.usage)