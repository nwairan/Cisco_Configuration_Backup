import json
import netmiko
import time

def main(username, password, ip_file):
    try:
        with open(ip_file, 'r') as ip_file:
            ips = ip_file.read().splitlines()

        logfile = 'log.log'
        log = open(logfile, mode='a+')

        for ip in ips:
            try:
                print(ip)
                connection = netmiko.ConnectHandler(
                    ip.strip(), device_type='cisco_ios',
                    username=username, password=password
                )
                connection.secret = ''
                connection.enable()
                hostname = connection.send_command("show running-config | include hostname").replace('hostname ', '')
                hostname = hostname.rstrip("\n")
                print(hostname)
                filename = hostname + "_" + ip + "_.conf"
                configuration = connection.send_command("show running-config")
                fileIO = open(filename, mode='w')
                fileIO.write(configuration)
                fileIO.close()
                connection.disconnect()
            except Exception as e:
                print(str(e))
                log.write(str(e))
        log.close()
    except FileNotFoundError:
        print(f"IP file '{ip_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Provide the username, password, and path to the IP file as command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <ip_file>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        ip_file = sys.argv[3]
        main(username, password, ip_file)
