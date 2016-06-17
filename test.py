import ctypes

libbatteries = ctypes.CDLL('libbatteries.dylib')
libbatteries.myprint()
