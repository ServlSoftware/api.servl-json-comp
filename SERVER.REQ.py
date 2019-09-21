import json

#JSON input string
#{"workplace":"SERVL", "ID":1234, "Time": 123, "Accepted":"False"}

workplaces = []
workplaces.append(hash("SERVL"))  

def req():
  jIn = input()
  jOut = json.loads(jIn)

  return jOut

print("Request (As JSON): ")
jOut = req()

jWork = jOut['workplace']
jId = jOut['ID']
jTime = jOut['Time']
jAccpt = jOut['Accepted']

if hash(jWork) in workplaces:
  print(jWork, jId)

  if jAccpt == "False":
    print("Accept Login (Y/N)")
    x = input()

    if x == 'Y' or x == 'y':
      jOut['Accepted'] = "True"
    else:
      jOut['Accepted'] = "False"

    print(json.dumps(jOut))

  else:
    print("Login Already Accepted")

else:
  print("Workplace not found")
