print("name of the module is :  {}".format(__name__))


# This method will execute while executing this python file
def first():
    print("first_module is  executed because it called by current module :  {}".format(__name__))


# This condition will be true while running this python file if false else will execute
if __name__ == '__main__':
    first()
else:
    print("first_module is called from another python module first function wont execute")
