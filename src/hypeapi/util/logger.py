from colorama import Fore as f
import time

class Logger:
    def log(self, message, file):
        print(f"[DEBUG] | {time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime())} | {file} | {message} {f.RESET}")