class Car(object):
    def __init__(self, model, company, color, speedLimit, horsePower):
        self.model = model
        self.company = company
        self.color = color
        self.speedLimit = speedLimit
        self.horsePower = horsePower

    def start(self):
        print("The Car Has Started")

    def stop(self):
        print("The Car Has Stopped")

    def accelerated(self):
        print("The Car Is Accelerating...")

RoolsRoyce = Car("R2","RR","White","100 KM/HR","440 KW")
Lamborghini = Car("L2","LB","Yellow","250 KM/HR","480 KW")
Bugati = Car("Sheron","BS","Lime Green", "200 KM/HR","460 KW")

print(RoolsRoyce.model)
print(RoolsRoyce.company)
print(RoolsRoyce.color)
print(RoolsRoyce.speedLimit)
print(RoolsRoyce.horsePower)
print(RoolsRoyce.start())
print(RoolsRoyce.stop())
print(RoolsRoyce.accelerated())

print(Lamborghini.model)
print(Lamborghini.company)
print(Lamborghini.color)
print(Lamborghini.speedLimit)
print(Lamborghini.horsePower)
print(Lamborghini.start())
print(Lamborghini.stop())
print(Lamborghini.accelerated())

print(Bugati.model)
print(Bugati.company)
print(Bugati.color)
print(Bugati.speedLimit)
print(Bugati.horsePower)
print(Bugati.start())
print(Bugati.stop())
print(Bugati.accelerated())