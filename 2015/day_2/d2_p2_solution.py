def ribbon_calc(dimensions: str) -> int:
    l, w, h = (int(_) for _ in dimensions.split("x"))
    p1 = 2 * (l + w)
    p2 = 2 * (w + h)
    p3 = 2 * (h + l)
    bow = l * w * h
    wrapping = min(p1, p2, p3)
    return bow + wrapping

with open(r"./d2_input.txt", "r") as f:
    input = f.read()

ribbon = 0
for line in input.splitlines():
    ribbon += ribbon_calc(line)
print(f"The elves need {ribbon} feet of ribbon.")
