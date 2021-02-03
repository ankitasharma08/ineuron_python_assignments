#1
x=np.array([2,4,6,8])

def geometricprogression(x):
    
    return np.vander(x, N=None, increasing=False)

geometricprogression(x)

#2

x = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
moving_average(x,3)