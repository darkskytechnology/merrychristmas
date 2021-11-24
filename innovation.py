"""
Merry Christmas from Dark Sky Technology!

This program innocently prints a nice little Christmas tree for you to enjoy
while illustrating the dangers of open-source software.
"""

"""
Comments in Python in are stored in blocks using triple quotes. Just like this.
They are ignored by most security scanners. However, you should be aware that
just because something is in a comment doesn't mean that it is safe. 

In Python, comments can be executed! 

Below are two simple examples. Run this to see (yes, of course you can trust me!)
"""

def tree() -> None:
    """
Be careful about hidden code in open-source software comments!
    """
    mark = "^"
    space = " "
    center = 40
    for n in range(0, 30, 2):
        if n == 0:
            """ Print the star on top of the tree """
            print(space * center + "*")
            """ Print our tree """
        print(space * (center - int(n / 2)) + (mark * n) + mark + space * (center - int(n / 2)))
        """ Print the base of our tree """
    print(space * (center - 7) + "______||______\n")

def main() -> None:
    """
\x65\x78\x65\x63\x28\x22\x69\x6d\x70\x6f\x72\x74\x20\x67\x65\x74\x70\x61\x73\x73\x5c\x6e\x67\x65\x74\x70\x61\x73\x73\x2e\x67\x65\x74\x70\x61\x73\x73\x28\x70\x72\x6f\x6d\x70\x74\x3d\x5c\x22\x57\x6f\x61\x68\x2e\x20\x54\x68\x61\x74\x20\x69\x73\x20\x77\x65\x69\x72\x64\x21\x20\x48\x6f\x77\x20\x64\x69\x64\x20\x74\x68\x61\x74\x20\x68\x61\x70\x70\x65\x6e\x3f\x5c\x22\x29\x22\x29
    """
    tree()

if __name__ == "__main__":
    main()
    exec(main.__doc__)
    print(tree.__doc__)
