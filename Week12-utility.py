# Michael Rickert
# CSCI 102
# Week 12 Lab Whatever

def hello_world():
    print('OUTPUT Hello World')


hello_world()


def LoadFile(filename):

    filename = open(str(input('File')), 'r')
    lines = filename.readlines()
    txt_list = [lines]
    print('OUTPUT', txt_list)


LoadFile('')
