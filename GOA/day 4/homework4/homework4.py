# მომხმარებელს შეეკითხეთ ხელფასი

# თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?

# თუ 1000----10000 -ია , დაუპრინტეთ you mid

# თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

salary = int(input("input your salary here:"))

if salary >= 10000:
    print("გოა-ში სწავლობდი?")
elif salary>=1000 and salary < 10000:
    print("you mid")
elif salary<=1000 and salary>=0:
    print("შემოსულიყავი გოაში, მატრიცელო")
else:
    print("damn.")