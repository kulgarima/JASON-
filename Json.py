data  = [{"id":1,"name":"vikash","age":"23","salary":"6000"},{"id":2,"name":"vivek","age":"43","salary":"7000"},{"id":3,"name":"vivek","age":"33","salary":"8000"},{"id":4,"name":"Raj","age":"73","salary":"8000"},{"id":5,"name":"Ram","age":"67","salary":"9800"}]

unique_data = {v['id']:v for v in data}.values()

file = open("table.html", "w")

table_data = '<table border="1px" style="margin-top:30px"><tr><td colspan="7" style="text-align: center;" >' \
                'JSON data to Table</td></tr><tr><td>Id</td><td>Name</td><td>Age</td>' \
                '<td>Salary</td></tr>'
for val in unique_data:
	table_data += '<tr><td>{id}</td>' \
				'<td>{name}</td>' \
				'<td>{age}</td>' \
				'<td>{salary}</td></tr>'.format(id=val.get('id'), name=val.get('name'), 
										age=val.get('age'), salary=val.get('salary'))
table_data += '</table>'
table_template = '<html><body>{}</body></html>'.format(table_data)

file.write(table_template)
file.close()