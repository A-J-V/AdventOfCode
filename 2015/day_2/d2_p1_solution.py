
def paper_calc(dimensions: str) -> int:
    l, w, h = (int(_) for _ in dimensions.split("x"))
    s1 = l * w
    s2 = w * h
    s3 = h * l
    slack = min([s1, s2, s3])
    surface = (2 * s1) + (2 * s2) + (2 * s3)
    return surface + slack

with open(r"./d2_input.txt", "r") as f:
    input = f.read()

paper = 0
for line in input.splitlines():
    paper += paper_calc(line)
print(f"The elves need {paper} sqft of wrapping paper.")

