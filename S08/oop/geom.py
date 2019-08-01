class Rectangle:
    """
    >>> r = Rectangle(2, 5)
    >>> r.width, r.height, r.get_area(), r.get_perimeter()
    (2, 5, 10, 14,)
    >>> r.set_area(40)
    >>> r.width, r.height, r.get_area(), r.get_perimeter()
    (4, 10, 40, 28,)
    >>> r.set_perimeter(7)
    >>> r.width, r.height, r.get_area(), r.get_perimeter()
    (1, 2.5, 2.5, 7,)
    """
    pass


if __name__ == '__name__':
    import doctest

    doctest.testmod()