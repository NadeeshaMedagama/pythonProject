class Car:

    wheels = 4;
    def __init__(self, type, model, year, color):
        self.type = type
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This", self.type ,"is driving")

    def stop(self):
        print("This", self.model ,"is stopping")
