#!/usr/bin/python3

def pascal_triangle(n):
    array = []
    if(n == 0):
        return array
    for i in range(n):
        i+=1
        if(i % 2 == 0):
            array.insert(int(len(array) / 2), i - 1)
            array.insert(int(len(array) / 2), i - 1)
            print(array)
        else:
            array2 = []
            w = i - 1
            if i == 1:
              array2.append(1)
            else:
              array2.append(1)
              array2.append(1)
              while len(array2) <= i - 1 and i % 2 != 0:
                  array2.insert(int(len(array2) / 2), w )
                  if len(array2) <= i - 1:
                      array2.insert(int(len(array2) / 2), w )
                  w += 1
                  if(w % 2 != 0):
                    w += 1

            print(array2)
