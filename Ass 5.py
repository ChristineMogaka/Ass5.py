print("Enter [P] to see available options") 

def the_options():
    print('Options')
    print("[C] Convert from Celsius")
    print("[F] Convert from Fahrenheit")
    print("[M] Convert from Miles")
    print("[KM] Convert from Kilometers")
    print("[IN] Convert from Inches")
    print("[CM] Convert from Centimeters")

conversion = True
#Convert from Celcius to Fahrenheit
while conversion:
    user_input = str.upper(input("Option: "))

    if user_input == 'P':
        the_options()

    elif user_input == 'C':
        def celsius():
            cel = float(input("Enter Temperature in Celsius units: "))
            calc_cel = (cel*1.8) +32
            print(calc_cel)
        celsius()

#Convert Fahrenheit to Celcius

    elif user_input == 'F':
        def fahrenheit():
            fer = float(input("Enter Temperature in Fahrenheit units: "))
            calc_fer = (fer-32) *5/9
            print(calc_fer)
        fahrenheit()
   
#Convert from Miles to Kilometers

    elif user_input == 'M':
        def miles():
            ml = float(input("Enter distance in Miles: "))
            calc_ml = ml*1.6
            print(calc_ml)
        miles()

#Convert from Kilometers to Miles 

    elif user_input == 'KM':
        def kilometers():
            km = float(input("Enter distance in Kilometers: "))
            calc_km = km/1.6
            print(calc_km)
        kilometers()

#Convert from Inches to Centimeters 

    elif user_input == 'IN':
        def inches():
            inc = float(input("Enter Length in Inches: "))
            calc_inc = inc*2.54
            print(calc_inc)
        inches()

#Convert from Centimeters to Inches

    elif user_input == 'CM':
        def centimeters():
            cm = float(input("Enter Length in Centimeters: "))
            calc_cm = cm/2.54
            print(calc_cm)
        centimeters()

    elif user_input == 'Q':
        convertion = False
        break
    else:
        convertion = False

    