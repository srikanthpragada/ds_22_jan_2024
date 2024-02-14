import pickle 

f = open("lr_model.pickle","rb")
model = pickle.load(f)

gre = int(input("Enter GRE   : "))
tof = int(input("Enter Toefl : "))
cgpa = float(input("Enter CGPA : "))

result = model.predict([[gre,tof,cgpa]])
print(f"{result[0]:.2f}")
