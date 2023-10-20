
def get_value(): 
   color1 = input("Enter the color band1:")
   color2= input("Enter the color band2:")
   color3= input("Enter the color band3:")
   color4= input("Enter the color band4:")

   colors = [
      color1, color2,color3,color4
   ]
   return colors
   

def validate_input(color):
   valid_colors = {
      "blk":0, "brn":1, "rd":2, "org":3, "yel":4,  
      "grn":5, "blu":6, "vil":7, "gry":8, "whi":9,
      "gld":5, "slv":10
   }
   if color in valid_colors:
      return valid_colors[color]
   else:
      print(f"invalid color {color}")
      return None
   
def check_num_validity( num1, num2,num3,num4):
   if num1 is None or num2 is None or num3 is None or num4 is None :
      print("one or more values are bad")
      return False
   else:
      return True
   
   

   
   

def calculate_value(num1,num2,num3,num4):
   is_valid = check_num_validity(num1,num2,num3,num4)
   if not is_valid:
      print("Invalid input supplied, Resistance cannot be calculated")
      return None
   
   sub_total = num1 * 10 + num2
   total_value = sub_total * 10**num3
   percentage_value=get_percentage(num4,total_value)
   upper_value = total_value + percentage_value
   lower_value = total_value - percentage_value
   print(f"resistance value is between {upper_value}ohm and {lower_value}ohm ")


 
def get_percentage(num4,total_value):
   resistance = (num4/100) * total_value 
   return resistance





def give_hint():
   print("Below are the abbreviation of the color code Resistor")
   print("Input the abbreviation to get the Resistance value of the Resisitor ")


   print("black =blk")
   print("brown = brn")
   print("red = rd")
   print("orang = org")
   print("yellow = yel")
   print("green = grn")
   print("blue = blu")
   print("violet = vil")
   print("grey = gry")
   print("white = whi")
   print("gold = gld")
   print("sliver = slv")
   

give_hint()
my_colors = get_value()
first_color,second_color,third_color,fourth_color = my_colors
print(f"first color is: {first_color}")
print(f"second color is: {second_color}")
print(f"thrid color is: {third_color}")
print(f"fourth color is: {fourth_color}")
first_color_number = validate_input(first_color)
second_color_number = validate_input(second_color)
third_color_number = validate_input(third_color)
fourth_color_number = validate_input(fourth_color)
print(f"first color number is: {first_color_number}")
print(f"second color number is: {second_color_number}")
print(f"thrid color number is: {third_color_number}")
print(f"fourth color number is: {fourth_color_number}")
result=calculate_value(first_color_number,second_color_number,third_color_number,fourth_color_number)



#print(f"first clolor is: {my_colors[0]}")
#print(f"second clolor is: {my_colors[1]}")
# my_input = Valid_input()




    
    




           


       
   
   

   
   
       
       


    













    
    







    