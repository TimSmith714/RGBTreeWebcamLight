from tree import RGBXmasTree
from time import sleep
from cmd import Cmd

# Had to do  pip3 install rpi.gpio

tree = RGBXmasTree()

bottomRow = [0,16,15,6,12,24,19,7]
middleRow = [1,17,14,5,11,23,20,8]
topRow = [2,18,13,4,10,22,21,9]
star = [3]
rows = [bottomRow, middleRow, topRow, star]
colorStep = 0.0039
r = 0.1
g = 0.1
b = 0.1
brightness = 0.1
debug = True

tree.color = (r,g,b)
tree.brightness = brightness

class RGBTreeLight(Cmd):

    #do_greet(self, line):
    print("Welcome to the RGBXmasTree Webcam utility")
    print("=========================================")
    print("Upper case increases, lowercase decreases")
    print("L:brightness, R:red, G:green, B:blue")
    print("w: resets colour to white using red level")


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
            tree.color = (tree.color[0] + 0.1, tree.color[1], tree.color[2])
        if debug:
            print("Colour: " + str(tree.color[0]) + "," + str(tree.color[1]) + "," + str(tree.color[2]) + "," )

    def help_R(self):
        print("Makes red brighter by 10%")

    def do_r(self, inp):
        print("Less Red")
        if tree.color[0] > 0:
            tree.color = (tree.color[0] - 0.1, tree.color[1], tree.color[2])
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

RGBTreeLight().cmdloop()
