from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].is_completed = True
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.is_completed]
        if current_tasks:
            print("Текущие задачи:")
            for i, task in enumerate(current_tasks):
                print(f"{i + 1}. {task.description} (Срок: {task.due_date})")
        else:
            print("Нет текущих задач.")

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Написать отчет", "2024-07-15")
    manager.add_task("Позвонить клиенту", "2024-07-12")
    manager.add_task("Подготовить презентацию", "2024-07-20")

    manager.list_current_tasks()

    manager.mark_completed(1)

    print("\nПосле выполнения задачи:")
    manager.list_current_tasks()