from netmiko import ConnectHandler
from getpass import getpass
import re
from jinja2 import Environment, FileSystemLoader
import sys

# Load Jinja2 environment (looks for templates in current directory)
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('asr9kroutingfo.j2')

#render interface input
INTERFACE = sys.argv[1]
output = template.render(INTERFACE=INTERFACE)

#print output
print(output)