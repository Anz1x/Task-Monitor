# ▀█▀ ▄▀█ █▀ █▄▀     █▀▄▀█ █▀█ █▄░█ █ ▀█▀ █▀█ █▀█
# ░█░ █▀█ ▄█ █░█     █░▀░█ █▄█ █░▀█ █ ░█░ █▄█ █▀▄

# built in required python libraries
import os
import time
import platform

# all third-party libraries (no need to install just run the program and it will do it for ya)
try:
    import psutil
except ModuleNotFoundError:
    os.system("pip3 install psutil")

try:
    import GPUtil
except ModuleNotFoundError:
    os.system("pip3 install GPUtil")

try:
    import colorama
except ModuleNotFoundError:
    os.system("pip3 install colorama")

from colorama import Fore

colorama.init(autoreset=True)

clear = lambda: os.system("cls" if os.name== "nt" else "clear")

clear()

print(f"""{Fore.LIGHTCYAN_EX}                            __________
                           /         /.
    .-------------.       /_________/ |
   /             / |      |         | |
  /+============+/ |      | |====|  | |
  ||C:\>        || |      |         | |
  ||            || |      | |====|  | |
  ||            || |      |   ___   | |
  ||            || |      |  |166|  | |
  ||            ||/@@@    |   ---   | |
  \+============+/    @   |_________|./.
                     @          ..  ....'
  ..................@     __.'.'  ''
 /oooooooooooooooo//     ///
/................//     /_/
------------------
""")

print(f"{Fore.LIGHTCYAN_EX}="*45, f"{Fore.LIGHTYELLOW_EX}Task Monitor", f"{Fore.LIGHTCYAN_EX}="*45)
print("\n")

# getting GPUs and its info
gpus = GPUtil.getGPUs()
for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_uuid = gpu.uuid

# outputting all the sys & hardware info
print(f"Device Network Name: {Fore.YELLOW + platform.node()}")
print(f"Machine Type: {Fore.YELLOW + platform.machine()}")
print(f"Operating System: {Fore.YELLOW + platform.platform()}")
print(f"Processor: {Fore.YELLOW + platform.processor()}")
print(f"CPU Cores: {Fore.YELLOW, psutil.cpu_count(logical=False)}")
print(f"GPU: {Fore.YELLOW + gpu_name}")
print(f"GPU UUID: {Fore.YELLOW + gpu_uuid}")
print("\n")

# cpu & ram usage visually displayed with animated sliding bars
def task_monitor(cpu_usg, ram_usg, bars = 50):
    cpu = (cpu_usg / 100.0)
    cpu_displaybar = "█" * int(cpu * bars) + "-" * (bars - int(cpu * bars))
    ram = (ram_usg / 100.0)
    ram_displaybar = "█" * int(ram * bars) + "-" * (bars - int(ram * bars))

    print(f"\rCPU Usage: {Fore.LIGHTYELLOW_EX}|{cpu_displaybar}| {cpu:.2f}%  ", end="")
    print(f"RAM Usage: {Fore.RED}|{ram_displaybar}| {ram:.2f}%  ", end="\r")

while True:
    try:
        task_monitor(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
        time.sleep(0.5)
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "\n[-] Stopped the task monitor")
        exit(0)
