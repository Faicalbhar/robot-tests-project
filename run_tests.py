import os
import subprocess

# Exécuter les tests
test_file = "test_sample.robot"
result = subprocess.run(["robot", test_file])

if result.returncode == 0:
    print("Tous les tests sont passés ✅")
else:
    print("Certains tests ont échoué ❌")
