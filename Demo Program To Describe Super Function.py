# Demo Programs To Describe Use Of Super() Function

class P:
    a = 10
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent Instant Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent Static Method')
class C(P):
    def __init__(self):
        print('Child Constructor')
    def method1(self):
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()
c = C()
c.method1()
