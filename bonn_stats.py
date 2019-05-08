import numpy as np
import matplotlib.pyplot as plt

Z_data = np.loadtxt('bonnZ2totalhpp.txt')
S_data = np.loadtxt('bonnS2totalhpp.txt')
O_data = np.loadtxt('bonnO2totalhpp.txt')

Z_data[Z_data == 0] = 10e-310
S_data[S_data == 0] = 10e-310
O_data[O_data == 0] = 10e-310

print('Z sum: ', np.sum(np.log10(Z_data)))
print('S sum: ', np.sum(np.log10(S_data)))
print('O sum: ', np.sum(np.log10(O_data)))

print('Z std: ', np.std(np.log10(Z_data)))
print('S std: ', np.std(np.log10(S_data)))
print('O std: ', np.std(np.log10(O_data)))

print('Z max: ', np.min(np.log10(Z_data)))
print('S max: ', np.min(np.log10(S_data)))
print('O max: ', np.min(np.log10(O_data)))

print('S obsahuje epilepsii')
plt.figure(1)
plt.plot(np.cumsum(np.log10(Z_data)))
#plt.figure(2)
plt.plot(np.cumsum(np.log10(S_data)), 'k')
#plt.figure(3)
plt.plot(np.cumsum(np.log10(O_data)), 'r')
plt.show()