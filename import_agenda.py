from db_table import db_table
import xlrd

file_name = "agenda.xls"
agenda = xlrd.open_workbook(file_name).sheet_by_name("Agenda")
schema = [x.replace("*", "").replace("\n", "") for x in agenda.row_values(14)]

agenda_table = db_table("agenda")
speaker_table = db_table("speaker")
subsession_table = db_table("subsession")

id = 1
parent_id = 1
for rx in range(15, agenda.nrows):
    content = [c for c in agenda.row_values(rx)]

    session = content[3]
    if session == "Session":
        parent_id = id

        # insert into agenda table
        agenda_table.insert({
            "id": id,
            "date": content[0],
            "time_start": content[1],
            "time_end": content[2],
            "title": content[4],
            "location": content[5],
            "description": content[6],
            "speaker": content[7]
        })
    else:
        # insert into subsession table, using parent_id to refer to data in agenda table
        subsession_table.insert({
            "id": id,
            "parent_id": parent_id,
            "date": content[0],
            "time_start": content[1],
            "time_end": content[2],
            "title": content[4],
            "location": content[5],
            "description": content[6],
            "speaker": content[7]
        })

    # insert into speaker table, using agenda_id to refer to data in agenda table
    if ";" in content[7]:
        speakers = content[7].split(';')
        for speaker in speakers:
            speaker_table.insert({
                "agenda_id": id,
                "speaker": speaker.strip()
            })
    elif len(content[7]) > 0:
        speaker_table.insert({
            "agenda_id": id,
            "speaker": content[7]
        })

    id += 1

agenda_table.close()
speaker_table.close()
