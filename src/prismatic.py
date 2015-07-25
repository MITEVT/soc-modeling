from battery import Battery
from custom_types import *

class PrismaticBattery(Battery):

	def __init__(self, capacity_ah, charge_curve, discharge_curve):
		super(PrismaticBattery, self).__init__(capacity_ah)
		self.charge_curve = charge_curve
		self.discharge_curve = discharge_curve
		self.mode = UsageMode.open_circuit

	def drawCurrent(self, amps, seconds):
		self.available_ah -= amps*(seconds/3600.0)
		self.available_ah = 0 if self.available_ah < 0 else self.available_ah

	def getVoltage(self):
		if (self.mode == UsageMode.open_circuit):
			self.mode = UsageMode.charging
			ch = self.getVoltage()
			self.mode = UsageMode.discharging
			di = self.getVoltage()
			self.mode = UsageMode.open_circuit
			return (ch + di) / 2
		elif (self.mode == UsageMode.charging):
			file = open(self.charge_curve, 'r')
		elif (self.mode == UsageMode.discharging):
			file = open(self.discharge_curve, 'r')

		soc = self.available_ah/self.capacity_ah
		dod = 1.0 - soc
		
		point = (0, 3.6)
		lastpoint = (0, 0)

		for l in file.readlines():
			tmp = l.split(',')
			lastpoint = point
			point = (float(tmp[0]), float(tmp[1])) # (dod, volts)
			if (float(tmp[0]) > dod):
				m = (point[1] - lastpoint[1])/(point[0] - lastpoint[0])
				b = point[1] - m*point[0]
				return m*dod+ b
		lastpoint = point
		point = (float(1), float(0)) # (dod, volts)
		m = (point[1] - lastpoint[1])/(point[0] - lastpoint[0])
		b = point[1] - m*point[0]

		return m*dod + b
