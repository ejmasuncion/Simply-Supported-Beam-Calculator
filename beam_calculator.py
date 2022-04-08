"""Simply Supported Beam Reaction Calculator"""

print("Welcome to Beam Calculator")

length = float(input("Input the length of the beam (m): "))

#Variable inputs
loads_point = {}
loads_distributed = {}
add_more_loads = True
total_force = 0
cw_moment = 0

#Addition of Point Loads
def add_point_load():
    number_of_point_load = int(input("How many point loads? "))
    for i in range(number_of_point_load):
        force = float(input("What is the force of the load (kN)?: "))
        location = float(input("Where is the force located from 0m (m): "))
        if location > length:
            print("location is not within beam length")
            location = float(input("Where is the force located from 0m (m): "))
        loads_point[f'P{i+1}'] = {'force': force, 'location': location}
#Addition of Distributed Loads
def add_distributed_load():
    number_of_distributed_load = int(input("How many distributed loads do you want? "))
    for i in range(number_of_distributed_load):
        udl = float(input("What is the force of the load (kN/m)?: "))
        start = float(input("Where is the start of distributed located from 0m (m): "))
        udl_length = float(input("How long is the distributed load (m): "))
        if start + udl_length > length:
            print("distributed load exceeded the beam length")
            udl_length = float(input("How long is the distributed load (m): "))
        lever_arm = udl_length / 2 - start
        loads_distributed[f'P{i+1}'] = {'force': udl, 'length': udl_length, 'lever_arm': lever_arm}

while add_more_loads:
    choice = input("Do you want to add a Point load? (y/n) ")
    if choice == 'y':
        add_point_load()
    elif choice == 'n':
        choice_2 = input("Do you want to add distributed load? (y/n) ")
        if choice_2 == 'y':
            add_distributed_load()
        else:
            add_more_loads = False


# Solving Total Moment
for j in range(len(loads_point)):
    moment = loads_point[f'P{j+1}']['force'] * loads_point[f'P{j+1}']['location']
    cw_moment += moment

for k in range(len(loads_distributed)):
    moment = loads_distributed[f'P{k+1}']['force'] * loads_distributed[f'P{k+1}']['length'] * loads_distributed[f'P{k+1}']['lever_arm']
    cw_moment += moment

# Solving Total Force
for l in range(len(loads_point)):
    force = loads_point[f'P{l+1}']['force']
    total_force += force 

for m in range(len(loads_distributed)):
    force = loads_distributed[f'P{m+1}']['force'] * loads_distributed[f'P{m+1}']['length']
    total_force += force 


reaction_2 = cw_moment / length
reaction_1 = total_force - reaction_2

print(f'The reaction of support at left side is {reaction_1}')
print(f'The reaction of support at right side is {reaction_2}')