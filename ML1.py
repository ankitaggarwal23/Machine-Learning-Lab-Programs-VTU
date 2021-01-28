import csv

num_at = 6;
print("No of atrributes :", num_at)

a = []
print("\n Given Train Data: ")

with open('enjoysport.csv', 'r') as csvfile:
  read = csv.reader(csvfile)
  for row in read:
    a.append(row)
    print(row)

print("\n Inital value of hypothesis: ")
hypothesis = ['0'] * num_at
print(hypothesis)
print("\n")

for i in range(0, len(a)):
    if a[i][num_at] == 'yes':
        for j in range(0, num_at):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print(" For Training Example No : {0} the hypothesis is " .format(i), hypothesis)

print("\n Maximum specific hypothesis for a given training examples :\n")
print(hypothesis)