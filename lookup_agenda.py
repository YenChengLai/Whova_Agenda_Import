from db_table import db_table

# get search parameters
cols = input("Please enter column:").split(",")
vals = input("Please enter value:").split(",")

search_params = {}

# format search parameters
for i in range(len(vals)):
    search_params[cols[i]] = vals[i]

# get tables
speaker_table = db_table("speaker")
agenda_table = db_table("agenda")
subsession_table = db_table("subsession")

# the final result list
results = []

# search
if "speaker" in cols:
    speakers = speaker_table.select(None, search_params)
    # get all sessions the speaker attended
    for i in range(len(speakers)):
        agenda = agenda_table.select(None, {"id": speakers[i]["agenda_id"]})
        results.extend(agenda)
else:
    results = agenda_table.select(None, search_params)

# use Session data to look for subsessions
for i in range(len(results)):
    subsessions = subsession_table.select(None, {"parent_id": results[i]["id"]})

    # if subsessions exist, remove parent_id data and insert it right after current session
    if len(subsessions) != 0:
        for subsession in subsessions:
            del subsession["parent_id"]
            i += 1
            results.insert(i, subsession)

# print out the final results
for result in results:
    print(result)
