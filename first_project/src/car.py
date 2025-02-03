from typing import LiteralString

from ..utils.query import query_int, query_yes_no

Wheels = int
Air_con = bool | str
Doors = int


class Car:
	def __init__(self, wheels: Wheels, air_con: Air_con, doors: Doors):
		self.wheels = wheels
		self.air_con = air_con
		self.doors = doors

	def __str__(self) -> LiteralString:
		air_con = self.has_clim()
		return f'La voiture a {self.wheels} roues, {air_con}, {self.doors} portes'

	def has_clim(self) -> str:
		if self.air_con:
			return 'elle a la clim'
		else:
			return "elle n'a pas la clim"


def get_car() -> None:
	print("Let's talk about your car")

	car_wheels = query_int('How many wheels does it have? ')
	car_air_con = query_yes_no('Does it have air conditioning ?')
	car_doors = query_int('How many doors ? ')

	result = Car(wheels=car_wheels, air_con=car_air_con, doors=car_doors)

	return print(result)
