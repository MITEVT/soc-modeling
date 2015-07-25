#!/usr/bin/python

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
from idealbattery import IdealBattery
from prismatic import PrismaticBattery
from custom_types import *


VSOC_CHARGE = '../data/vsoc_charge.txt'
VSOC_DISCHARGE = '../data/vsoc_discharge.txt'

bat = PrismaticBattery(20, VSOC_CHARGE, VSOC_DISCHARGE)
bat.mode = UsageMode.discharging
bat.drawCurrent(20, 60)
print bat.getVoltage()




