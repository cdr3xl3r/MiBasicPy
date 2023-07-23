import os
from Config import conTheme as ctm
from sceneManager import sceneManager
import time 

'''#from dotenv import dotenv_values as dV
config = {
    **dV(".env.shared"),  # load shared development variables
    ** dV(".env.secret"),  # load sensitive variables
    ** os.environ,  # override loaded values with environment variables
}
#print(dV.__dir__())'''

def main():
    sTime = time.asctime() # type: ignore
    theme = ctm.defaultTheme
    user = os.environ.get('USERNAME',)
    sceneManager(theme,f'User: {user} Login@: {sTime}')

print(os.environ.get('USERNAME',))
main()

