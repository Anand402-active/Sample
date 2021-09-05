import first_module
# import first_module

print("name of the module is : {}".format(__name__))


# This will execute when executing current second module python file
def second():
    print("second_module is  executed because it called by current module :  {}".format(__name__))


# This condition is true while executing this python file
if __name__ == '__main__':
    second()
