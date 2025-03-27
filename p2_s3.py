#ШАГ 3: Подготовка информации о задаче к сохранению

import uuid #простое подключение модулей
from datetime import datetime #подключение конкретного атрибута из модуля

STATUS_ACTIVE = "active" #глобальная переменная|константа для статуса
SEPARATOR = "<>" #глобальная переменная для разделителя

def read_from_db():
	file_object = open("db.txt", "r", encoding="utf8")
	file_content = file_object.read()
	file_object.close()
	return file_content

def parse_tasks(raw_content):
	raw_tasks = raw_content.splitlines()
	tasks = []

	for task_info in raw_tasks:
		splitted_task = task_info.split(SEPARATOR) #используем глобальную переменную
		raw_status = splitted_task[4]
		if raw_status == STATUS_ACTIVE: #используем глобальную переменную
			status = "✓"
		else:
			status = "✕"
		task = status + " " + splitted_task[1] + " " + splitted_task[2] + " " + splitted_task[3]
		#task = " ".join([status, splitted_task[1], splitted_task[2], splitted_task[3]])
		tasks.append(task)

	return tasks

def print_all_tasks_to_console(tasks):
	counter = 1
	print("Актуальные задачи:")
	for task_info in tasks:
		print(str(counter) + ": " + task_info)
		counter += 1

def prepare_task_to_save(task_info): #готовим строку для сохранения
	task_id = uuid.uuid4() #генерируем уникальный идентификатор; пригодится нам сильно позже
	task_date_created = datetime.now() #получаем текущую дату/время
	#task_date_created = datetime.datetime.now() #если подключали весь модуль import datetime

	to_join = [str(task_id), task_info[0], "["+task_info[1]+"]", str(task_date_created), STATUS_ACTIVE]
	task_to_save = SEPARATOR.join(to_join) #объединяем разные части задачи через сепаратор
	return task_to_save

def parse_new_task(raw_data):
	splitted_params = raw_data.split("[") 
	task_description = splitted_params[0].strip()
	task_due_date = ""

	if len(splitted_params) == 2:
		task_due_date = splitted_params[1].replace("]","")

	#final_list = [task_description, task_due_date]
	#return final_list
	return [task_description, task_due_date]


def main():
	while True:
		all_tasks = read_from_db()
		tasks_list = parse_tasks(all_tasks)
		print_all_tasks_to_console(tasks_list)

		new_task_info = input("Введите новую задачу: ")
		task_data = parse_new_task(new_task_info) #разбираем ввод пользователя и получаем список из 2х элементов
		task_to_save = prepare_task_to_save(task_data) #формируем итоговую строку для записи в БД (с доп. параметрами и разделителем)
		print(task_to_save) #промежуточный вывод задачи для сохранения

main()