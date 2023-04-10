# i=1                                      1
# while i<5:                               2
#     j=1                                  3
#     while j<5:                           4
#         print(j)                        
#     i=i+1

# i=0
# while i<5:
#     j=1
#     while j<5:
#         print(j,end=" ")           1 2 3 4
#         j=j+1
#     print()
#     i=i+1

# i=1                  1
# while i<5:           1
#     j=1              1
#     while j<5:       1..........
#         j=j+1
#         print(i)
#     i=i+1            4


# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j)
#         j=j-1
#     i=i-1 
#     i=i-1

# i=1                               1
# while i<=5:                       1 2
#     j=1                           1 2 3
#     while j<=i:                   1 2 3 4
#         print(j,end=" ")          1 2 3 4 5
#         j=j+1
#     print()
#     i=i+1 

# i=5                               5
# while i>=1:                       5 4
#     j=5                           5 4 3
#     while j>=i:                   5 4 3 2
#         print(j,end="")           5 4 3 2 1
#         j=j-1
#     print()
#     i=i-1

# i=1
# while i<=5:                       5 4 3 2 1
#     j=5                           5 4 3 2
#     while j>=i:                   5 4 3
#         print(j,end="")           5 4
#         j=j-1                     5
#     print()
#     i=i+1

# i=5                              55555
# while i>=1:                      4444
#     j=1                          333
#     while j<=i:                  22
#         print(i,end="")          1
#         j=j+1
#     print()
#     i=i-1

# i=5
# while i>=1:                      55555
#     j=5                          44444
#     while j>=1:                  33333
#         print(i,end="")          22222
#         j=j-1                    11111
#     print()
#     i=i-1

# i=5
# while i>=1:                      12345
#     j=1                          1234
#     while j<=i:                  123
#         print(j,end="")          12
#         j=j+1                    1
#     print()
#     i=i-1

# i=5
# while i>=1:                      5
#     j=5                          44
#     while j>=i:                  333
#         print(i,end="")          2222
#         j=j-1                    11111
#     print()
#     i=i-1

# i=1
# while i<=6:                      54321
#     j=1                          4321
#     while j<=6-i:                321
#         print(6-j,end="")        21
#         j=j+1                    1
#     print()
#     i=i-1

# i=1                               1
# while i<=5:                       22
#     j=1                           333
#     while j<=i:                   4444
#         print(i,end="")           55555
#         j=j+1
#     print()
#