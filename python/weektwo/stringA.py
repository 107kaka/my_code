### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts! '
print s4

# Characters and slices
print s1[-2]
print len(s1)
print s1[0:10] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38

def convert(val):
        dollars = int(val)
        cents = int(100 * (val - dollars))
        return str(dollars) + " dollars and " + str(cents) + "cents"

# Tests
print convert(11.23)
print convert(11.20)
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)

print "========================================="

def convert_unit(val, name):
        result = str(val) + " " + name
        if val > 1:
            result = result + "s"
        return result

# Convert xx.yy to xx dollars and yy cents
def convertB(val):
        # Split into dollars and cents
        dollars = int(val)
        cents = int(round(100 * (val - dollars)))
                                                        
        # Convert to strings
        dollars_string = convert_unit(dollars, "dollars")
        cents_string = convert_unit(cents, "cent")

        # return composite string
        if dollars == 0 and cents == 0:
            return "Droke!"
        elif dollars == 0:
            return cents_string
        elif cents == 0:
            return dollars_string
        else:
            return dollars_string + " and " + cents_string
                                                                                                                                
# Tests
print convertB(11.23)
print convertB(11.20)
print convertB(1.12)
print convertB(12.01)
print convertB(1.01)
print convertB(0.01)
print convertB(1.00)
print convertB(0)
