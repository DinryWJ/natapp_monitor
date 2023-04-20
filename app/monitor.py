import psutil
import subprocess

SERVICE = 'natapp'

def check_service_status():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name().lower()
            # print(process_name)
            if SERVICE in process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if not check_service_status():
    print(f'{SERVICE} service is not running, restarting...')
    subprocess.run(['sudo', 'service', SERVICE, 'start'])
else:
    print(f'{SERVICE} service is running')



if __name__ == "__main__":
    check_service_status()