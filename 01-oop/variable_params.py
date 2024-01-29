
def my_function(value, *args, **kwargs):
    print(value)
    print(args)
    print(kwargs)


my_function(5, 7, 8, 9, 10, 11, color="gray", 
            temperature=36.6, coutry="GR")