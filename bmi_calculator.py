def main():
	height = raw_input("How tall are you (inches)? ")
	weight = raw_input("How much do you weight (in lbs)? " )
	bmi_raw = (float(weight)*703) / (float(height)**2)

	print "Your BMI is ", round(bmi_raw,2)

	if bmi_raw	< 15:
		print "This places you in the 'very severely underweight' (15.0-) category."
	elif bmi_raw >= 15 and bmi_raw < 16:
		print "This places you in the 'severely underweight' (15.0 - 16.0) category."
	elif bmi_raw >= 16.0 and bmi_raw < 18.5:
		print "This places you in the 'underweight' (16.0 - 18.5) category."
	elif bmi_raw >= 18.5 and bmi_raw < 25:
		print "This places you in the 'normal' (18.5 - 25.0) category."
	elif bmi_raw >= 25 and bmi_raw < 30:
		print "This places you in the 'overweight' (25.0 - 30.0) category."
	elif bmi_raw >= 30 and  bmi_raw < 35:
		print "This places you in the 'moderately obsese' (30.0 - 35.0) category."
	elif bmi_raw >= 35 and bmi_raw < 40:
		print "This places you in the 'severely obese' (35.0 - 40.0) category."
	elif bmi_raw >= 40:
		print "This places you in the 'very severely obese' (40.0+) category."

if __name__ == '__main__':
	main()