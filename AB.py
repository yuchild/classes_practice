class A(object):
    def __init__(self, something):
        print('A init called...')
        self.something = something
        
class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print('B init called...')
        self.something = something