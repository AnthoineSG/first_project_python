from .src.car import get_car
from .src.env import check_env
from .src.fibo import fibonacci


def init() -> None:
	check_env()

	print('--------')

	fibonacci(2000)

	print('--------')

	get_car()
