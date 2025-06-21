import platform
import psutil
import subprocess
import json

def get_host_info() -> str:
    """get host information
    
    Returns:
        str: the host information in JSON string
    """
    info: dict[str, str] = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.architecture()[0],
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    
    cpu_count: int | None = psutil.cpu_count(logical=True)
    
    try:
        cpu_model: str = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"], text=True, stderr=subprocess.DEVNULL
        ).decode().strip()
        info["cpu_model"] = cpu_model
    except (subprocess.CalledProcessError, FileNotFoundError):
        info["cpu_model"] = "Unknown"
    
    return json.dumps(info, indent=4)

if __name__ == "__main__":
    print(get_host_info())