# QUESTION:there is n seats in a row.you are given a string s with length n ; for each valid i,the i'th character of s is '0' if the i'th seat is empty or '1' if there is someone sitting in that seat. t wo people are friends if they are sitting next to each other. two friends are always are part of the same group of friends . can you find the number of groups? using python
#ANS:
print("How much time you want to do the operation\n")
time_to_do_operation = int(input())
for _ in range(time_to_do_operation):
    print("\n!!Enter the sitting sequence!!\n")
    base=input()
    arrangement = [int(i) for i in base ]
    groups = 0
    if arrangement[0] == 1:
        groups += 1

    for i in range(1, len(arrangement)):
        rev = True
        if arrangement[i] == 1:
            if arrangement[i - 1] != 1:
                groups += 1


    print("Number of groups are",groups)

# t = int(input())
# for i in range(t):
#         b = input()
#
#         c = 0
#         for i in range(len(b)):
#             if b[i] == '0' and b[i - 1] == '1' and i != 0:
#                 c += 1
#
#         if b[-1] == '1':
#             c += 1
#         print(c)