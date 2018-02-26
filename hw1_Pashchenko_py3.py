import json
import csv
import random
import os
import sys

class SuperDict(dict):

    def __init__(self, inj):

        if(isinstance(inj, dict)):# ежели инициализируем словарем
            self.elemlist = dict(inj.items())
            #print('init:', self.elemlist)

        elif (isinstance(inj, str)):#   ежели json
            if (inj.endswith('.json')):

                self.elemlist = {}
                with open(inj, 'r') as js:

                    for line in js:
                        tmpd = json.loads(str(line))
                        self.elemlist.update(tmpd)

                #print('init:', self.elemlist)

            elif (inj.endswith('.csv')):#   csv

                with open(inj, 'r') as js:
                    reader = csv.reader(js)
                    self.elemlist = {}

                    for row in reader:
                        if len(row) > 2:
                            print("------\nerror occured: too many columns in .csv file. invalid string ignored.\n------")
                            #next(reader)
                        else:
                            self.elemlist.update({row[0]:row[1]})

                    #print('init:', self.elemlist)
        else:
            print("initialization error")

############################################################## - ниже "старые" методы
    def __getitem__(self, item):
        return self.elemlist.__getitem__(item)

    def __str__(self):#Для перегрузки вывода
        return str(self.elemlist)

    def clear(self):
        self.elemlist.clear()

    def items(self):
        return self.elemlist.items()

    def keys(self):
        return self.elemlist.keys()

    def values(self):
        return self.elemlist.values()

    def iteritems(self):
        return iter(self.elemlist.items())

    def iterkeys(self):
        return iter(self.elemlist.keys())

    def itervalues(self):
        return iter(self.elemlist.values())

    def __iter__(self):
        return self.elemlist.__iter__()

    def __eq__(self, other):#сравниваю не сущности, а значения, так и задумано
        return self.elemlist == other.elemlist

    def __len__(self):
        return self.elemlist.__len__()

################################################################# - ниже "новые" методы

    def get_random_key(self):#возвращает рандомный ключ, не более того
        temp = list(self.keys())
        r = random.randint(0, self.__len__() - 1)
        return temp[r]

    def max_key_len(self):
        temp = list(self.keys())
        ctr = 0
        for i in temp:
            if (str(i)).__len__() > ctr:
                ctr = (str(i)).__len__()
        return ctr

    def __add__(self, other):
        self.elemlist.update(other.elemlist)
        return self

    def to_csv(self, adr):
        with open(adr, 'w') as ofile:
            writer = csv.writer(ofile)
            writer.writerows(list(self.items()))

    def to_json(self, adr):
        with open(adr, 'w') as ofile:
            json.dump(self.elemlist, ofile)

    def get_key_starts_from(self, word):
        temp = list(self.keys())
        for i in range(0, self.__len__()):
            if temp[i].startswith(word):
                print("selected keys:", temp[i])

                
print("enter full path to your initialization file as a string:")
tstr = input()

sd = SuperDict(tsrt)

#############################################################################   file_tree function:

def file_tree(path, file_filter = None):

    for root, subdirs, files in os.walk(path):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')
        print('list_file_path = ' + list_file_path)
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                if file_filter is None:
                    print('\t- file %s (full path: %s)' % (filename, file_path))
                else:
                    if str(filename).endswith(file_filter):
                        print('\t- file %s (full path: %s)' % (filename, file_path))

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                    list_file.write(f_content)
                    list_file.write(b'\n')

#file_tree("C:/Users/User/Desktop/Kursuch/CurseSuch", "ue.pdf")
#file_tree("C:/Users/User/Desktop/Kursuch/CurseSuch")
