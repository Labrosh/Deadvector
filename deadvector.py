import yaml, random, pathlib

event = yaml.safe_load(pathlib.Path("events/ELEC-000.yml").read_text())

print(event["ai_opening"])
roll = random.randint(1, 20)
outcome = "success" if roll >= 11 else "fail"
print(event["narration"][outcome])
