import random
import time
import subprocess
import matplotlib.pyplot as plt

def generate_string(length):
    return ''.join(random.choice('abc') for _ in range(length))

def run_test(n):
    A = generate_string(n)
    B = generate_string(n)

    with open("temp.in", "w") as f:
        f.write("3\n")
        f.write("a 2\nb 4\nc 5\n")
        f.write(A + "\n")
        f.write(B + "\n")

    start = time.time()
    subprocess.run(["python3", "src/main.py"], stdin=open("temp.in"))
    end = time.time()

    return end - start

sizes = [25, 50, 75, 100, 150, 200, 300, 400, 500, 600]
times = []

for s in sizes:
    t = run_test(s)
    times.append(t)
    print(f"Size {s}: {t}")

plt.plot(sizes, times, marker='o')
plt.xlabel("String Length")
plt.ylabel("Runtime (seconds)")
plt.title("HVLCS Runtime")
plt.savefig("results/runtime.png")
plt.show()