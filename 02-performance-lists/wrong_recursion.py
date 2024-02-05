# RecursionError: maximum recursion depth exceeded

def wrong(n):
    return wrong(n+1)

wrong(1)