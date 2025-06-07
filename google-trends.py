from pytrends.request import TrendReq
import matplotlib.pyplot as plt

#اتصال به گوگل ترندز
pytrends = TrendReq(hl="fa",tz=270)

#موضوعات مورد بررسی
keywords = ["همراه اول","ایرانسل","رایتل"]

#گرفتن داده از گوگل ترندز
pytrends.build_payload(keywords,timeframe="today 3-m",geo='IR')
#دادهای ترند
data = pytrends.interest_over_time()
#حذف ستون
if 'isPartial' in data.columns:
    data= data.drop(columns=['isPartial'])

#چاپ دادها
print(data.head())

#رسم نمودار ترند
plt.figure(figsize=(12,6))
for keyword in keywords:
    plt.plot(data.index,data[keyword], label=keyword)

plt.title("tahlil trend jostojo dar iran(3 month)",fontsize=14)
plt.xlabel("date")
plt.ylabel("search volume")
plt.legend()
plt.tight_layout()
plt.show()

