# Практическое задание №4. Сбор логов

Выполнил Курдюков Александр, группа ББМО-01-23

## `rsyslog`

### Установка `rsyslog` на сервер

![image](https://github.com/Z-xel/TOIB/assets/70752907/f6fce66e-2938-456d-aa71-b1f5a9b329dc)


![image](https://github.com/Z-xel/TOIB/assets/70752907/10a9e2e9-fe7b-4874-95eb-ae60260123a4)

### Настройка модулей `rsyslog`

![image](https://github.com/Z-xel/TOIB/assets/70752907/04bca09c-534c-4fcc-8219-e77f4e26ef0f)

### Добавление правил обработки логов

![image](https://github.com/Z-xel/TOIB/assets/70752907/8c130466-4553-4446-bb74-11264c86d162)

### Применение конфигурации `rsyslog`

![image](https://github.com/Z-xel/TOIB/assets/70752907/ec97b9a4-97a7-4562-b85c-55616705550f)

### Установка `rsyslog` на клиент

![image](https://github.com/Z-xel/TOIB/assets/70752907/4628631d-5270-4d3c-bbed-7eb0ef5f2ca0)


![image](https://github.com/Z-xel/TOIB/assets/70752907/9b476a3e-8b37-4312-b5fc-be61973e17b9)

### Добавление правила пересылки логов на сервер

![image](https://github.com/Z-xel/TOIB/assets/70752907/2547a14e-4ea7-4591-98a4-8de64f407751)

### Применение конфигурации `rsyslog`

![image](https://github.com/Z-xel/TOIB/assets/70752907/818df6cf-8e4f-427b-9dbf-3a4971159bf1)

### Просмотр полученных логов на сервере

![image](https://github.com/Z-xel/TOIB/assets/70752907/fc937dd3-d662-45c2-a50b-e1d2e417ddbd)

## Grafana Loki

### Загрузка compose-файла от разработчика

![image](https://github.com/Z-xel/TOIB/assets/70752907/fadf000c-648d-476a-bfc4-61f68ce0cfb0)

### Редактирование compose-файла с целью отключения компонента `promtail` на сервере

![image](https://github.com/Z-xel/TOIB/assets/70752907/9a197b5d-e5bb-474d-9d1c-94e6db1ce9f3)

### Запуск Loki

![image](https://github.com/Z-xel/TOIB/assets/70752907/2231886c-8cda-4ac5-9528-9095d4de9e82)

### Редактирование конфигурации `promtail` на клиенте

![image](https://github.com/Z-xel/TOIB/assets/70752907/07666e73-1ffd-4f70-bc16-d24a8913b00e)

### comopose-файл для `promtail`

![image](https://github.com/Z-xel/TOIB/assets/70752907/bacdebfa-6b87-466a-8440-3cb86ac38025)

### Запуск `promtail` на клиенте

![image](https://github.com/Z-xel/TOIB/assets/70752907/10b5a596-c958-4e7c-8880-dae9d4511b3f)

### Просмотр логов клиента в Grafana

![image](https://github.com/Z-xel/TOIB/assets/70752907/270f023f-adf0-4e8f-8e5f-5e3dae12278d)

## Signoz

### Запуск Signoz

Установка согласно https://signoz.io/docs/install/docker/#install-signoz-using-docker-compose

![](screenshots/18-start-signoz.png)

### Рабочая панель Signoz

![](screenshots/19-open-signoz.png)

### Редактирование конфигурации клиентского приложения для отправки данных в Signoz

Используемое приложение - https://github.com/SigNoz/sample-nodejs-app/

![](screenshots/20-update-compose-client.png)

### Запуск клиентского приложения

![](screenshots/21-start-client.png)

### Информация о приложении в Signoz

![](screenshots/22-dashboards.png)

![](screenshots/23-traces.png)
