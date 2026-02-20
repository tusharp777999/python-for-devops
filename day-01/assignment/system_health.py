import psutil

def check_system_health():
    user_input_threshold = int(input("Enter threshold value: "))
    cpu_threshold_value = psutil.cpu_percent(interval=1)

    if cpu_threshold_value > user_input_threshold:
        print("CPU alert sent mail !!!")
    else:
        print("CPU usage is in limit.")

check_system_health()

#Extra methods:
print("Disk usage: ", psutil.disk_usage('/'))
print("Disk partition: ", psutil.disk_partitions(all=True))
print("Swap memory: ", psutil.swap_memory())
print("Virtual memory: ", psutil.virtual_memory)
print("CPU stats: ", psutil.cpu_stats)
print("CPU frequency: ", psutil.cpu_freq(percpu=False))
print("CPU count: ", psutil.cpu_count(logical=True))
print("CPU times percent: ", psutil.cpu_times_percent(interval=None, percpu=False))