import time

from colorama import Fore as f


class Logger:
    def log(self, message, file):
        print(f"[LOG] | {time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime())} | {file} | {message} {f.RESET}")
