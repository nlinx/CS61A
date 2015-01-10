from lab10 import * 

###########
# Streams #
###########

def make_fib_stream():
    return fib_stream_generator(0, 1)

def fib_stream_generator(a, b):
    return Stream(a, lambda: fib_stream_generator(a, a+b))
    
x = make_fib_stream()


def filter_stream(filter_func, stream):
    def make_filtered_rest():
        return filter_stream(filter_func, stream.rest)
    if Stream.empty:
        return stream
    elif filter_func(stream.first):
        return Stream(stream.first, make_filtered_rest)
    else:
        return filter_stream(filter_funct, stream.rest)

def find(stream, predicate):
    "*** YOUR CODE HERE ***"

def interleave(stream1, stream2):
    if stream1 is Stream.empty:
        return Stream.empty
    return Stream(s1.first, lambda: interleave(s2.rest, s1))

