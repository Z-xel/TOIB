Практическая работа №3, keycloak


На ВМ1 был развернут сервис keycloak с помощью docker контейнера

![277189257-11215389-71d3-4f5d-848a-689e174a50da](https://github.com/Z-xel/TOIB/assets/70752907/fe3080f5-9306-4efb-a3d0-997d5eb49880)

Создал новый реалм

![277189286-e2557af1-7c9d-44a2-ab38-da421a8f0f0b](https://github.com/Z-xel/TOIB/assets/70752907/07c2c6ca-cba0-4fcf-9b27-f5c696b2d73c)

В реалме создал тестовых пользователей

![277189309-27921194-e956-4067-92c8-a44b8d2ce288](https://github.com/Z-xel/TOIB/assets/70752907/0a116350-83e2-4a9d-aa5e-0b64616496dc)


![277189313-f03c0783-fc90-40dd-856a-ff2b809931dc](https://github.com/Z-xel/TOIB/assets/70752907/bd7771ae-3610-458f-91cd-2fc415f2bef2)


![277189325-d9b4aebf-5a8c-478a-b929-80869a0df07c](https://github.com/Z-xel/TOIB/assets/70752907/83a18288-a131-43e1-9135-73b6a399ea42)

В качестве приложения на ВМ 2 для реализации аутентификации при помощи keycloak выбрал Jupyter Hub, создаю клиента для него

![277189359-285492a8-81b5-4836-b658-9d70aa716691](https://github.com/Z-xel/TOIB/assets/70752907/e1953a1c-7f38-4219-9878-039af8a48b0d)

Для Jupyter Hub был написан данный конфиг для успешной привязки сервисов друг к другу

![277189587-b9926590-a128-4e70-85ab-714da92a11c5](https://github.com/Z-xel/TOIB/assets/70752907/81aafd7d-dce0-4b8d-b846-4463fb098ffc)

Сервис успешно запустился со сторонним сервисов аутентификации

![277189645-ce4014df-800f-49ac-b655-6b33373ad1b0](https://github.com/Z-xel/TOIB/assets/70752907/8bfaf5b2-02a6-4a72-bf26-acc35fe3708e)


![277189656-9462c332-4062-4d05-9760-aedbb22a280c](https://github.com/Z-xel/TOIB/assets/70752907/db47a8fc-96f7-4f55-a359-5f4aec662921)

Аутентификация успешно прошла с помощью заданной связки логин-пароль в keycloak

![277189662-dd75863c-87d2-48d7-8891-199c15fe4676-1](https://github.com/Z-xel/TOIB/assets/70752907/23605026-8abd-4f66-88c3-99fd86183ad9)

Далее включаем OTP в настройках приложения в keycloak

![277189708-fed92086-9bba-4d7f-b3ae-6096fca03427](https://github.com/Z-xel/TOIB/assets/70752907/7dd0ff7f-1bfe-40da-9dff-ef6d1d5dd833)

При перезаходе в приложение нам предложило добавить запись в OTP клиент

![277189747-ddbfd2b5-3551-4999-8338-87e95d2f91af](https://github.com/Z-xel/TOIB/assets/70752907/6939b953-5c09-41d5-838a-467d82d5c615)
