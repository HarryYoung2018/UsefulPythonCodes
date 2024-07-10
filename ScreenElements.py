def screen_elements(S):
    """
    Input: string in English

    Output: string with letters adapted to periodic table elements
    """
    elements = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]

    e=[i.lower() for i in elements]
    s=S.lower()
    for i in range(len(s)):
        for j in range(len(e)):
            if i+1<=len(s)-1 and len(e[j])==2:
                if s[i:i+2]==e[j]:
                    s=s[:i]+elements[j]+s[i+2:]
                    i+=2
            elif s[i]==e[j]:
                s=s[:i]+elements[j]+s[i+1:]
    return s

if __name__ == "__main__":
    S=input()
    print(screen_elements(S))