def do_stuff(num):
    try:
        if num!=None:
            return int(num)*5
        else:
            return "please enter a number"
    except ValueError as err:
        return err