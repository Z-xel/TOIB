# Лабораторная работа №4
## Курдюков Александр Анатольевич ББМО-01-23
### Создание ключевой пары GPG

`gpg --full-generate-key`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/d07defcf-e396-4640-89b5-bd8ff078c57d)
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/568be73a-79c6-4513-841b-66f9f1980a43)
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/9d59e659-e229-451d-89f8-14df61acf663)

### Просмотр созданных ключей, подписей, секретных ключей, отпечатков

`gpg --list-keys kurdyuko.a.a@edu.mirea.ru`

`gpg --list-signatures kurdyuko.a.a@edu.mirea.ru`

`gpg --list-secret-keys kurdyuko.a.a@edu.mirea.ru`

`gpg --fingerprint kurdyuko.a.a@edu.mirea.ru`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/19b98ad8-1597-433e-852b-f3ed74c0d4c6)

### Создание отзывающего сертификата
Вывод сертификата в консоль | Запись сертификата в файл
--- | ---
`gpg --gen-revoke kurdyuko.a.a@edu.mirea.ru` | `gpg --output revoke.asc --gen-revoke kurdyuko.a.a@edu.mirea.ru`
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/84078d48-faa7-4867-b22a-6565b22de577) | ![изображение](https://github.com/Z-xel/TOIB/assets/70752907/d5e3e4fb-849d-4c6a-ba68-1daa09c9f2d9)

### Экспорт публичного ключа в бинарном и текстовом виде
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/344be776-7c0f-4a2d-97c3-2316e60baf82)
В бинарном виде | В текстовом виде
--- | ---
`gpg --output kurdyukov-pub.gpg` | `gpg --armor --output kurdyukov-pub.asc --export kurdyuko.a.a@edu.mirea.ru`
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/bf3b3b62-ad46-4fa5-b1c7-f8563324026c) | ![изображение](https://github.com/Z-xel/TOIB/assets/70752907/400fb4fe-3619-48a6-bf09-e7004ab854af)

### Создание файла для подписи
![изображение](https://github.com/Z-xel/TOIB/assets/70752907/c5d5b1ff-277a-40b5-806b-9cf6263db0fe)

### Создание цифровой подписи в бинарном виде

`gpg --local-user kurdyuko.a.a@edu.mirea.ru --sign msg.txt`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/872b3f74-bd04-4034-86ad-4f5f0f647831)

### Проверка подписи

`gpg --verify msg.txt.gpg`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/98846530-9681-480d-81ee-159c253945af)

### Создание цифровой подписи в формате ASCII

`gpg --local-user kurdyuko.a.a@edu.mirea.ru --armor --sign msg.txt`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/60c63b8e-547e-4cf0-8a43-31b0c2269d98)

### Создание цифровой подписи, вставленной в содержимое файла

`gpg --local-user kurdyuko.a.a@edu.mirea.ru --clearsign secret`

`gpg --verify secret.asc`

![изображение](https://github.com/Z-xel/TOIB/assets/70752907/beacdd2e-cba8-4d91-b80c-82cf5eb11bbb)

