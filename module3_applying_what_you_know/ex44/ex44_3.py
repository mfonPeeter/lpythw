# a closure is any function that is created inside another function but accesses data in its parent.

# this function makes functions
def constructor(color, size): 
    print(">>> constructor color: ", color, "size: ", size)

    def repeater():
        # notice this function is using color, size
        print('### repeater color: ', color, "size: ", size)

    print("<<< exit constructor")
    return repeater

# what's returned are repeater functions
blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

# see how these repeaters "know" the parameters?
for i in range(0, 4):
    blue_xl()
    green_sm()