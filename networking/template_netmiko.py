from getpass import getpass
from netmiko import ConnectHandler

input_username = input("Username: ")
input_password = getpass("Password: ")


device = ConnectHandler(device_type='cisco_ios',
                        ip='192.168.1.1',
                        username=input_username,
                        password=input_password)
output = device.send_command('show hostname')
print(output)
device.disconnect()
