import time
from colorama import Fore as f

class Logger:
    @staticmethod
    def log(message, file):
        print(f"DEBUG | {time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime())} | {file} | {message} {f.RESET}")
