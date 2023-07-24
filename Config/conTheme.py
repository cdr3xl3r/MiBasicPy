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
        config.add_section('DK_MODE')
        config.set('DK_MODE', 'UltraDark', 'gray4')
        config.set('DK_MODE', 'Dark', 'gray14')
        config.set('DK_MODE', 'Medium', 'gray24')
        config.set('DK_MODE', 'Light', 'gray34')
        config.set('DK_MODE', 'UltraLight', 'gray80')
        config.add_section('WIND')
        config.set('WIND', 'BG', 'gray14')
        config.set('WIND', 'FG', 'gray34')
        config.set('WIND', 'Geometry', "1600x1100+")
        config.add_section('FONT')
        config.set('FONT', 'mainFont', "MS Outlook")
        config.set('FONT', 'Light', 'gray14')
        config.set('FONT', 'Dark', 'gray54')
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
conThemeInstaller()
        
