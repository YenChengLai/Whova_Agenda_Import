from db_table import db_table

cols = input("Please enter column:").split(",")
vals = input("Please enter value:").split(",")

search_params = {}

for i in range(len(vals)):
    search_params[cols[i]] = vals[i]

speaker_table = db_table("speaker")
agenda_table = db_table("agenda")

results = []

if "speaker" in cols:
    speakers = speaker_table.select(None, search_params)
    for i in range(len(speakers)):
        agenda = agenda_table.select(None, {"id": speakers[i]["agenda_id"]})
        results.extend(agenda)
else:
    results = agenda_table.select(None, search_params)

for result in results:
    print(result)
