path = "pid-tests/transformed-data/pid-test-40.txt"

cleaned_data = []

with open(path, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("PHYSICAL MOVEMENT"):
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
        line = line.replace('Long target: ', '')
        line = line.replace('Long angle: ', '')
        line = line.replace('Long error: ', '')
        line = line.replace('Long output: ', '')
        line = line.replace('Long prop: ', '')
        line = line.replace('Long der: ', '')
        line = line.replace('Long int: ', '') 
        line = line.replace('Loop time (ms): ', '')
        line = line.replace('left bottom front muscle open(ms): ', '')
        line = line.replace('right bottom front muscle open(ms): ', '')
        line = line.replace('left bottom back muscle open(ms): ', '')
        line = line.replace('right bottom back muscle open(ms): ', '')
        line = line.replace('right bottom back muscle open(ms): ', '')
        line = line.replace('Upper leg lateral target: ', '')
        line = line.replace('Upper leg lateral angle: ', '')
        line = line.replace('Upper leg lateral error: ', '')
        line = line.replace('Upper leg lateral output: ', '')
        line = line.replace('Upper leg lateral prop: ', '')
        line = line.replace('Upper leg lateral der: ', '')
        line = line.replace('Upper leg lateral int: ', '')
        line = line.replace(' | ', ';')
        line = line.replace('| ', ';')
        cleaned_data.append(line)

# write to file
with open(path, "w") as f:
    f.write("\n".join(cleaned_data))

print(f"Transformed! File '{path}' was rewritten with transformed data consisting of ({len(cleaned_data)} lines).")
