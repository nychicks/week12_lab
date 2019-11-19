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


# loadfile('')


def UpdateString(string,letter,num):
    string_list = list(string)
    string_list[num] = letter
    print(string_list)


def FindWordCount(word_list, word_to_find):
    word_list = []
    with open('sample_file.txt', 'r') as f:
        for line in f:
            for word in line.split():
                word_list.append(word)

    print('OUTPUT> ', word_list.count(word_to_find))



# a = str(input('Word>'))
# FindWordCount('', a)

def scorefinder(list1,list2,string):
    print(list1,list2,string)

scorefinder(['mike','jill','amy'], [2,3,4,4,5,5], '')


def union(list1,list2):
    union_list = list1 + list2
    return union_list

list1 = [5,8,10,6,4]
list2 = ['Melvin','Martian','Baka', 'Xai','Cody']
print(union(list1,list2))












