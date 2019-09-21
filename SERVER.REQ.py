import json

#JSON input string
#{"workplace":"SERVL", "ID":1234, "Time": 123, "Accepted":"False"}

workplaces = []
workplaces.append(hash("SERVL"))  

def req():
  JSON_Input = input()
  JSON_PARSED_OUTPUT = json.loads(JSON_Input)

  return JSON_PARSED_OUTPUT

print("Request (As JSON): ")
JSON_PARSED_OUTPUT = req()

PARSED_QUERY_WORK = JSON_PARSED_OUTPUT['workplace']
PARSED_QUERY_ID = JSON_PARSED_OUTPUT['ID']
PARSED_QUERY_TIME = JSON_PARSED_OUTPUT['Time']
PARSED_QUERY_STATUS = JSON_PARSED_OUTPUT['Accepted']

if hash(PARSED_QUERY_WORK) in workplaces:
  print(PARSED_QUERY_WORK, PARSED_QUERY_ID)

  if PARSED_QUERY_STATUS == "False":
    print("Accept Login (Y/N)")
    _input_ = input()

    if _input_ == 'Y' or _input_ == 'y':
      JSON_PARSED_OUTPUT['Accepted'] = "True"
    else:
      JSON_PARSED_OUTPUT['Accepted'] = "False"
    
    #TEST DUMP
    print(json.dumps(JSON_PARSED_OUTPUT))

  else:
    #NO CHANGE NEEDED
    print("Login Already Accepted")

else:
  #THROW ERROR
  print("Workplace not found")
