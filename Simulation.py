import numpy as np
import numpy_financial as nf
import pandas

# List to store yearly amounts in savings and investments
# Each row is a new "case", ie row 1 is case 1
A=np.zeros((5000,5))
# Open text file 
# Pick a random line and convert it to a float value 
# Set mu, sigma, and n 
# Generate n random samples from a Normal distn with mu and sigma
for k in range(0,1000):
	with open("C:/Users/taylo/Desktop/Math 377/Project/5yr.txt") as data: 
		lines=data.readlines()
		mean=(np.random.choice(lines))
		mean=float(mean)
		annual=(1+mean)**(1/5)-1 
		mu,sigma,n=annual,0.12,5 
		samples=np.random.normal(mu,sigma,n)
	#print(samples)

	# Temp list to store the XI values 
	PV_values=[]

	# Calculate the XI values 
	# Note: XI is (500*(risk/100)
	def calculate_PV(risk): 
		out = np.zeros(5)
		i = 0
		PV = 0
	    
		for rate in samples:
			PV = -1*(nf.fv(rate/12,12,(500*(risk/100)),PV,when=1))
			out[i] = PV
	#		print(PV)
			i = i+1
	#	print(out)    
		return out

	# Define S(t) 
	# Note: XS is (100 - Contribution Risk)% * 500
	# Note: first term goes to 0 as S0=0 
	def S(t,XS):
		return XS*(((1+(0.01/12))**(12*t)-1)/(0.01/12))

	# Case 1: 
	for t in range(1,6): 
		result = calculate_PV(25)
		A[5*k][t-1]=S(t,(100-25)*5)+ result[t-1]

	# Case 2: 
	for t in range(1,6): 
		result = calculate_PV(50)
		A[5*k+1][t-1]=S(t,(100-50)*5)+ result[t-1]

	# Case 3: 
	for t in range(1,6): 
		result = calculate_PV(65)
		A[5*k+2][t-1]=S(t,(100-65)*5)+ result[t-1]
	 
	# Case 4: 
	for t in range(1,6): 
		result = calculate_PV(80)
		A[5*k+3][t-1]=S(t,(100-80)*5)+ result[t-1]

	# Case 5: 
	for t in range(1,6): 
		result = calculate_PV(100)
		A[5*k+4][t-1]= result[t-1]

data=pandas.DataFrame(A)
data.to_excel("C:/Users/taylo/Desktop/Math 377/Project/Math377Simulations.xlsx")