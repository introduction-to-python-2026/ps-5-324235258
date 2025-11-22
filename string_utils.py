from fractions import Fraction
import sympy as sp

def balance_reaction(reaction):
    left, right = reaction.split("->")
    left = [m.strip() for m in left.split("+")]
    right = [m.strip() for m in right.split("+")]
    all_molecules = left + right

    # Count atoms
    atom_dicts = [count_atoms_in_molecule(m) for m in all_molecules]

    # Unique atoms
    atoms = sorted(set().union(*[d.keys() for d in atom_dicts]))

    # Build matrix
    rows = []
    for atom in atoms:
        row = []
        for i, molecule in enumerate(atom_dicts):
            count = molecule.get(atom, 0)
            if i < len(left):
                row.append(count)
            else:
                row.append(-count)
        rows.append(row)

    M = sp.Matrix(rows)

    # Nullspace
    ns = M.nullspace()[0]

    # Convert to Fractions
    coeffs = [Fraction(x) for x in ns]

    # Clear denominators
    lcm = abs(sp.lcm([c.denominator for c in coeffs]))
    coeffs = [c * lcm for c in coeffs]

    # Reduce by gcd
    gcd = sp.gcd([c.numerator for c in coeffs])
    coeffs = [c / gcd for c in coeffs]

    return coeffs
