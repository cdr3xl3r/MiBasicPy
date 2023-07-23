import os
from Config import conTheme as ctm
from sceneManager import sceneManager

'''#from dotenv import dotenv_values as dV
config = {
    **dV(".env.shared"),  # load shared development variables
    ** dV(".env.secret"),  # load sensitive variables
    ** os.environ,  # override loaded values with environment variables
}
#print(dV.__dir__())'''

def main(args=None):
    theme = ctm.defaultTheme
    sceneManager(theme)

print(os.environ.get('USERNAME',))
main()

