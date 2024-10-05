import os
import yaml
import json
import time
import logging

logging.basicConfig(level=logging.INFO)

path = os.getcwd()
path_run_config = os.path.join(path, "config.yml")
path_webssh = os.path.join(path, "webssh")
path_websftp = os.path.join(path, "sftp_web_client")
path_webssh_config = os.path.join(path_webssh, "config.json")
path_websftp_config = os.path.join(path_websftp, "src")
path_js_config = os.path.join(path_websftp_config, "config.js")
path_html_file = os.path.join(path, "index.html")  

def load_yaml_config():
    """Load the YAML configuration file."""
    try:
        with open(path_run_config, 'r') as file:
            config = yaml.safe_load(file)
        logging.info(f"YAML Config loaded: {config}")
        return config
    except Exception as e:
        logging.error(f"Error loading YAML-config: {e}")
        return {}

def load_ssh_config():
    """Load the existing SSH JSON configuration file."""
    if os.path.exists(path_webssh_config):
        with open(path_webssh_config, 'r') as file:
            config = json.load(file)
        logging.info(f"Existing SSH JSON Config loaded: {config}")
        return config
    return {}

def save_json_config(json_path, data):
    """Save the data to a JSON configuration file."""
    try:
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Saved JSON config to {json_path}.")
    except Exception as e:
        logging.error(f"Error saving JSON-config: {e}")

def update_json_config_if_changed():
    """Update the configuration files if changes are detected in the YAML config."""
    yaml_config = load_yaml_config()
    if not yaml_config:
        logging.error("YAML configuration is empty or could not be loaded.")
        return 

    update_ssh_config(yaml_config)
    update_js_config(yaml_config.get("websftp_port", '8001'))  
    update_html_ports(yaml_config)  

def update_ssh_config(yaml_config):
    """Update the SSH configuration based on the YAML config."""
    json_config = load_ssh_config()

    new_json_config = {
        "listen": {
            "ip": "127.0.0.1",
            "port": int(yaml_config.get('webssh_port', 1239)) 
        },
        "user": {
            "name": yaml_config.get('webssh_user', 'default_user'),
            "password": yaml_config.get('webssh_password', 'default_password')
        },
        "ssh": {
            "host": "0.0.0.0",
            "port": 22,
            "term": "xterm-color",
            "readyTimeout": 20000
        },
        "useminified": False,
        "header": {
            "text": None,
            "background": "green"
        },
        "session": {
            "name": "WebSSH2",
            "secret": "mysecret"
        },
        "options": {
            "challengeButton": True
        },
        "algorithms": {
            "kex": [
                "ecdh-sha2-nistp256",
                "ecdh-sha2-nistp384",
                "ecdh-sha2-nistp521",
                "diffie-hellman-group-exchange-sha256",
                "diffie-hellman-group14-sha1"
            ],
            "cipher": [
                "aes128-ctr",
                "aes192-ctr",
                "aes256-ctr",
                "aes128-gcm",
                "aes128-gcm@openssh.com",
                "aes256-gcm",
                "aes256-gcm@openssh.com",
                "aes256-cbc"
            ],
            "hmac": [
                "hmac-sha2-256",
                "hmac-sha2-512",
                "hmac-sha1"
            ],
            "compress": [
                "none",
                "zlib@openssh.com",
                "zlib"
            ]
        },
        "serverlog": {
            "client": True,
            "server": False
        },
        "accesslog": True
    }

    if new_json_config != json_config:
        logging.info("SSH-config has changed, saving...")
        save_json_config(path_webssh_config, new_json_config)
        logging.info("SSH config.json has been updated.")
    else:
        logging.info("No changes detected in SSH-config.")

def update_js_config(sftp_port):
    """Update the config.js file with the new SFTP port."""
    if os.path.exists(path_js_config):
        with open(path_js_config, 'r') as file:
            js_content = file.read()
        logging.info("Existing JS Config loaded as text.")

        new_js_content = js_content.replace("sftpPort: '8001'", f"sftpPort: '{sftp_port}'")

        with open(path_js_config, 'w') as file:
            file.write(new_js_content)
        logging.info("config.js updated with the new SFTP port.")
    else:
        logging.warning(f"config.js doesn't exist at: {path_js_config}")

def update_html_ports(yaml_config):
    """Update the index.html file with the correct ports for the SSH and SFTP clients."""
    if os.path.exists(path_html_file):
        logging.info(f"HTML file found at: {path_html_file}")
        with open(path_html_file, 'r') as file:
            html_lines = file.readlines()
        logging.info("Existing HTML file loaded.")

        ssh_port = str(yaml_config.get("webssh_port", '1239')) 
        sftp_port = str(yaml_config.get("websftp_port", '8001')) 

        # Update the SSH link
        ssh_updated = False
        for i, line in enumerate(html_lines):
            if 'href="http://localhost:' in line and '/ssh/host/127.0.0.1"' in line:
                logging.info(f"Original SSH link found: {line.strip()}")
                html_lines[i] = f'        <a href="http://localhost:{ssh_port}/ssh/host/127.0.0.1">\n'
                logging.info(f"SSH link updated to: {html_lines[i].strip()}")
                ssh_updated = True
                break 

        if not ssh_updated:
            logging.warning("SSH link not found in HTML file!")

        sftp_line_index = 101
        #here you need to put the line where the sftp link is located in de index.html
        #line - 1
        if len(html_lines) > sftp_line_index:
            original_sftp_line = html_lines[sftp_line_index]
            logging.info(f"Original SFTP link found: {original_sftp_line.strip()}")
            html_lines[sftp_line_index] = f'            <a href="http://localhost:{sftp_port}"></a>\n'
            logging.info(f"SFTP link updated to: {html_lines[sftp_line_index].strip()}")
        else:
            logging.warning(f"Line {sftp_line_index} not found in HTML file!")

        try:
            with open(path_html_file, 'w') as file:
                file.writelines(html_lines)
            logging.info("index.html updated with the new SSH and SFTP ports.")
        except Exception as e:
            logging.error(f"Error updating HTML file: {e}")
    else:
        logging.warning(f"index.html doesn't exist at: {path_html_file}")

def monitor_config_changes(interval=5):
    """Monitor the config.yml file for changes and update if modified."""
    last_modified_time = os.path.getmtime(path_run_config)

    while True:
        time.sleep(interval)
        current_modified_time = os.path.getmtime(path_run_config)

        if current_modified_time != last_modified_time:
            last_modified_time = current_modified_time
            update_json_config_if_changed()

if __name__ == "__main__":
    monitor_config_changes()
