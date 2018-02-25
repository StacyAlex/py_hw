import json
import csv
import random

class SuperDict(dict):

    def __init__(self, inj):

        if(isinstance(inj, dict)):#ежели инициализируем словарем
            self.elemlist = dict(inj.items())
            #print('init:', self.elemlist)

        elif (isinstance(inj, str)):#ежели json
            if (inj.endswith('.json')):

                with open(inj, 'r') as js:
                    tmpd = json.load(js)
                self.elemlist = tmpd
                #print('init:', self.elemlist)

            elif (inj.endswith('.csv')):#csv

                with open(inj, 'r') as js:
                    reader = csv.reader(js)
                    self.elemlist = {}

                    for row in reader:
                        self.elemlist.update({row[0]:row[1]})

                    #print('init:', self.elemlist)
##############################################################         переделать
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
            

d = {'a':'8', 'b':'9'}
sd1 = SuperDict(d)
sd2 = SuperDict('C:/Users/User/PycharmProjects/test/venv/inits.json')
sd3 = SuperDict('C:/Users/User/PycharmProjects/test/inits.csv')

print("sd1:", sd1, "\nsd2:", sd2, "\nsd3:", sd3)
print("__getitem__():", sd1.__getitem__('b'))

sd2.clear()
print("clear():", sd2)

print("items():", list(sd3.items()))
print("keys():", list(sd3.keys()))
print("values():", list(sd3.values()))
print("iteritems():", sd3.iteritems())
print("iterkeys():", sd3.iterkeys())
print("itervalues():", sd3.itervalues())
print("__iter__():", sd3.__iter__())
print("__eq__():", sd1 == sd2)
print("__len__():", sd3.__len__())

print("get_random_key():", sd3.get_random_key())
print("max_key_len():", sd3.max_key_len())
print("__add__():", sd3 + sd1)

sd3.to_csv("C:/Users/User/PycharmProjects/test/outfile.csv")

