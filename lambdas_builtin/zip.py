midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['stan', 'maciek', 'edek']

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

final_grades_dict = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)
print(final_grades_dict)


# interleave('hi', 'ha')  # 'hhia'
def interleave(str1, str2):
    zipped = zip(str1, str2)
    return ''.join([''.join(x) for x in zipped])
