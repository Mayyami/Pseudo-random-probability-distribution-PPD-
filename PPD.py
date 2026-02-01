from C import compute_c
import datetime
def random(first, second):
  if not isinstance(first, int) or not isinstance(second, int):
    raise ValueError("Both arguments must be integers")
  date_now = str(datetime.datetime.now())[-6:]
  date_now = str(datetime.datetime.now())[-6:]
  integer_for_gen = int(date_now + date_now)
def pseudo_random():
  countt = int(input("Enter the number of random cases:"))
  random_cases =[]
  for i in range(countt):
    print("Enter constant",i + 1,"random case:")
    x = int(input())
    random_cases.append(x)
  random_cases2 = random_cases
  retry = int(input("Enter the number of retries:"))
  for i in range (retry):
    for j in range(len(random_cases)):
      break
n = int(input())
print(f"C для {n}%: {compute_c(n/100):.5f}")