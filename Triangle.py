"""Classifies Triangles based on the given side lengths side_a, side_b, side_c"""
def classify_triangle(side_a, side_b, side_c):
    """
    Parameters:
    side_a (int): triangle side a
    side_b (int): triangle side b
    side_c (int): triangle side c

    requires that the input values be >= 0 and <= 200
    verifies that all 3 inputs are integers
    verifies that the sum of any 2 sides is greater than the third side
    Python's "isinstance(object,type) returns True if the object is of the specified type

    Returns:
    string: Type of Triangle or 'Not a Triangle' or 'Invalid Input'
    """

    instance_list = [isinstance(side_a, int), isinstance(side_b, int), isinstance(side_c, int)]
    if (max(side_a, side_b, side_c) > 200 or min(side_a, side_b, side_c) < 0 or not instance_list):
        return 'Invalid Input'

    if ((side_a >= (side_b + side_c)) or (side_b >= (side_a + side_c))
            or (side_c >= (side_a + side_b))):
        return 'Not A Triangle'

    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if ((((side_a ** 2) + (side_b ** 2)) == (side_c ** 2)) or
            (((side_a ** 2) + (side_c ** 2)) == (side_b ** 2)) or
            (((side_c ** 2) + (side_b ** 2)) == (side_a ** 2))):
        return 'Right'
    if (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'
