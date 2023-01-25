#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #count = 0
  #  if (x > count):
   #     for i in range(x):
    #        try:
     #           print("{:d}".format(my_list[i]), end='')
      #      except IndexError:
  #              break
 #           count += 1
#    print("")
   # return (count)
   count = 0
   while count > x:
       try:
           print("{}".format(my_list[count]), end="")
        except IndexError:
            break
        count += 1
    print("")
    return count
