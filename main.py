import pandas as pd

population = pd.read_csv("population.csv", index_col="country")
print(population.sort_values("population",ascending=False).head(10))
#플롯 꾸미기
import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np
matplotlib.style.use('bmh')
_, ax = plt.subplots(2,2)
s = np.arange(0,10)
t = np.random.randint(1,10,10)
r = np.random.randint(1,10,100)
ax[0,0].bar(s,t)
ax[0,1].scatter(s,t)
ax[1,0].hist(r)
ax[1,1].pie(t)
plt.show()
#플롯 꾸미기
import matplotlib.pyplot as plt
import numpy as np
cities = ["Seoul", "Busan", "Daejeon"]
y = np.arange(2000, 2020, dtype=int)
min, max = 0, 0
for c in cities:
 t = np.random.randn(20).cumsum()
 plt.plot(y, t, "o-")
 plt.annotate(s=c, xy=(2020, t[19]))
 if min > t.min(): min = t.min()
 if max < t.max(): max = t.max()
plt.axis([1999, 2024, min
-1, max+3])
plt.title("City growth")
plt.xlabel("year")
plt.ylabel("population")
plt.legend(cities)
plt.show()
