#ШАГ 1: Обработка ввода новой задачи

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

def parse_new_task(raw_data): #функция-заглушка, которая будет разбирать введённую информацию от пользователя
	print("Создаётся задача с параметрами:")
	print(raw_data) #просто выводим в том же виде, как ввёл пользователь
	print("#----------------------------------#")

def main(): #основная функция, которая будет постоянно ожидать ввода новой задачи
	while True: #бесконечный цикл вызова функций
		#сначала отображаем список все задач из БД
		all_tasks = read_from_db()
		tasks_list = parse_tasks(all_tasks)
		print_all_tasks_to_console(tasks_list)

		#затем ожидаем ввода новой задачи и обрабатываем введённую информацию
		#print("Введите новую задачу: ")
		#new_task_info = input()	
		
		new_task_info = input("Введите новую задачу: ")	
		parse_new_task(new_task_info)

main()