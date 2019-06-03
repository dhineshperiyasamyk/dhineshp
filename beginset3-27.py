j = input ()

try:

	val=float(j)

	print("yes")

except ValueError:

	try:

		val=int(j)

		print("yes")

	except ValueError:

		print("No")
