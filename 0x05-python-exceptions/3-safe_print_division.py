def safe_print_division(a, b):
    inside_result = 0
    try:
        inside_result = (a / b)
    except:
        inside_result = None
    finally:
        print("Inside result: {}".format(inside_result))
    return (inside_result)
