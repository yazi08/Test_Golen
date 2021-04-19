
print("Hello Yar")
class Myname:
    def __init__(self,name):
        self.name = name
        
    def __call__(self):
        return name
        
my = Myname()
my = Myname("Yazi")
my.name