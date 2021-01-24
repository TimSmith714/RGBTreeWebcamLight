from tree import RGBXmasTree
from time import sleep
from cmd import Cmd
import configparser

# Had to do  pip3 install rpi.gpio

#Init the tree 
tree = RGBXmasTree()
# Set up the rows legacy by might be helpful
bottomRow = [0,16,15,6,12,24,19,7]
middleRow = [1,17,14,5,11,23,20,8]
topRow = [2,18,13,4,10,22,21,9]
star = [3]
rows = [bottomRow, middleRow, topRow, star]
colorStep = 0.0039

#Import config
config = configparser.ConfigParser()
# Try and load config
config.read('config.ini')
# Check for contents
#print("Config Length: " + str(len(config)))

if len(config) == 1:
    # Empty so set the defaults
    print("No Config file found")
    config['COLOURS'] = { 'r': 0.1, 'g': 0.1, 'b': 0.1, 'brightness': 0.1 }
    config['ADVANCED'] = { 'debug': True }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    config.read('config.ini')


# Load the config settings
r = float(config['COLOURS']['r'])
g = float(config['COLOURS']['g'])
b = float(config['COLOURS']['b'])
brightness = float(config['COLOURS']['brightness'])
debug = config['ADVANCED']['debug']

# Apply the default from the config file
tree.color = (r,g,b)
tree.brightness = brightness

# Define colour change function

def updateColour(colour, change):
        # colour: String
        # change: float
        if colour == 'r':
            tree.color = (round(tree.color[0] + change,1), tree.color[1], tree.color[2])
        elif colour == 'g':
            tree.color = (tree.color[0], round(tree.color[1] + change,1), tree.color[2])
        elif colour == 'b':
            tree.color = (tree.color[0], tree.color[1], round(tree.color[2] + change,1))
        # Finally show the colour if in debug
        if debug:
            print(tree.color)

class RGBTreeLight(Cmd):

    #do_greet(self, line):
    print("Welcome to the RGBXmasTree Webcam utility")
    print("=========================================")
    print("Upper case increases, lowercase decreases")
    print("L:brightness, R:red, G:green, B:blue")
    print("w: resets colour to white using red level")
    print("save: save settings to config file")

    print("Starting")

    # Brightness

    def do_L(self, inp):
        print("Brighter")
        if tree.brightness < 1:
            tree.brightness = tree.brightness + 0.1
        if debug:
            print("Brightness: " + str(tree.brightness))

    def help_L(self):
        print("Makes brighter by 10%")

    def do_l(self, inp):
        print("Darker")
        if tree.brightness > 0:
            tree.brightness = tree.brightness - 0.1
        if debug:
            print("Brightness: " + str(tree.brightness))
    
    def help_l(self):
        print("Makes darker by 10%")

    # Red

    def do_R(self, inp):
        print("More Red")
        if tree.color[0] < 1:
            updateColour('r',0.1)
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )

    def help_R(self):
        print("Makes red brighter by 10%")

    def do_r(self, inp):
        print("Less Red")
        if tree.color[0] > 0:
            updateColour('r',-0.1)
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )
    
    def help_r(self):
        print("Makes Red darker by 10%")

    # Green

    def do_G(self, inp):
        print("More Green")
        if tree.color[1] < 1:
            tree.color = (tree.color[0], tree.color[1] + 0.1 , tree.color[2])
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )

    def help_G(self):
        print("Makes green brighter by 10%")

    def do_g(self, inp):
        print("Less Green")
        if tree.color[1] > 0:
            tree.color = (tree.color[0], tree.color[1] - 0.1, tree.color[2])
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )
    
    def help_g(self):
        print("Makes green darker by 10%")

    # Blue

    def do_B(self, inp):
        print("More Blue")
        if tree.color[1] < 1:
            tree.color = (tree.color[0], tree.color[1], tree.color[2] + 0.1 )
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )

    def help_B(self):
        print("Makes Blue brighter by 10%")

    def do_b(self, inp):
        print("Less Blue")
        if tree.color[1] > 0:
            tree.color = (tree.color[0], tree.color[1], tree.color[2] - 0.1)
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )
    
    def help_b(self):
        print("Makes Blue darker by 10%")

    # Reset color to White

    def do_w(self, inp):
        print("Setting to white at reds brightness")
        tree.color = (tree.color[0],tree.color[0],tree.color[0])

    def help_w(self):
        print("Set to White at reds brightness")

    # App Controls

    def help_exit(self):
        print("Sets the lights to 0 and quits")

    def do_exit(self, inp):
        '''exit the application'''
        tree.color = (0,0,0)
        print("Quitting")
        return True

    def help_QuickGuide(self):
        print("Upper case increases, lowercase decreases")
        print("L:brightness, R:red, G:green, B:blue")
        print("w: resets colour to white using red level")

    def do_save(self, inp):
        config['COLOURS'] = { 'r': tree.color[0], 'g': tree.color[1], 'b': tree.color[2], 'brightness': tree.brightness }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print("Settings Saved")

    def help_save(self):
        print("Save the current settings to the config file")

RGBTreeLight().cmdloop()


