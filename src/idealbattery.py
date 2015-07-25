from battery import Battery

class IdealBattery(Battery):

	def __init__(self, capacity_ah, nominal_voltage):
		super(IdealBattery, self).__init__(capacity_ah)
		self.nominal_voltage = nominal_voltage

	def drawCurrent(self, amps, seconds):
		self.available_ah -= amps*(seconds/3600.0)
		self.available_ah = 0 if self.available_ah < 0 else self.available_ah

	def getVoltage(self):
		return 0 if self.available_ah <= 0 else self.voltage

	def getAvailableAh(self):
		return self.available_ah

	def getAvailableWh(self):
		return self.available_ah * self.nominal_voltage