# Michael Rickert
# CSCI 102
# Week 12 Lab Whatever

def hello_world():
    print('OUTPUT Hello World')


hello_world()


def loadfile(filename):

    filename = open(str(input('File')), 'r')
    lines = filename.readlines()
    txt_list = [lines]
    print('OUTPUT', txt_list)


loadfile('')


def UpdateString(string,letter,num):
    string_list = list(string)
    string_list[num] = letter
    print(string_list)


def FindWordCount(word_list, a):
    d = {}
    word_list = []
    a = str(input('WORD>'))
    with open('sample_file.txt', 'r') as f:
        for line in f:
            for word in line.split():
                word_list.append(word)
        for word in word_list:
            if word not in d:
                d[word] = 0
            d[word] += 1
    print(d)

FindWordCount('','')











