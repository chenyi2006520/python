__author__="Seven"

class Hello:
    def __init__(self,name):#gou zao han shu
        self._name = name
    def sayhello(self):
        print("Hello Word")
    
    def saySome(self):
        print("Hello {0}".format(self._name))
        
        
class Hi(Hello):#//ji cheng lei
    def __init__(self,name):
        Hello.__init__(self,name)#zhi xing fu lei gou zao han shu
    
    def sayHi(self):
        print("Hi {0}".format(self._name))
        
h = Hello("Seven")
h.sayhello()    
h.saySome()

h2 = Hi("Dear")
h2.sayHi()
h2.sayhello()