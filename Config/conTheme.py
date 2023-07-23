import configparser


filePath = 'Config/app/'
defaultTheme = 'guiThemeDefault.ini'
def conThemeInstaller():
    try:
        # import os
        # cur_path = os.path.dirname(__file__)
        filename = defaultTheme
        # os.path.relpath('..\\Config\\app\\guiThemeDefault.ini', cur_path)
        filePath = 'Config/app/'
        # instantiate
        config = configparser.ConfigParser()
        config.read(filename)
        # add a new section and some values
        config.add_section('DKMODE')
        config.set('DKMODE', 'UltraDark', 'gray4')
        config.set('DKMODE', 'Dark', 'gray14')
        config.set('DKMODE', 'Medium', 'gray24')
        config.set('DKMODE', 'Light', 'gray34')
        config.set('DKMODE', 'UltraLight', 'gray80')
        config.add_section('WIND')
        config.set('WIND', 'BG', 'gray14')
        config.set('WIND', 'FG', 'gray34')
        config.set('WIND', 'Geometry', "1600x1100+")
        with open(f'{filePath}{filename}', 'w') as file:
            config.write(file)
    except configparser.DuplicateSectionError:
        print('err')
    
def getTheme(theme,sec,opt):
    tFile = f"{filePath}{theme}"
    config = configparser.ConfigParser()
    config.read(tFile)
    var = config.get(sec, opt)
    return var   
#conThemeInstaller()
        
