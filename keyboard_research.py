import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10))
df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(120,16), kind="bar")
plt.show()
data = trends.trending_searches(pn="india")
print(data.head(10))

keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
print(data.head())

