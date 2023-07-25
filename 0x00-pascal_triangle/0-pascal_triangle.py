#!/usr/bin/python3

def pascal_triangle(n):
    triangle = []
    if(n <= 0): return triangle
    for row in range(n):
        current_row = [1]
        if triangle:
            prev_row = triangle[-1]
            for i in range(len(prev_row) - 1):
                current_row.append(prev_row[i] + prev_row[i + 1])
            current_row.append(1)
        triangle.append(current_row)

    return(triangle)
ine = int(input("Enter: "))
print(pascal_triangle(ine))
