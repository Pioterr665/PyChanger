#!/usr/bin/env python3
import os, sys, shutil
import subprocess as sp

#GTK4 Theme changer for Gnome DE

#Global variables
usr = os.getlogin()
theme_folder = f'/home/{usr}/.themes'
curr_dir = os.getcwd()
#Initialize program
def checkThemes():
    if os.path.exists(theme_folder):        
        os.chdir(theme_folder)
        print(os.getcwd())
        #print(os.listdir())
    else:
        os.mkdir(theme_folder)
        os.chdir(theme_folder)
        print(f"{os.getcwd()}")
        print('Folder z motywami jest pusty, pobierz motywy: https://www.gnome-look.org/browse?cat=135&ord=latest')
        
#List available themes
def themes():
    #init()
    os.chdir(theme_folder)
    theme_list = os.listdir()
    print('Available themes: ')
    for thm in theme_list:
        print(thm)
        
#Change theme 
def chtheme(themename):
    os.chdir(theme_folder)
    if not os.path.exists(f'/home/{usr}/.config/gtk-4.0'):
        shutil.copytree(f'{theme_folder}/{themename}/gtk-4.0', f'/home/{usr}/.config/gtk-4.0')
    else:
        os.rename(f'/home/{usr}/.config/gtk-4.0', f'/home/{usr}/.config/gtk-4.0.old')
        shutil.copytree(f'{theme_folder}/{themename}/gtk-4.0', f'/home/{usr}/.config/gtk-4.0')
    sp.run(f'gsettings set org.gnome.desktop.interface gtk-theme "{themename}"', shell=True)
    sp.run(f'gsettings set org.gnome.desktop.wm.preferences theme "{themename}"', shell=True)
    #sp.run(f'''dconf write /org/gnome/shell/extensions/user-theme/name '"{themename}"' ''', shell=True)

#Change Shell Theme
def shtheme(themename):
    os.chdir(theme_folder)
    sp.run(f'''dconf write /org/gnome/shell/extensions/user-theme/name '"{themename}"' ''', shell=True)

#set default theme
def default():
    sp.run(f'gsettings set org.gnome.desktop.interface gtk-theme "Adwaita"', shell=True)
    sp.run(f'settings set org.gnome.desktop.interface color-scheme "default"', shell=True)
    sp.run(f'''dconf write /org/gnome/shell/extensions/user-theme/name '"default"' ''', shell=True)
    os.remove(f'/home/{usr}/.config/gtk-4.0')
    os.rename(f'/home/{usr}/.config/gtk-4.0.old', f'/home/{usr}/.config/gtk-4.0')


def main():
    checkThemes()
    print('For help type --help')

  
if __name__ == "__main__":
    if '--help' in sys.argv:
        help_message = '''        --themes for list available themes
        --chtheme <THEME_NAME> for change theme
        --shtheme <THEME_NAME> for change shell theme
            '''
        print(help_message)
        sys.exit
    if '--themes' in sys.argv:
        themes()
        sys.exit()
    if '--chtheme' in sys.argv:
        _themename = sys.argv.index('--chtheme') + 1
        if _themename < len(sys.argv):
            chtheme(sys.argv[2])
        sys.exit()
    if '--shtheme' in sys.argv:
        _themename = sys.argv.index('--shtheme') + 1
        if _themename < len(sys.argv):
            shtheme(sys.argv[2])
        sys.exit()    
    if '--default' in sys.argv:
        default()
        sys.exit()

     
    main()
    
    
#few gsettings commands:

#1 gsettings set org.gnome.desktop.interface gtk-theme 'Adapta-Nokto-Eta'
# gsettings set org.gnome.desktop.interface cursor-theme 'Paper'
# gsettings set org.gnome.desktop.interface icon-theme 'Flat-Remix-Dark'
#2 gsettings set org.gnome.desktop.wm.preferences theme '_theme'

# gsettings set org.gnome.shell disable-user-extensions false
# gsettings set org.gnome.shell.extensions.user-theme name 'Adapta-Nokto'// this dont work now
#to change shell theme use:
# dconf write /org/gnome/shell/extensions/user-theme/name "'theme_name'"

# settings set org.gnome.desktop.interface color-scheme 'prefer-dark' for dark and default for white