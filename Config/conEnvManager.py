from cgi import print_arguments
import os
from dotenv import dotenv_values

config = {
    **dotenv_values('..\\MiBasicPy\\Config\\Env\\.secret.env'),
    **dotenv_values('..\\MiBasicPy\\Config\\Env\\.shared.env'),
    **os.environ
}

print(config.items())
