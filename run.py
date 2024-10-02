import os
import platform
import subprocess
import stat
import yaml

path = os.getcwd()

subprocess.Popen(['python', 'webserver.py'], text=True)

print("the webserver is running on http://localhost:8000")

def load_config():
    config_path = os.path.join(path, 'config.yml')
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                return config
        except Exception as e:
            print(f"Error loading config.yml: {e}")
            return {}
    else:
        print("config.yml not found, an empty configuration is being used.")
        return {}

def save_config(config):
    config_path = os.path.join(path, 'config.yml')
    try:
        with open(config_path, 'w') as file:
            yaml.safe_dump(config, file)
            print("Configuration saved")
    except Exception as e:
        print(f"error saving config.yml: {e}")

config = load_config()

def detect_os_and_execute():
    os_name = platform.system()

    if os_name == 'Linux':
        if os.path.isfile('/etc/os-release'):
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith("ID="):
                        distro_id = line.strip().split('=')[1].strip('"')
                        if distro_id in ['debian', 'ubuntu']:
                            print("Detected Linux distribution: Debian-based")
                            execute_debian_code()
                        elif distro_id in ['fedora']:
                            print("Detected Linux distribution: Fedora-based")
                            execute_fedora_code()
                        elif distro_id in ['arch']:
                            print("Detected Linux distribution: Arch-based")
                            execute_arch_code()
                        else:
                            print(f"Unknown Linux distribution: {distro_id}")
                            execute_unknown_linux_code()
        else:
            print("Not a Linux distribution or /etc/os-release file not found.")

    elif os_name == 'Windows':
        print("Detected OS: Windows")
        execute_windows_code()

    elif os_name == 'Darwin':
        print("Detected OS: macOS")
        execute_macos_code()

    else:
        print("Unknown operating system")

def ask_question(question, config_key):
    if config_key in config:
        return config[config_key]
    answer = input(question).lower()
    config[config_key] = answer
    save_config(config)
    return answer

def run_subprocess(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {' '.join(command)}")
        print(f"Error message: {e.stderr.strip()}")
        print(f"Error code: {e.returncode}")

def execute_debian_code():
    path_node_deb = os.path.join(path, "install_node.sh")
    path_install_deb = os.path.join(path, "install.sh")
    path_start_deb = os.path.join(path, "start.sh")
    path_linux = os.path.join(path, "linux")
    install_sftp_deb = os.path.join(path_linux, "install_sftp.sh")
    install_ssh_deb = os.path.join(path_linux, "install_ssh.sh")
    start_sftp_deb = os.path.join(path_linux, "start_sftp.sh")
    start_ssh_deb = os.path.join(path_linux, "start_ssh.sh")

    run_subprocess(['sudo', 'apt', 'install', 'firewalld', '-y'])
    run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
    run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])

    for script in [path_node_deb, path_install_deb, path_start_deb, install_sftp_deb, install_ssh_deb, start_sftp_deb, start_ssh_deb]:
        try:
            os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            print(f"Permissions successfully set for {script}.")
        except Exception as e:
            print(f"Error setting permissions for {script}: {e}")

    if ask_question("Is Node.js already installed? (Y/N)", "node_installed") == "n":
        run_subprocess(['bash', path_node_deb])

    if ask_question("Has this program been run before? (Y/N)", "program_run_before") == "n":
        run_subprocess(['bash', path_install_deb])

    if input("Do you want to start the program now? (Y/N)").lower() == "y":
        print("===================================================================")
        print("The sftp server is running on http://localhost:4340/")
        print("The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1")
        print("===================================================================")
        print("go to http://localhost:8000 for the main panel")
        run_subprocess(['bash', path_start_deb])
    else:
        input("Press enter to exit...")

def execute_fedora_code():
    path_node_fedora = os.path.join(path, "install_node_fedora.sh")
    path_install_fedora = os.path.join(path, "install_fedora.sh")
    path_start_fedora = os.path.join(path, "start_fedora.sh")
    
    run_subprocess(['sudo', 'dnf', 'install', 'firewalld', '-y'])
    run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
    run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])

    for script in [path_node_fedora, path_install_fedora, path_start_fedora]:
        try:
            os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            print(f"Permissions successfully set for {script}.")
        except Exception as e:
            print(f"Error setting permissions for {script}: {e}")

    if ask_question("Is Node.js already installed? (Y/N)", "node_installed_fedora") == "n":
        run_subprocess(['bash', path_node_fedora])

    if ask_question("Has this program been run before? (Y/N)", "program_run_before_fedora") == "n":
        run_subprocess(['bash', path_install_fedora])

    if input("Do you want to start the program now? (Y/N)").lower() == "y":
        print("===================================================================")
        print("The sftp server is running on http://localhost:4340/")
        print("The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1")
        print("===================================================================")
        print("go to http://localhost:8000 for the main panel")
        run_subprocess(['bash', path_start_fedora])
    else:
        input("Press enter to exit...")

def execute_arch_code():
    path_node_arch = os.path.join(path, "install_node_arch.sh")
    path_install_arch = os.path.join(path, "install_arch.sh")
    path_start_arch = os.path.join(path, "start_arch.sh")
    
    run_subprocess(['sudo', 'pacman', '-S', 'firewalld', '--noconfirm'])
    run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
    run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])

    for script in [path_node_arch, path_install_arch, path_start_arch]:
        try:
            os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            print(f"Permissions successfully set for {script}.")
        except Exception as e:
            print(f"Error setting permissions for {script}: {e}")

    if ask_question("Is Node.js already installed? (Y/N)", "node_installed_arch") == "n":
        run_subprocess(['bash', path_node_arch])

    if ask_question("Has this program been run before? (Y/N)", "program_run_before_arch") == "n":
        run_subprocess(['bash', path_install_arch])

    if input("Do you want to start the program now? (Y/N)").lower() == "y":
        print("===================================================================")
        print("The sftp server is running on http://localhost:4340/")
        print("The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1")
        print("===================================================================")
        print("go to http://localhost:8000 for the main panel")
        run_subprocess(['bash', path_start_arch])
    else:
        input("Press enter to exit...")

def execute_windows_code():
    print("Executing code specific to Windows...")
    path_node_win = os.path.join(path, "install_node.bat")
    path_install_win = os.path.join(path, "install.bat")
    path_start_win = os.path.join(path, "start.bat")

    install_node = ask_question("Is Node.js already installed? (Y/N)", "node_installed_windows")

    if install_node.lower() == "n":
        run_subprocess([path_node_win])

    done = ask_question("Has this program been run before? (Y/N)", "program_run_before_windows")
    
    if done.lower() == "n":
        run_subprocess([path_install_win])

    start = input("Do you want to start the program now? (Y/N)").lower()
    if start == "y":
        print("===================================================================")
        print("The sftp server is running on http://localhost:4340/")
        print("The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1")
        print("===================================================================")
        print("go to http://localhost:8000 for the main panel")
        run_subprocess([path_start_win])
    else:
        input("Press enter to exit...")

def execute_macos_code():
    print("macOS is not supported")

def execute_unknown_linux_code():
    print("your linux distro is unknown, use a debian based linux distro")

detect_os_and_execute()
