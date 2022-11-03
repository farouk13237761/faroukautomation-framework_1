import inspect

def whoami():
    return inspect.stack()[1][2]
def whosdaddy():
    return inspect.stack()[2][3]


def farouk():
    x= whosdaddy()
    print(x)


k=farouk()
print(k)