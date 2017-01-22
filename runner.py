from my_package.myfirstmodule.maps import maps
from my_ackage.mysecondmodule.utils import connection_to

def viz():
    return maps, connection_to

if __name__ == '__main__':
    print viz()