from db_table import db_table

col = input("Please enter column:").split(",")
val = input("Please enter value:").split(",")

searchParams = {}

for i in range(len(val)):
    searchParams[col[i]] = val[i]

speaker_table = db_table("speaker")
agenda_table = db_table("agenda")

result = []

if "speaker" in col:
    speakers = speaker_table.select(None, searchParams)
    print(speakers)
    for i in range(len(speakers)):
        agenda = agenda_table.select(None, {"id": speakers[i]["agenda_id"]})
        print(agenda)
