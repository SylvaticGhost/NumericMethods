def system_of_equations_to_string(system):
    string_builder = ""
    for i in range(len(system)):
        string_builder += str(system[i]) + " = 0\n"

    return string_builder