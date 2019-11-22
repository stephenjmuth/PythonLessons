


def build_profile(first,last,**user_info):
    for k,v in user_info.items():
        print(k,v)
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('stephen','muth',
    employer='oracle',
    children='too many')

print(user_profile)
for k,v in user_profile.items():
    print(k,v)

################################################
print(f"\nCar Build funtion:\n")

def build_car(man,mod,**options):
    for k,v in options.items():
        print(k,v)
    options['manufacturer']=man
    options['model']=mod
    car=options
    return car

car = build_car('subaru', 'outback', color='blue', tow_package=True)

print(car)