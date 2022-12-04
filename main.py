import subprocess
import os
import sys
from time import sleep
import pathlib
import asyncio
import datetime
import time

def main():
    subprocess.Popen([sys.executable, "client1.py"])
    subprocess.Popen([sys.executable, "client2.py"])

if __name__ == '__main__':
    main()
