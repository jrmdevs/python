from turtle import clear


total = 0
for number in range(100):
  total += number
  print(total)

for days in range(7):
  print("Day", days)

loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))

for i in range(1,11):
  print(i,"x 13 =",i*13)

for i in range(10,0,-1):
  print(i)

print("Example:")
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
for i in range(start,end,increment):
  print(i)
