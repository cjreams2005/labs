class A(object):
    def __str__(self):
        return 'Hello ' + object.__str__(self)

print(str(A()))