
def split_before_uppercases(formula):
    if not formula:
        return []
    split_formula = []
    start = 0
    for end in range(len(formula)):
        if end != start and formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_digit(formula):
   digit_location = 0
    while digit_location < len(formula) and not formula[digit_location].isdigit():
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    start_digit = digit_location
    while digit_location < len(formula) and formula[digit_location].isdigit():
        digit_location += 1
    prefix = formula[:start_digit]
    number = int(formula[start_digit:digit_location])
    return prefix, number


def count_atoms_in_molecule(molecular_formula):
   atom_counts = {}
   split_formula = split_before_uppercases(molecular_formula)
    for formula_part in split_formula:
        atom, count = split_at_digit(formula_part)
        if atom in atom_counts:
            atom_counts[atom] += count
        else:
            atom_counts[atom] = count
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
