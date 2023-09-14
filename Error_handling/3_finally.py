# Error Handling
while True:
    try:
        age = int(input('what is your age?'))
        print(10/age)
        raise ValueError('hey cut it out')
    except ValueError:
        print("Input is not integer")
    except ValueError:
        print("Please input integer")
    except ZeroDivisionError:
        print("Input is zero")
    else:
        print('thank you')
        break
    finally: # Runs ragrdless of whther there's an error or not
        print('ok I am finally done')

