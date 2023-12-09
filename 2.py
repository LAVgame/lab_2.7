#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Заданные множества строк
    A = {'c', 'g', 'h', 'k', 'y'}
    B = {'a', 'b', 'k', 'n', 'u'}
    C = {'c', 'd', 'k', 'l', 'y'}
    D = {'a', 'g', 'h', 'u', 'v', 'z'}
    #u = {'a', 'b', 'c', 'd','e', 'f', 'g', 'h',
    #'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    #'s', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    g = set("abcdefghijklmnopqrstuvwxyz")
    # Операции с использованием union вместо or

    an = g.difference(A)

    Y = (an.intersection(D)).union(C.difference(B))
    X = A.intersection(B).union(C)

    # Вывод результатов
    print(f"Результат Y: {Y}")
    print(f"Результат X: {X}")