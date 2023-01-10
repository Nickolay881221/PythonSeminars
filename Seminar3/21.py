# Напишите программу для печати всех уникальных значенией в словаре.
# inpDict = {
#"I": "S001",
#"II": "S002",
#"III": "S001",
#"IV": "S005",
#"V": " S005 ",
#"VI": " S009 ",
#"VII": " S007 ",
#}


inpDict = {"I": "S001", "II": "S002", "III": "S001", "IV": "S005", "V": "S005", "VI": "S009", "VII": "S007"}
print(inpDict.values())
res = set(inpDict.values())
print(res)
print(sorted(res))
