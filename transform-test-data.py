path = "pid-tests/transformed-data/pid-test-26.txt"

cleaned_data = []

with open(path, "r") as f:
    for line in f:
        if line.startswith("PHYSICAL MOVEMENT"):
            continue
        line = line.strip()
        line = line.replace('Target: ', '')
        line = line.replace('Angle: ', '')
        line = line.replace('Error: ', '')
        line = line.replace('Output: ', '')
        line = line.replace('Time (ms): ', '')
        line = line.replace('Prop: ', '')
        line = line.replace('Der: ', '')
        line = line.replace('Int: ', '') 
        line = line.replace('Loop time (ms): ', '')
        line = line.replace(' | ', ';')
        cleaned_data.append(line)

# write to file
with open(path, "w") as f:
    f.write("\n".join(cleaned_data))

print(f"Transformed! File '{path}' was rewritten with transformed data consisting of ({len(cleaned_data)} lines).")
