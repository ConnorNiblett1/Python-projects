import math

while True:

    try:
        #Switch to determine what type of calculation needs to be run. 
        data_type = input("Please select the type of information avaliable:\n(A) Base and Height\n(B) Three Side Lengths\n(C) Two Sides and an Angle...\n ")
        if data_type.lower() == 'a':
            #Triangle Area formula is condition a.
            base = input("Please enter the triangle's base:\n")
            height = input("Please enter the triangle's height:\n")
            base = float(base)
            height = float(height)
            #The two if statements below make sure the provided numbers are within range
            if base <= 0:
                raise ValueError ("Please enter a number greater than zero for both variables")
            if height <= 0:
                raise ValueError ("Please enter a number greater than zero for both variables")  
            result = base * 0.5 * height
        elif data_type.lower() == 'b':
            #Heron's Formula is condition b.
            side_a = float(input("Side length A:\n"))
            side_b = float(input("Side length B:\n"))
            side_c = float(input("Side length C:\n"))
            semi_perimeter  = (side_a + side_b + side_c)/2.0
            result = math.sqrt(semi_perimeter*(semi_perimeter - side_a)*(semi_perimeter - side_b)*(semi_perimeter - side_c))

        elif data_type.lower() == 'c':
            #SAS Area Formula is condition c.
            angle = float(input("Please enter the given angle:\n"))
            side_a = float(input("Please enter side length A:\n"))
            side_b = float(input("Please enter side length B:\n "))
            result = 1.0/2.0*side_a*side_b*math.sin(math.radians(angle))
            
    
    except ValueError as err:
        print(err)
        continue
    except:
        print("Error encountered! Please make sure your equation has been entered correctly, and does not evaulate to a negative number.")
    else:
        break
print("The Area of the specified triangle is:", round(result,3) )    
