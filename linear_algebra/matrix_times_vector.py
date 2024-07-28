"""
Matrix times Vector (easy)
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10]
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
"""


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:

    vec_dims = len(b)
    res = []

    if any(len(row) != vec_dims for row in a):
        return -1

    for row in a:
        dot_product = sum((row[i] * b[i] for i in range(vec_dims)))
        res.append(dot_product)
    return res
