import xmltodict

student = {
  "data" : {
    "name" : "Madhurendra",
    "marks" : {
      "math" : 91,
      "english" : 71
    },
    "id" : "s387hs3"
  }
}

print(xmltodict.unparse(student, pretty=True))