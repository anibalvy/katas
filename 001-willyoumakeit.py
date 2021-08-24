def zero_fuel(distance_to_pump, mpg, fuel_left):
    # 25 mile per Galon
    # mpg 1
    # x   fuel_left
    return True if mpg*fuel_left >= distance_to_pump else False



zero_fuel(50,25,2)
zero_fuel(100,50,1)
