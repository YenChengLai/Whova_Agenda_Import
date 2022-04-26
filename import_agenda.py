from xlrd.timemachine import xrange

from db_table import db_table
import xlrd

file_name = "agenda.xls"
agenda = xlrd.open_workbook(file_name).sheet_by_name("Agenda")
schema = [x.replace("*", "").replace("\n", "") for x in agenda.row_values(14)]

users = db_table("agenda", {
    "id": "integer PRIMARY KEY",
    "date": "string NOT NULL",
    "time_start": "string NOT NULL",
    "time_end": "string NOT NULL",
    "session_title": "string NOT NULL",
    "location": "string",
    "description": "string"
})

id = 1
for rx in xrange(15, agenda.nrows):
    content = [c for c in agenda.row_values(rx)]

    users.insert({
        "id": id,
        "date": content[0],
        "time_start": content[1],
        "time_end": content[2],
        "session_title": content[3],
        "location": content[4],
        "description": content[5]
    })

    id += 1

users.close()
