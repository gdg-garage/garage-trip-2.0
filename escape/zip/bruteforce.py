import subprocess

for passwd in range(1111, 10000):
    try:
        r = subprocess.run(["unzip", "-o", "-P", str(passwd), "use-the-force.zip", "-d", "out"], check=True, capture_output=True)
        print(passwd)
        break
    except subprocess.CalledProcessError:
        pass

