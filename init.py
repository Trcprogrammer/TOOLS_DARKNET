import subprocess as sb
import os 

options="""
[1]:Activate VPN
[2]:Desactivate VPNclear
[3]:search for links to the darknet/tor



"""

class shadownet:
    def __init__(self, options):
        self.options = options
        self.whois = ""
        self.shadownet = ""
        self.banner=""" 
` ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠤⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⢀⣀⣀⠀⠠⠤⢀⡑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠅⠒⠈⠉⠀⠀⠀⠀⢀⡀⠀⠘⡀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢠⣤⣄⡀⠀⢀⣴⡾⠛⠛⠓⠀⢱⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠉⣩⠻⠖⡘⠛⣴⣶⣦⣤⠴⢄⣧⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠾⠿⠿⠀⣾⡀⠉⠉⠁⠀⠀⠀⣿⠺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⢿⠇⢠⠠⠤⢠⡤⠂⢸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡠⣖⣁⣻⣶⣾⣥⣤⣴⣿⡏⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡻⡛⣉⣻⣿⡭⠄⢀⠞⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣌⠀⠈⣿⡇⠀⠈⡠⠪⠏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠙⢷⡤⠻⠇⠤⠊⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⡔⠁⢠⠀⠀⠙⠢⣀⠀⠀⠀⠀⣠⠇⢳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡀⠤⠀⠒⠊⠉⠀⠀⡇⠀⠘⡄⠀⠀⠀⠈⠑⢢⡤⢼⡁⠀⢸⠀⠉⢶⠠⢀⡀⠀⠀⠀⠀⠀
⡎⠁⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⢻⢦⠀⠀⠀⡴⠋⠀⠀⠙⡄⢸⡆⠀⠈⡄⠀⠈⠉⠐⠢⡄⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠃⠀⠀⠈⡄⠑⣄⡞⢆⠀⠀⢀⠜⠙⠊⢱⠀⠀⠘⡄⠀⠀⠀⠀⠘⡄
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠄⠀⠀⣧⠀⠈⠀⢰⠋⠁⠘⣄⠀⠀⠸⡄⠀⠠⠃⠀⠀⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠐⠀⠂⠒⠐⠒⠀⠀⠂⠒⠒⠒⠒⠐⠂⠒⠀⠒⠂⠀⠀⠀"""


    #in this part i put this selection the options
    def get_option(self):
        if self.options == "1":
            content_dark=input('Write the content that you want >')
            sb.call(['python3','dark.py','-q',f'{content_dark}'], cwd="get_dark/darkdump-main")


choose=input(">")
class_action=shadownet(choose)
while True:
    class_action.get_option()
