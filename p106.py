day,month,year=[int(i) for i in input().split()]
JMM = ((14 - month) // 12)
JMY = (year + 4800 - JMM)
JMD = day - 32045 + (((month + 12 * JMM - 3) * 153 + 2) // 5) + (JMY * 365) + (JMY // 4) - (JMY // 100) + (JMY // 400)
res = JMD % 7
ans=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(ans[res])