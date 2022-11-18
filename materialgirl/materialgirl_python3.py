# first step is to generate questions
#!/usr/bin/env python3l

# created variabes 
material_girl= {
        "vehicle": " Luxury: gas_guzzlere",
        "Brunch": " Luxury: Yaht",
        "Shopping":"Luxury: Nordstrom",
        }

questions= {"Which would you choose?"}

vehicles= { "Luxury Gas Guzzler": True,
            "Tesla": True,
            "Hybrid": False,
            "American Sedan": False,}
            

Brunch= { "Yaht": True,
          "Steakhouse": True,
          "Ihop": False,
          "Broken Yoke": False,}

Shopping= {"Nordstrom": True,
           "Burlington " : False,
           "Neiman Marcus": True,
           "Ross": False,} 

# dictionaries above look good! here's what we need to do next.

# I added the following two lines, where we print out the car options and ask the user to provide input- choose a car
print(vehicles.keys())
answer= input("Which vehicle would you choose: ")

if vehicles[answer] == True: # I tweaked this line for you
        print ("Material Girl or Guy!")

#("vehicles",["Hybrid"]["American Sedan"])  # don't need this line, can be deleted              
if vehicles[answer] == False: # I tweaked this line too
       print ("Smart Guys/Gals Budget!")

# ^ so all the above will print the choices the user can make, asks them for input, then checks the dictionary to see if that key's value is True or False
# once you understand every change I made here, apply it to the sections you started below :)

("Brunch",["Yaht"]["Steakhouse"])

if True:
    print ("Material Girl or Guy!")

("Bruch",["Ihop"]["Broken Yoken"])
if False:

    print ("Food is Food!")
    
    

    #print the keys from that dictionary
# print a question, which would you choose?

# use an if to see if it returns true or false

# examples:
   # if vehicles[choice] == True:  material_girl_score +1... or print out "material girl!!"
   # elif vehicles[choice] == False: material_girl_score -1... or print out "not material girl!!"

   
                        
