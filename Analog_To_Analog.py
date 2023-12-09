#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09-12-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#AM
ac = 2
fc = 5
pc = 0

time = np.arange(0,10,.001)

carrier_signal = ac*np.sin(2*np.pi*fc*time + pc)

am = 0.2
fm = 0.8
pm = 0

massage_signal = am*np.sin(2*np.pi*fm*time + pm)

signal = carrier_signal * massage_signal


plt.subplot(3,1,1)
plt.title("Amplitude Modulation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(time,signal)
plt.grid(True)


#FM
ac = 2
fc = 5
pc = 0

time = np.arange(0,10,.001)

carrier_signal = ac*np.sin(2*np.pi*fc*time + pc)

am = 0.2
fm = 0.8
pm = 0

massage_signal = am*np.sin(2*np.pi*fm*time + pm)

frequency_modulation = ac*np.sin(2*np.pi*(fc+massage_signal)*time + pc)


plt.subplot(3,1,2)
plt.title("Frequency Modulation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(time,frequency_modulation)
plt.grid(True)



#PM
ac = 2
fc = 5
pc = 0

time = np.arange(0,10,.001)

carrier_signal = ac*np.sin(2*np.pi*fc*time + pc)

am = 0.2
fm = 0.8
pm = 0

massage_signal = am*np.sin(2*np.pi*fm*time + pm)

phase_modulation = np.sin(2*np.pi*fc*time + massage_signal)


plt.subplot(3,1,3)
plt.title("Phase Modulation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(time,phase_modulation)
plt.grid(True)

plt.tight_layout()
plt.show()
