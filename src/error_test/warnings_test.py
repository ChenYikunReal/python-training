import warnings


# d = r × t
def rtd(distance=None, rate=None, time=None):
    if distance is None:
        distance = rate * time
    elif rate is None:
        rate = distance / time
    elif time is None:
        time = distance / rate
    else:
        warnings.filterwarnings("Nothing to solve for")
    return dict(distance=distance, rate=rate, time=time)


result = rtd(distance=31.2, rate=6)
print(result)
