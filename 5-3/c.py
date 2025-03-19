class MyClass:
    def __repr__(self):
        raise Exception


a = MyClass()
func(a)
