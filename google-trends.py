from pytrends.request import TrendReq
import matplotlib.pyplot as plt

#
pytrends = TrendReq(hl="fa",tz=270)

#
keywords = ["همراه اول","ایرانسل","رایتل"]

#
pytrends.build_payload(keywords,timeframe="today 3-m",geo='IR')
#
data = pytrends.interest_over_time()
#
if 'isPartial' in data.columns:
    data= data.drop(columns=['isPartial'])

#
print(data.head())

#
plt.figure(figsize=(12,6))
for keyword in keywords:
    plt.plot(data.index,data[keyword], label=keyword)

plt.title("tahlil trend jostojo dar iran(3 month)",fontsize=14)
plt.xlabel("date")
plt.ylabel("search volume")
plt.legend()
plt.tight_layout()
plt.show()

