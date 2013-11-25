#computes the area of a triangle
def triangle_area(base, height):
	area = (1.0 / 2) * base * height
	return area

ans = triangle_area(3, 8)
print int(ans)

def f_to_c(f):
	c = (5.0 / 9) * (f - 32)
	return c

res = f_to_c(90)
print res
