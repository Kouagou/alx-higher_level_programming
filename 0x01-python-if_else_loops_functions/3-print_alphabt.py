#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if ('{:c}'.format(i) != 'e') and ('{:c}'.format(i) != 'q'):
        print('{:c}'.format(i), end='')
