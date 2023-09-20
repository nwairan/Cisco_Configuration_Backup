```markdown
# Cisco Configuration Backup Script Manual

## Overview

The "Cisco Configuration Backup Script" is a Python script designed to automate the backup of Cisco device configurations. It connects to Cisco devices via SSH and retrieves their running configurations, saving them to separate files. This manual provides information on how to use the script effectively.

## Prerequisites

Before using the script, ensure that the following prerequisites are met:

1. **Python and Libraries**: The script requires Python 3.x and the `netmiko` library to be installed. You can install `netmiko` using `pip`:

   ```bash
   pip install netmiko
   ```

2. **Cisco Devices**: Ensure that the Cisco devices you want to back up are accessible via SSH. The devices should be properly configured for SSH access.

3. **Text File**: Prepare a text file containing a list of the IP addresses of the Cisco devices, one IP address per line.

## Usage

### Running the Script

To run the script, use the following command format:

```bash
python CBakcup.py <username> <password> <ip_file>
```

- `<username>`: Your SSH username for connecting to the Cisco devices.
- `<password>`: Your SSH password for connecting to the Cisco devices.
- `<ip_file>`: The path to a text file containing a list of IP addresses of the Cisco devices.

### Example

```bash
python CBakcup.py myusername mypassword ips.txt
```

### Script Execution

1. The script reads the list of IP addresses from the specified text file (`ips.txt` in the example).

2. For each IP address in the list, it attempts to connect to the Cisco device using SSH.

3. Upon successful connection, it retrieves the hostname and constructs a filename based on the hostname and IP address (e.g., `hostname_ip_.conf`).

4. It fetches the running configuration of the device using the "show running-config" command.

5. The running configuration is saved to a file with the format "hostname_ip_.conf" in the current working directory.

6. Any exceptions encountered during the process are printed to the console and logged in a log file named 'log.log'.

### Log File

The script logs any exceptions or errors encountered during execution in the 'log.log' file located in the same directory as the script.

## Troubleshooting

- **Authentication Issues**: Ensure that the provided username and password are correct, and the Cisco devices are properly configured for SSH access.

- **Missing Dependencies**: If you encounter missing library dependencies, make sure to install the `netmiko` library using `pip` (as mentioned in the prerequisites).

- **IP File Not Found**: If the script cannot find the specified IP file, double-check the file path and filename. Make sure it is in the same directory as the script or provide the full path.

- **Other Issues**: For any other issues or errors, refer to the console output and the log file ('log.log') for detailed error messages.

## Security Considerations

- Ensure that your username and password are kept secure and not exposed to unauthorized users.

- Consider using SSH keys for authentication to enhance security.

- Run the script in a controlled and secure environment.

## Conclusion

The "Cisco Configuration Backup Script" simplifies the task of backing up configurations from multiple Cisco devices. By following this manual and the provided usage instructions, you can efficiently automate the backup process and ensure that your configurations are safe and accessible when needed.
```
