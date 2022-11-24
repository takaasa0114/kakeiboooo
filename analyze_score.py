scores=[90,86,78,64,57,62,87,82,90,95,86]

N=len(scores)
total=0
best=0
for i in range(N):
    total+=scores[i]
    if scores[i]>=best:
        best=scores[i]

avarage=total/N
print("平均は"+str(avarage)+"点")
print("最高得点は"+str(best)+"点")

rb=[]
for i in range(N):
    if scores[i]<avarage:
        rb.append(scores[i])


print(len(rb))
