from collections.abc import Callable


def fibonacci_decorator[Function: Callable[[int], None]](
	function: Function,
) -> Callable[[int], None]:
	def print_before_and_after(param: int) -> None:
		print('#### Avant fibonacci')
		function(param)
		print('#### Après fibonacci')

	return print_before_and_after


@fibonacci_decorator
def fibonacci(n: int) -> None:
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()
