from first_project.src.fibo import fibonacci


decorator_before = '#### Avant fibonacci\n'
decorator_after = '#### Après fibonacci\n'


class TestFibonacci:
	def test_return(self):
		assert fibonacci(1000) is None

	def test_fibonacci(self, capsys):
		# ! Test 0 - Return "\n"
		fibonacci(0)
		capturedSystem = capsys.readouterr()
		expected_result = '\n'
		assert (
			capturedSystem.out
			== f'{decorator_before}{expected_result}{decorator_after}'
		)

		# ! Test 10 - Return "0 1 1 2 3 5 8 \n"
		fibonacci(10)
		capturedSystem = capsys.readouterr()
		expected_result = '0 1 1 2 3 5 8 \n'
		assert (
			capturedSystem.out
			== f'{decorator_before}{expected_result}{decorator_after}'
		)

		# ! Test 2000 - Return "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 \n"
		fibonacci(2000)
		capturedSystem = capsys.readouterr()
		expected_result = '0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 \n'
		assert (
			capturedSystem.out
			== f'{decorator_before}{expected_result}{decorator_after}'
		)
