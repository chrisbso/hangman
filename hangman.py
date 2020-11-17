import sys, importlib, os
if __name__ == "__main__":
    fileName = str(sys.argv[1])
    attempts = int(sys.argv[2])
    from hangmanFunctions import *
    importlib.reload(sys.modules['hangmanFunctions'])
    instanceGame(fileName,attempts)