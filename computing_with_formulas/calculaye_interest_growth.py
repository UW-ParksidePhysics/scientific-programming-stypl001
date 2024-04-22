# 3 year rate as of March 28 2024 was 4.40%

P = 4.40
n = 3
A = 1000
FV = A * ( 1 + (P/100))**n

Growth = FV - A

print(f' Initial investment: ${A:3.2f} ' )
print(f' Interest rate: {P:3.1f}%')
print(f' The growth is ${Growth:.2f}')
