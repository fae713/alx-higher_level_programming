se_geometry module declaration """


class BaseGeometry:
    """ BaseGeometry class definition """

    def __init__(self):
        """An empty init constructor"""
        pass

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
