#ШАГ 2: Разбор по частям введённой информации

def read_from_db():
	file_object = open("db.txt", "r", encoding="utf8")
	file_content = file_object.read()
	file_object.close()
	return file_content

def parse_tasks(raw_content):
	raw_tasks = raw_content.splitlines()
	tasks = []

	for task_info in raw_tasks:
		splitted_task = task_info.split("<>")
		raw_status = splitted_task[4]
		if raw_status == "active":
			status = "✓"
		else:
			status = "✕"
		task = status + " " + splitted_task[1] + " " + splitted_task[2] + " " + splitted_task[3]
		tasks.append(task)

	return tasks

def print_all_tasks_to_console(tasks):
	counter = 1
	print("Актуальные задачи:")
	for task_info in tasks:
		print(str(counter) + ": " + task_info)
		counter += 1


def parse_new_task(raw_data):
	splitted_params = raw_data.split("[") #пробуем выделить описание и дату

	task_description = splitted_params[0].strip() #массив всегда будет содержать один элемент, даже если нет скобки, поэтому можем смело брать первый элемент;
	#👆 strip() убирает лишние пробелы
	task_due_date = "не задана"

	if len(splitted_params) == 2: #если в списке 2 элемента
		#другой вариант "убирания" закрывающей скобочки
		#task_due_date = splitted_params[1].split("]")
		#task_due_date = task_due_date[0]
		
		task_due_date = splitted_params[1].replace("]","") #"удаляем" лишнюю закрывающую скобку, т.е. меняем символ [ на "ничего"

	print("Создаётся задача с параметрами:")
	print("- Описание задачи: " + task_description)
	print("- Дата выполнения: [" + task_due_date + "]")
	print("#----------------------------------#")

def main():
	while True:
		all_tasks = read_from_db()
		tasks_list = parse_tasks(all_tasks)
		print_all_tasks_to_console(tasks_list)

		new_task_info = input("Введите новую задачу: ")
		parse_new_task(new_task_info)

main()