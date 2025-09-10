import psutil

# Get disk usage for a specific path
disk_usage = psutil.disk_usage('/')

print(f"Total: {disk_usage.total / (1024**3):.2f} GB")
print(f"Used: {disk_usage.used / (1024**3):.2f} GB")
print(f"Free: {disk_usage.free / (1024**3):.2f} GB")
print(f"Percentage Used: {disk_usage.percent}%")