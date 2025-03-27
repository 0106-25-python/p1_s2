#ШАГ 4: Сохранение информации о новой задаче в базу

import uuid
from datetime import datetime as dt #псевдоним

STATUS_ACTIVE = "active" 
SEPARATOR = "<>" 
DB_FILE_PATH = "db.txt" #глобальная переменная для пути к файлу

def read_from_db():
	file_object = open(DB_FILE_PATH, "r", encoding="utf8")
	file_content = file_object.read()
	file_object.close()
	return file_content

def save_task_to_db(task_info): #записываем информацию в файл
	file_object = open(DB_FILE_PATH, "a", encoding="utf8") #открываем файл с параметром append, т.е. добавление информации в файл
	file_object.write("\n") #сначала записываем перенос на новую строку, иначе будет добавлять к последнему символу в файле
	file_object.write(task_info) #записываем информацию о задаче
	file_object.close()

def parse_tasks(raw_content):
	raw_tasks = raw_content.splitlines()
	tasks = []

	for task_info in raw_tasks:
		splitted_task = task_info.split(SEPARATOR) 
		raw_status = splitted_task[4]
		if raw_status == STATUS_ACTIVE: 
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

def prepare_task_to_save(task_info): 
	task_id = uuid.uuid4() 
	task_date_created = dt.now() 
	task_to_save = SEPARATOR.join([str(task_id), task_info[0], "["+task_info[1]+"]", str(task_date_created), STATUS_ACTIVE]) 
	return task_to_save

def parse_new_task(raw_data):
	splitted_params = raw_data.split("[") 
	task_description = splitted_params[0].strip()
	task_due_date = ""

	if len(splitted_params) == 2:
		task_due_date = splitted_params[1].replace("]","")

	return [task_description, task_due_date]


def main():
	while True:
		all_tasks = read_from_db()
		tasks_list = parse_tasks(all_tasks)
		print_all_tasks_to_console(tasks_list)

		new_task_info = input("Введите новую задачу: ")
		task_data = parse_new_task(new_task_info)
		task_to_save = prepare_task_to_save(task_data)
		save_task_to_db(task_to_save) #сохраняем информацию о задаче

main()