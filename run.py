import os
import platform
import subprocess
import stat
import yaml

path = os.getcwd()

subprocess.Popen(['python', 'webserver.py'], text=True)
subprocess.Popen(['python', 'sync.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("the webserver is running on http://localhost:8000")

def load_config():
    config_path = os.path.join(path, 'config.yml')
    config = {}  
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file) or {}
                if not config:
                    config = {
                        'node_installed': '',
                        'program_run_before': '',
                        'webssh_port': '1234',
                        'webssh_user': '',
                        'websftp_port': '1234',
                        'webssh_password': ''
                    }
                    save_config(config)
                return config
        except Exception as e:
            print(f"Error loading config.yml: {e}")
            return config  
    else:
        print("config.yml not found, creating a new one with default values.")
        config = {
            'node_installed': '',
            'program_run_before': '',
            'webssh_port': '1234',
            'webssh_user': '',
            'websftp_port': '1234',
            'webssh_password': ''
        }
        save_config(config) 
        return config


def save_config(config):
    config_path = os.path.join(path, 'config.yml')
    try:
        with open(config_path, 'w') as file:
            yaml.safe_dump(config, file)
            print("Configuration saved")
    except Exception as e:
        print(f"error saving config.yml: {e}")

config = load_config()

run = 0

print("=========================================")
print("welcome to the vulcanopanel start script.")
print("do you want to run some commands or do you want to start the script immediately? ")
print("")
start = input("(1) run some commands \n(2) start the script immediately \n> ")
print("=========================================")
if start == "1":
    run = 0
    print("welcome to the command prompt")
    print("for a list of commands type help")
    print("-----------------------------------")
    while run == 0:
        command = input(">> ").lower()
        if command == "help":
            print("=====[list of commands]=====")
            print("- config (view the current configuration)")
            print("- ports (view the required ports for this script)")
            print("- os (view the recomended and supported operating systems)")
            print("- run (start this script when you ran all the commands)")
            print("- ftp (view the details of the sftp server)")
            print("- ssh (view the details of the ssh server)")
            print("=============================")

        elif command == "config":
            node = config.get("node_installed")
            ran = config.get("program_run_before")
            sftp_port = config.get("websftp_port")
            ssh_port = config.get("webssh_port")
            ssh_user = config.get("webssh_user")
            ssh_password = config.get("webssh_password")

            node_ans = ""
            ran_ans = ""
            sftp_port_ans = ""
            ssh_port_ans = ""
            ssh_user_ans = ""
            ssh_password_ans = ""

            if node == "y":
                node_ans = "yes"
            elif node == "n":
                node_ans = "no"
            elif node == '':
                node_ans = "undefined"
            if ran == "y":
                ran_ans = "yes"
            elif ran == "n":
                ran_ans = "no"
            elif ran == '':
                ran_ans = "no"
            if sftp_port == '1234':
                sftp_port_ans = "undefined"
            else:
                sftp_port_ans = sftp_port
            if ssh_port == '1234':
                ssh_port_ans = "undefined"
            else:
                ssh_port_ans = ssh_port
            if ssh_user == '':
                ssh_user_ans = "undefined"
            else:
                ssh_user_ans = ssh_user
            if ssh_password == '':
                ssh_password_ans = "undefined"
            else:
                ssh_password_ans = ssh_password

            print("=====[config]=====")
            print("is node installed? (this value is incorrect if you haven't run this script before): ", node_ans)
            print("")
            print("did you run this script before? (this value is incorrect if you haven't run this script before): ", ran_ans)
            print("")
            print("what is the port of the websftp server?: ", sftp_port_ans)
            print("")
            print("what is the port of the webssh server?: ", ssh_port_ans)
            print("")
            print("what is the username for the webssh server?: ", ssh_user_ans)
            print("")
            print("what is the password for the webssh server?: ", ssh_password_ans)
            print("==================")

        elif command == "ports":
            print("=====[ports]=====")
            print("for this script you need 3 ports.")
            print("")
            print("the ports you need: ")
            print("- 8000 (required for the main panel)")
            print("- a port of choice (required for the webssh server)")
            print("- another port of choice (required for the websftp server)")
            print("")
            print("if you want the panel to be accessible outside your loca network, you need to forward the ports in your router.")
            print("if you don't have the credentials of your router (which can be found on the back of your router) or you don't want to forward the ports in your router,")
            print("you can use a tunnel software like https://playit.gg or https://ngrok.com")
            print("==================")

        elif command == "os":
            print("=====[os]=====")
            print("for this script we recommend to use a debian based linux distro")
            print("")
            print("=+=+=+[supported operating systems]+=+=+=")
            print("we support the following operating systems: ")
            print("- every debian based linux distro")
            print("- every fedora based linux distro")
            print("- every arch based linux distro")
            print("- windows")
            print("-=-=-=[unsupported operating systems]=-=-=-")
            print("- macOS")
            print("- unknown linux distro's")
            print("================")

        elif command == "ftp":
            print("=====[sftp]=====")
            print("for file transfers, you can use sftp with filezilla")
            print("host: localhost")
            print("port: 22")
            print("username: ", ssh_user_ans)
            print("password: ", ssh_password_ans)
            print("----------------")
            print("we recommend to use the main panel: https://localhost:8000")
            print("================")

        elif command == "ssh":
            print("=====[ssh]=====")
            print("for sending commands, you can use ssh with putty")
            print("host: localhost")
            print("port: 22")
            print("username: ", ssh_user_ans)
            print("password: ", ssh_password_ans)
            print("----------------")
            print("we recommend to use the main panel: https://localhost:8000")
            print("===============")

        elif command == "run":
            run = 1

        else:
            print("unknown command")

elif start == "2":
    run = 1

if run == 1:

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
        keys_to_check = ["webssh_user", "webssh_password", "program_run_before", "node_installed"]
        
        if config_key == "webssh_port" and (config_key not in config or config[config_key] == "1234"):
            answer = input(question).lower()
            config[config_key] = answer
            save_config(config)
            return answer
        
        if config_key == "websftp_port" and (config_key not in config or config[config_key] == "1234"):
            answer = input(question).lower()
            config[config_key] = answer
            save_config(config)
            return answer

        if any(key not in config or not config[key] for key in keys_to_check):
            answer = input(question).lower()
            config[config_key] = answer
            save_config(config)
            return answer
        
        return config[config_key]


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
        path_setup_ssh_sftp_deb = os.path.join(path, "setup_ssh_sftp.sh")
        path_linux = os.path.join(path, "linux")
        install_sftp_deb = os.path.join(path_linux, "install_sftp.sh")
        install_ssh_deb = os.path.join(path_linux, "install_ssh.sh")
        start_sftp_deb = os.path.join(path_linux, "start_sftp.sh")
        start_ssh_deb = os.path.join(path_linux, "start_ssh.sh")

        for script in [path_node_deb, path_install_deb, path_start_deb, install_sftp_deb, install_ssh_deb, start_sftp_deb, start_ssh_deb, path_setup_ssh_sftp_deb]:
            try:
                os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                print(f"Permissions successfully set for {script}.")
            except Exception as e:
                print(f"Error setting permissions for {script}: {e}")

        run_subprocess(['bash', path_setup_ssh_sftp_deb])
        run_subprocess(['sudo', 'apt', 'install', 'firewalld', '-y'])
        run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
        run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])

        if ask_question("Is Node.js already installed? (Y/N)", "node_installed") == "n":
            run_subprocess(['bash', path_node_deb])

        if ask_question("Has this program been run before? (Y/N)", "program_run") == "n":
            run_subprocess(['bash', path_install_deb])

        ask_question("On which port do you want to run the webssh server? (default port is 8002)", "webssh_port")
        ask_question("On which port do you want to run the websftp server? (default port is 8001)", "websftp_port")
        
        ask_question("set the username for the webssh server: ", "webssh_user")
        ask_question("set the password for the webssh server: ", "webssh_password")

        webssh_port = config.get("webssh_port")
        websftp_port = config.get("websftp_port")

        start = input("Do you want to start the program now? (Y/N)").lower()
        if start == "y":
            print("===================================================================")
            print(f"The sftp server is running on http://localhost:{websftp_port}")
            print(f"The webssh server is running on http://localhost:{webssh_port}/ssh/host/127.0.0.1")
            print("===================================================================")
            print("go to http://localhost:8000 for the main panel")
            run_subprocess(['bash', path_start_deb])
        else:
            input("Press enter to exit...")

    def execute_fedora_code():
        path_node_fedora = os.path.join(path, "install_node_fedora.sh")
        path_install_fedora = os.path.join(path, "install_fedora.sh")
        path_start_fedora = os.path.join(path, "start_fedora.sh")
        path_setup_ssh_sftp_fedora = os.path.join(path, "setup_ssh_sftp_fedora.sh")
        path_linux = os.path.join(path, "linux")
        install_sftp_fedora = os.path.join(path_linux, "install_sftp.sh")
        install_ssh_fedora = os.path.join(path_linux, "install_ssh.sh")
        start_sftp_fedora = os.path.join(path_linux, "start_sftp.sh")
        start_ssh_fedora = os.path.join(path_linux, "start_ssh.sh")

        for script in [path_node_fedora, path_install_fedora, path_start_fedora, path_setup_ssh_sftp_fedora, install_sftp_fedora, install_ssh_fedora, start_sftp_fedora, start_ssh_fedora]:
            try:
                os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                print(f"Permissions successfully set for {script}.")
            except Exception as e:
                print(f"Error setting permissions for {script}: {e}")

        run_subprocess(['sudo', 'dnf', 'install', 'firewalld', '-y'])
        run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
        run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])
        run_subprocess(['bash', path_setup_ssh_sftp_fedora])

        if ask_question("Is Node.js already installed? (Y/N)", "node_installed") == "n":
            run_subprocess(['bash', path_node_fedora])

        if ask_question("Has this program been run before? (Y/N)", "program_run_before") == "n":
            run_subprocess(['bash', path_install_fedora])

        ask_question("On which port do you want to run the webssh server? (default port is 8002)", "webssh_port")
        ask_question("On which port do you want to run the websftp server? (default port is 8001)", "websftp_port")
        
        ask_question("set the username for the webssh server: ", "webssh_user")
        ask_question("set the password for the webssh server: ", "webssh_password")

        webssh_port = config.get("webssh_port")
        websftp_port = config.get("websftp_port")

        start = input("Do you want to start the program now? (Y/N)").lower()
        if start == "y":
            print("===================================================================")
            print(f"The sftp server is running on http://localhost:{websftp_port}")
            print(f"The webssh server is running on http://localhost:{webssh_port}/ssh/host/127.0.0.1")
            print("===================================================================")
            print("go to http://localhost:8000 for the main panel")
            run_subprocess(['bash', path_start_fedora])
        else:
            input("Press enter to exit...")

    def execute_arch_code():
        path_node_arch = os.path.join(path, "install_node_arch.sh")
        path_install_arch = os.path.join(path, "install_arch.sh")
        path_start_arch = os.path.join(path, "start_arch.sh")
        path_setup_ssh_sftp_arch = os.path.join(path, "setup_ssh_sftp_arch.sh")
        path_linux = os.path.join(path, "linux")
        install_sftp_arch = os.path.join(path_linux, "install_sftp_arch.sh")
        install_ssh_arch = os.path.join(path_linux, "install_ssh_arch.sh")
        start_sftp_arch = os.path.join(path_linux, "start_sftp_arch.sh")
        start_ssh_arch = os.path.join(path_linux, "start_ssh_arch.sh")

        for script in [path_node_arch, path_install_arch, path_start_arch, install_sftp_arch, install_ssh_arch, start_sftp_arch, start_ssh_arch]:
            try:
                os.chmod(script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                print(f"Permissions successfully set for {script}.")
            except Exception as e:
                print(f"Error setting permissions for {script}: {e}")

        run_subprocess(['bash', path_setup_ssh_sftp_arch])
        run_subprocess(['sudo', 'pacman', '-S', 'firewalld', '--noconfirm'])
        run_subprocess(['sudo', 'systemctl', 'start', 'firewalld'])
        run_subprocess(['sudo', 'systemctl', 'enable', 'firewalld'])

        if ask_question("Is Node.js already installed? (Y/N)", "node_installed") == "n":
            run_subprocess(['bash', path_node_arch])

        if ask_question("Has this program been run before? (Y/N)", "program_run_before") == "n":
            run_subprocess(['bash', path_install_arch])

        ask_question("On which port do you want to run the webssh server? (default port is 8002)", "webssh_port")
        ask_question("On which port do you want to run the websftp server? (default port is 8001)", "websftp_port")
        
        ask_question("set the username for the webssh server: ", "webssh_user")
        ask_question("set the password for the webssh server: ", "webssh_password")

        webssh_port = config.get("webssh_port")
        websftp_port = config.get("websftp_port")

        start = input("Do you want to start the program now? (Y/N)").lower()
        if start == "y":
            print("===================================================================")
            print(f"The sftp server is running on http://localhost:{websftp_port}")
            print(f"The webssh server is running on http://localhost:{webssh_port}/ssh/host/127.0.0.1")
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

        install_node = ask_question("Is Node.js already installed? (Y/N)", "node_installed")

        if install_node.lower() == "n":
            run_subprocess([path_node_win])

        done = ask_question("Has this program been run before? (Y/N)", "program_run_before")
        
        if done.lower() == "n":
            run_subprocess([path_install_win])

        ask_question("On which port do you want to run the webssh server? (default port is 8002)", "webssh_port")
        ask_question("On which port do you want to run the websftp server? (default port is 8001)", "websftp_port")
        
        ask_question("set the username for the webssh server: ", "webssh_user")
        ask_question("set the password for the webssh server: ", "webssh_password")

        webssh_port = config.get("webssh_port")
        websftp_port = config.get("websftp_port")

        start = input("Do you want to start the program now? (Y/N)").lower()
        if start == "y":
            print("===================================================================")
            print(f"The sftp server is running on http://localhost:{websftp_port}")
            print(f"The webssh server is running on http://localhost:{webssh_port}/ssh/host/127.0.0.1")
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
