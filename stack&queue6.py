# import sys
# input = sys.stdin.readline

# q = []
# N = int(input().strip())
# result = []

# for _ in range(N):
#     commandline = input().strip()
#     match commandline.split(" ")[0]:

#         case "1":
#             q.insert(0,commandline.split(" ")[1])
            

#         case "2":
#             q.append(commandline.split(" ")[1])

#         case "3":
#             if not q:
#                 result.append("-1")
#             else:
#                 result.append(q.pop(0))

#         case "4":
#             if not q:
#                 result.append("-1")
#             else:
#                 result.append(q.pop())

#         case "5":
#             result.append(str(len(q)))

#         case "6":
#             if not q:
#                 result.append("1")
#             else:
#                 result.append("0")

#         case "7":
#             if not q:
#                 result.append("-1")
#             else:
#                 result.append(q[0])

#         case "8":
#             if not q:
#                 result.append("-1")
#             else:
#                 result.append(q[-1])

# sys.stdout.write("\n".join(result))

import sys
input = sys.stdin.readline

N = int(input().strip())
dq = [0] * (2 * N)
front = rear = N
result = []
for _ in range(N):
    commandline = input().strip()
    match commandline.split(" ")[0]:

        case "1":
            front -= 1
            dq[front] = commandline.split(" ")[1]
            

        case "2":
            dq[rear] = commandline.split(" ")[1]
            rear += 1

        case "3":
            if front == rear:
                result.append("-1")
            else:
                result.append(dq[front])
                front += 1  
        case "4":
            if front == rear:
                result.append("-1")
            else:
                rear -= 1
                result.append(dq[rear])

        case "5":
            result.append(str(rear - front))

        case "6":
            if front == rear:
                result.append("1")
            else:
                result.append("0")

        case "7":
            if front == rear:
                result.append("-1")
            else:
                result.append(dq[front])

        case "8":
            if front == rear:
                result.append("-1")
            else:
                result.append(dq[rear - 1])

sys.stdout.write("\n".join(result))
