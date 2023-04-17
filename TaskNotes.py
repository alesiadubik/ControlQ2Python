import json
import datetime

filename = 'notes.json'

def load_notes():
    try:
        with open(filename, 'r') as fn:
            notes = json.load(fn)
    except FileNotFoundError:
        notes = []
    return notes

def all_notes(number=None):
    number = input("Enter - вывода всех заметок или дата/время (dd-mm-yyyy hh:mm): " '\n')
    notes = load_notes()
    if number:
        notes = [note for note in notes if note['date'] == number]
    if not notes:
        print("Нет заметок")
    for note in notes:
            print(note['id'], note['title'], note['date'])
    return notes


def show_note(note_id = None):
    note_id = int(input("Введите номер заметки для просмотра: "))
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id))
    if note:
        print()
        print(note['title'], note['date'])
        print(note['text']) 
        return note
    else:
        return None
        print("\nЗаметка не найдена!")
    
def save_notes(notes):
    with open(filename, 'w') as fn:
        json.dump(notes, fn)

def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    note_title = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    notes.append({'id': note_id, 'title': note_title, 'text': note_text, 'date': note_date})
    save_notes(notes)

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note_title = input("Введите новое название заметки: ")
        note_text = input("Введите новый текст заметки: ")
        note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        note['title'] = note_title
        note['text'] = note_text
        note['date'] = note_date
        save_notes(notes)
    else:
        print("\nНет такой заметки!")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для удаления: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("\nЗаметка удалена!")
    else:
        print("\nЗаметка не найдена!")

print("\nПриложение для заметок.")

while True:
    print("\nСписок команд:")
    print("1 - Вывод всего списка заметок")
    print("2 - Просмотреть заметку")
    print("3 - Создать заметку")
    print("4 - Редактировать заметку")
    print("5 - Удалить заметку")
    print("0 - Выход из приложения")

    choice = input("\nВведите номер команды: ")

    if choice == '1':
        notes = all_notes()   
    elif choice == '2':
        note = show_note()
    elif choice == '3':
        create_note()
    elif choice == '4':
        edit_note()
    elif choice == '5':
        delete_note()
    elif choice == '0':
        print("\nВыход из приложения")
        break