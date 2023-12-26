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
![](https://i.imgur.com/vJkNn2L.png)
В бинарном виде | В текстовом виде
--- | ---
`gpg --output chursinov-pub.gpg` | `gpg --armor --output chursinov-pub.asc --export chursinov.g.s@edu.mirea.ru`
![](https://i.imgur.com/kY0mxbK.png) | ![](https://i.imgur.com/zhMDUfx.png)
### Создание файла для подписи
![](https://i.imgur.com/jaxSciL.png)
### Создание цифровой подписи в бинарном виде

`gpg --local-user chursinov.g.s@edu.mirea.ru --sign file.txt`

![](https://i.imgur.com/ynUtXnT.png)
### Проверка подписи

`gpg --verity file.txt.gpg`

![](https://i.imgur.com/Cwuzo6d.png)
### Создание цифровой подписи в формате ASCII

`gpg --local-user chursinov.g.s@edu.mirea.ru --armor --sign file.txt`

![](https://i.imgur.com/Bv3K6pC.png)
### Создание цифровой подписи, вставленной в содержимое файла

`gpg --local-user chursinov.g.s@edu.mirea.ru --clearsign file.txt`

`gpg --verify file.txt.asc`

![](https://i.imgur.com/oGVtN5U.png)
