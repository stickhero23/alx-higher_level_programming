#!/usr/bin/python3
def safe_print_integer(value):
    try :
<<<<<<< HEAD
        print("{:d}".format(int(value)))
        return True
    except:
        return False
=======
        print("{:d}".format(value))
    except:
        return False
    else:
        return True
>>>>>>> 33f292c37e90dc11706688931d374ee9bb126fea
