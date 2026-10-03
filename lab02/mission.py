# Joseph Naze - CIS109 - lab02

# welcome message
print('Welcome to the mission!')

# mission information
agent_name = input('Enter your agent name: ')
age = input('Enter your age: ')
training_years = input('How many years have you been training? ')
favorite_color = input('Enter your favorite color: ')
gadget_count = input('How many gadgets are you carrying? ')
minutes = input('How many minutes do you have? ')

#mission statistics
training_percentage = int(training_years) / int(age) * 100
gadget_density = int(gadget_count) / int(training_years) 
mission_seconds = int(minutes) * 60
mission_time_remaining = int(minutes) - 7

# mission code
mission_code = agent_name + '-' + favorite_color + '-' + age 

# boolean expressions
is_adult = int(age) >= 18
has_many_gadgets = int(gadget_count) >= 5 
has_training_experience = int(training_years) > 0 

#secret mission briefing
print(' ')
print('====================================')
print('        SECRET MISSION BRIEFING     ')
print('====================================')
print(' ')
print('Name:' , agent_name)
print('Mission Code:' , mission_code)
print(' ')
print('Age:' , int(age))
print('Training:' , int(training_years) , 'years')
print('Training Percentage:' , training_percentage , '%')
print(' ')
print('Gadgets:' , int(gadget_count))
print('Gadget Density:' , gadget_density , 'per training year')
print(' ')
print('Mission Time:' , int(minutes) , 'minutes')
print('Mission Time Remaining:' , int(mission_time_remaining) , 'minutes')
print('Mission Time in Seconds:' , int(mission_seconds))
print(' ')
print('Adult Agent:' , is_adult)
print('Many Gadgets:' , has_many_gadgets)
print('Training Experience:' , has_training_experience)
print(' ')
print('====================================')
print('        GOOD LUCK, AGENT!           ')
print('====================================')