import logging

logging.basicConfig(filename="Task6.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Creating Class for string Operations

class Str_t6:
    def __init__(self, input_str):
        self.input_str = input_str
        logging.info("This is string operations")

    def str_extraction(self):
        '''Try to extract data from index one to index 300 with a jump of 3 '''

        try:
            logging.info(f"The input i have given is {self.input_str}")
            r = self.input_str[1:300:3]
            logging.info(f"The output is {r}")
            return r


        except Exception as e:
            logging.error("This is an exception block: ", e)

    def rev_notreverse(self):
        '''Try to reverse a string without using reverse function '''

        try:
            logging.info(f"The input i have given is {self.input_str}")
            r = self.input_str[::-1]
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def up_str(self):
        '''Try to split a string after conversion of entire string in uppercase '''

        try:
            logging.info(f"The input i have given is {self.input_str}")
            r = self.input_str.upper().split(' ')
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def low_str(self):
        '''try to convert the whole string into lower case '''

        try:
            logging.info(f"The input i have given is {self.input_str}")
            r = self.input_str.lower()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def capti_str(self):
        '''Try to capitalize the whole string '''

        try:
            logging.info(f"The input i have given is {self.input_str}")
            r = self.input_str.capitalize()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def IsAlphaNum(self, str):

        '''Try to check alpha-numeric characters '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.isalnum()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def Alpha(self, str):

        '''Try to check alphabetic characters '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.isalpha()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def Expantab(self, str):

        '''Try to give an example of expand tab '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.expandtabs()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def rmspace(self, str):

        '''Try to remove white spaces '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.strip()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def Lrmspace(self, str):

        '''Try to remove Left white spaces '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.lstrip()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def Rrmspace(self, str):

        '''Try to remove right white spaces '''

        try:
            logging.info(f"The input i have given is {str}")
            r = str.rstrip()
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def replc(self, str, str1, str2):

        '''Try to replace one character by another '''

        try:
            logging.info(f"The input i have given is {str}")
            logging.info(f"I want to change{str1} by {str2}")
            r = str.replace(str1, str2)
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)

    def centru(self, str, num, num1):

        '''Try to centre my string by the given digits'''

        try:
            logging.info(f"The input i have given is {str}")
            logging.info(f"I want to center the string by{num}")
            r = str.center(num, num1)
            logging.info(f"The output is {r}")
            return r

        except Exception as e:
            logging.error("This is an exception block: ", e)


# Creating Class for list Operations

class lst_t6:
    def __init__(self, l):
        self.l = l
        logging.info("This is list operations")

    def lst_reverse(self):
        '''This function will reverse the list provided.'''

        try:
            logging.info(f"This is my try block and the list I have entered is{self.l}")
            l1 = l[::-1]
            logging.info(f"The output is {l1}")
            return l1

        except Exception as e:
            logging.error(e)

    def lst_outof_list(self, lst):
        self.lst = lst
        '''Try to extract all the list entity.'''

        try:
            l1 = []
            logging.info(f"try blog is initiated and input is {self.lst}")
            for i in self.lst:
                if type(i) == list:
                    l1.append(i)
            logging.info(f"The output is {l1}")
            return l1

        except Exception as e:
            logging.error(e)

    def tup_outof_list(self, lst):
        self.lst = lst
        '''Try to extract all the tuple entity'''

        try:
            l1 = []
            logging.info(f"Input is {self.lst}")
            for i in self.lst:
                if type(i) == tuple:
                    l1.append(i)
            logging.info(f"The output is {l1}")
            return l1
        except Exception as e:
            logging.error(e)

    def num_outof_list(self, lst):
        self.lst = lst
        '''Try to extract all the numerical date, it may be a part of dictionary key and values.'''

        try:
            l1 = []
            logging.info(f"Input is {self.lst}")
            for i in self.lst:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
            logging.info(f"The output is {l1}")

            return l1

        except Exception as e:
            logging.error(e)

    def sum_numdata(self, lst):
        self.lst = lst
        '''Try to extract all the numerical date, it may be a part of dictionary key and values and provide the sum.'''

        try:
            l1 = []
            logging.info(f"Input is {self.lst}")
            for i in self.lst:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
            logging.info(f"The output is {l1} and sum is " + str(sum(l1)))

            return sum(l1)

        except Exception as e:
            logging.error(e)

    def odd_numdata(self, lst):
        self.lst = lst
        '''Try to filter out all the odd values out of all numeric data which is a part of a list.'''

        try:
            l1 = []
            logging.info(f"Input is {self.lst}")
            for i in self.lst:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
            logging.info(f"The numeric data we got is {l1}")

            if not l1 == []:
                l_odd = []
                for i in l1:
                    if i % 2 == 1:
                        l_odd.append(i)
            logging.info(f"The odd data extracted is {l_odd}")

            return l_odd


        except Exception as e:
            logging.error(e)

    def occ_data(self, lst):
        self.lst = lst
        '''Try to find out the no. of occurences of all the data.'''

        try:
            l1 = []
            logging.info(f"Input is {self.lst}")
            for i in self.lst:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        l1.append(j)
                if type(i) == dict:
                    l1.extend(list(i.keys()) + list(i.values()))
            logging.info(f"The complete data we got is {l1}")

            l2 = set(l1)
            l3 = []
            for i in l2:
                a = i, l1.count(i)
                l3.append(a)

            logging.info(f"The right hand side is the occurence of data viz {l3}")

            return l3


        except Exception as e:
            logging.error(e)


# Creating Class for dictionary Operations

class dict_t6:

    def __init__(self, l2):
        self.l2 = l2


    def dec_data(self, l):
        self.l = l
        '''This function will extract all the dictonary data and put it into one list'''

        try:
            lst = []
            logging.info(f"The input data is{self.l}")
            for i in self.l:
                if type(i) == dict:
                    lst.extend(list(i.keys()))
                    lst.extend(list(i.values()))
            logging.info(f"the output data is {lst}")
            return lst

        except Exception as e:
            print(e)



    def no_of_keys(self,l):
        self.l = l
        '''Try to find out no. of keys in dict element.'''

        try:
            key= []
            logging.info(f"The input value is {self.l}")
            for i in self.l:
                if type(i) == dict:
                    key.append(len(i))
            logging.info(f"The no of keys in a dictionary is {key}")
            return key

        except Exception as e:
            print(e)


#Creating class for tuple operations

class tuple_t6:
    def __init__(self,l):
        self.l = l

    def tup_entity(self,l):
        self.l = l
        '''Try to extract all the tuple entity'''

        try:
            lst_tuple = []
            logging.info(f"the input value is {self.l}")
            for i in self.l:
                if type(i) == tuple:
                    lst_tuple.append(i)
            logging.info(f"The output value is {lst_tuple}")
            return lst_tuple

        except Exception as e:
            print(e)



# Creating class for set operations

class set_t6:
    def __init__(self, l):
        self.l = l

    def set_entity(self, l):
        self.l = l
        '''Try to extract all the set entity'''

        try:
            lst_set = []
            logging.info(f"the input value is {self.l}")
            for i in self.l:
                if type(i) == set:
                    lst_set.append(i)
            logging.info(f"The output value is {lst_set}")
            return lst_set

        except Exception as e:
            print(e)




# String operations

obj = Str_t6("I am trying to learn Python")
print(obj.str_extraction())
print(obj.rev_notreverse())
print(obj.up_str())
print(obj.low_str())
print(obj.capti_str())
print(obj.IsAlphaNum("456456454"))
print(obj.Alpha("happyme"))
print(obj.Expantab("I am always the best\tand also the santury\t sdjfkdj"))
print(obj.rmspace("            dkf jkdjfkjdkfjdkfjkdjfkd                "))
print(obj.Lrmspace("            dkf jkdjfkjdkfjdkfjkdjfkd                "))
print(obj.Rrmspace("            dkf jkdjfkjdkfjdkfjkdjfkd                "))
print(obj.replc("hello money finder", "money", "paisa"))
print(obj.centru("Abhishek_Dave", 90,"@"))


# List Operations

l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]
l1 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
      {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

ver = lst_t6(l)
print(ver.lst_reverse())
print(ver.lst_outof_list([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"sudh", 'k2': "ineuron", 'k3': "kumar", 3:6, 7:8}, ["ineuron", "data science"]]))
print(ver.tup_outof_list(l1))
print(ver.num_outof_list(l1))
print(ver.sum_numdata(l1))
print(ver.odd_numdata(l1))
print(ver.occ_data((l1)))


# Dictionary Operations

l1 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

variable = dict_t6(l1)

print(variable.dec_data(l1))
print(variable.no_of_keys(l1))


#Tuple Operations

l1 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

tup = tuple_t6(l1)
print(tup.tup_entity(l1))


# set operations

varset = set_t6(l1)
print(varset.set_entity(l1))
