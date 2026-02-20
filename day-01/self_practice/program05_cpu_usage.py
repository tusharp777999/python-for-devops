'''
We need to find the current CPU usage. To get the current CPU usage we have library in python which is called as "psutil".
"psutil" is a cross-platform library used to monitor system resources like CPU, memory. disks, network, sensors etc and manages running processes.
It provides functionality similar to command line tools like top, ps, netstat and ifconfig supporting Linux, MacOS and BSD systems.
Note: To install library we need to use the below command:
>pip install psutil or pip3 install psutil
Here pip stands for p: pip, i: installs, p:packages

But to use this library we need to install it.
This library is available on the open source platform called as pypi.org official website: https://pypi.org/project/psutil/
pypi stands for py: python, p: package, i: index.

Once the package is installed we need to import it in our program or project so then we can able to use it.
'''
import psutil #Here we imported the package.

def check_cpu_usage():#Defined the function.
    input_threshold = int(input("Enter the threshold value: "))#Taking threshold value from user as an input.
    current_system_threshold = psutil.cpu_percent(interval=1)#Get the current system cpu usage using the "psutil" having in-built method which is "cpu_percent()" and interval is a attribute for the method which fetches the details from past 1 second how much it is utilized.
    print("Current CPU Threshold value is: ", current_system_threshold)
    if current_system_threshold > input_threshold:
        print("CPU alert email sent!!!")
    else:
        print("CPU is not reached the threshold value.")

check_cpu_usage()