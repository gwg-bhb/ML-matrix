#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-08-01 08:54
#@Author: daemon
#@File  : 4.py

import numpy as np
import  matplotlib.pyplot as plt

x=np.linspace(-1, 1, 100)
y=2*x*x+2
plt.plot(x,y)
plt.show()