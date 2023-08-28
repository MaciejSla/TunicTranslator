import glob

for file in glob.glob("../runes/*black.svg"):
    f = open(file, "rt")
    data = f.read()
    data = data.replace("#000000", "#b4b4b4")
    f.close()

    file = file.replace("black", "gray")
    f = open(file, "wt")
    f.write(data)
    f.close()
