#Wadati diagram with arriving time of P wave
import numpy as np
import matplotlib.pyplot as plt

tp = np.float_([54.65, 57.34, 00.49, 01.80, 01.90, 02.25, 03.10])
ts = np.float_([57.90, 62.15, 07.55, 10.00, 10.10, 10.70, 12.00])
td = ts-tp

x = tp
y = td

plt.title("Wadati diagram of the earthquake")
plt.xlabel("Arriving time of P wave, $t_p (s)$")
plt.ylabel("$t_s - t_p (s)$")
plt.scatter(x, y, color ="red")
plt.xlim()
plt.ylim(0,10)
plt.show()
