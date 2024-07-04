-- Отримати всі завдання певного користувача (наприклад, користувача #1)
SELECT * from tasks WHERE user_id=1

-- Вибрати завдання за певним статусом (наприклад, 'new')
SELECT * FROM tasks WHERE status_id=(SELECT id FROM status WHERE name='new')

-- Оновити статус конкретного завдання (наприклад, завдання #3 зробити 'in progress')
UPDATE tasks SET status_id=(SELECT id FROM status WHERE name='in progress') WHERE id=3

-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)

-- Додати нове завдання для конкретного користувача (наприклад користувач #2 і завдання в статусі 'new')
INSERT INTO tasks(user_id, title, description, status_id) VALUES(2, 'new task', 'new task description', 1);

-- Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name='completed')

-- Видалити конкретне завдання (наприклад завдання #1)
DELETE FROM tasks WHERE id=1

-- Знайти користувачів з певною електронною поштою (наприклад, з домена ʼ@example.org')
SELECT * FROM users WHERE email LIKE '%@example.org'

-- Оновити ім'я користувача (наприклад, користувача #1 на 'John Smith')
UPDATE users SET fullname='John Smith' WHERE id=1

-- Отримати кількість завдань для кожного статусу
SELECT COUNT(*), s.name FROM tasks t LEFT JOIN status s ON t.status_id = s.id GROUP BY s.id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти (наприклад, '@example.com') 
SELECT * FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%@example.com'

-- Отримати список завдань, що не мають опису
SELECT * FROM tasks  WHERE (description = '' or description is null)

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT u.fullname, t.title FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE status_id=(SELECT id FROM status WHERE name='in progress')

-- Отримати користувачів та кількість їхніх завдань.
SELECT COUNT(*), u.fullname FROM tasks t LEFT JOIN users u ON t.user_id = u.id GROUP BY u.id
