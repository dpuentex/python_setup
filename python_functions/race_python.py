class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)


myCar.talk('Michael')


class Race:
  def __init__(self, track, number_laps):
    self.track = track
    self.number_laps = number_laps

  def lights(self, track):
    print(f"LIGHTS OUT AT {track}!!!")
 
  def intro(self, track, number_laps):
    print(f"Welcome to {track} where we will have a {self.number_laps} race!!! ")

imola = Race("Imola", 43)
vegas_gp = Race("LV-Circuit", 55)

imola.lights("Imola")

vegas_gp.intro("vegas")