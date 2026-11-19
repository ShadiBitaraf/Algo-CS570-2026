def generate_input_strings(file_path):
    """
    Read two base strings and expand each using its insertion indices.
    """

    with open(file_path, encoding="utf-8") as file:
        lines = [line.strip() for line in file]

    # get the line index of the second string t_0 in the file
    second_start = next(
        i for i in range(1, len(lines))
        if not lines[i].isdigit()
    )

    # apply insertion indices in order, doubling the string each time
    def expand(base, indices):
        for index in indices:
            split = int(index) + 1
            base = base[:split] + base + base[split:]
        return base

    # Each base string uses only the numeric lines that follow it.
    s_j = expand(lines[0], lines[1:second_start])
    t_k = expand(lines[second_start], lines[second_start + 1:])

    return s_j, t_k
