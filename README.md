# T_bot_201023

#### STEP'S command line
##### Step 1
- sudo apt install telegram-desktop 
- conda deactivate
- cd $HOME
- mkdir enviroments
- cd enviroments
- python3 -m venv T_bot_201023_env
- source T_bot_201023_env/bin/activate
- $HOME/enviroments/T_bot_201023_env/bin/python3.7 -m pip install --upgrade pip
- cd $HOME
- git clone https://github.com/mirpribili/T_bot_201023.git
- cd $HOME/T_bot_201023
- git remote set-url origin git@github.com:mirpribili/T_bot_201023.git
- *conda deactivate;cd $HOME/enviroments;source T_bot_201023_env/bin/activate;cd $HOME/T_bot_201023*
- **git add .;git commit -m "add git simple project";git push origin**
- **pip freeze > requirements.txt**
- git clone https://github.com/Latand/udemy_course.git
- cd $HOME/T_bot_201023;sudo apt-get install python3.8
- python3.8 --version
- nano ~/.bashrc
- - add string
- - - alias python3=python3.8
- python3 -m venv --upgrade $HOME/enviroments/T_bot_201023_env/
- deactivate
- cd $HOME
- *rmvirtualenv T_bot_201023_env*
- *python3.8 -m venv T_bot_201028_env*
- *sudo apt-get install python-virtualenv*
- sudo apt-get install python3.8-dev python3.8-venv
- *virtualenv --python=/usr/bin/python3.8 venv*
- python3.8 --version
- **python3.8 -m venv T_bot_201028_env**
- **conda deactivate;cd $HOME/enviroments;source T_bot_201028_env/bin/activate;cd $HOME/T_bot_201023**
- python --version
- **git branch**
- **git branch 201028_template**
- **git checkout 201028_template**
- **git checkout master**
- **git branch -d 201028_template**
- **git checkout -b 201028_template**
- pip uninstall loader
- pip list

<img src="img\telegram_kurs.png"> 

## 11. Практика
### написание запросов
- https://api.telegram.org/bot%token%/getUpdates
- https://api.telegram.org/bott%token%/sendMessage?chat_id=514021214&text=Hello World

### Задание
- Необходимо отправить нашим ботом в группу с chat_id = -1001359487461 фотографию, которую вы нашли в интернете по ссылке: https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png
- Token бота = 932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs
- При этом вы хотите сделать подпись к фотке "Ух, ты только посмотри на него!"
- Сформируйте необходимый запрос и пришлите сюда то, что содержится в поле file_unique_id (уникальный идентификатор этой фотографии).
- ******* Подсказка ******* 
- - Используйте метод sendPhoto

> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/sendPhoto?chat_id=-1001359487461&photo=https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png&caption=Ух, ты только посмотри на него!
>> AQADJjDcJ10AAwiXAAI
>>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/sendphoto?chat_id=-1001359487461&photo=https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png&caption=Ух, ты только посмотри на него!


#### Уровень 2.
- У вас есть чат-группа с chat_id = -1001359487461, где находится ваш бот-админ. Вы хотите этим ботом установить новое название чата "Моя мини-супер группа" (или придумайте своё). Сделайте это с помощью запроса через API.
- Используйте тот же токен бота.
- ПРИШЛИТЕ СЮДА СФОРМИРОВАННЫЙ ЗАПРОС
- ******* Подсказка ******* 
- - "Название" по английски - Title
- - "Чат" - Chat

> setChatTitle
>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/setChatTitle?chat_id=-1001359487461&title=Моя мини-супер группа
>>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/setChatTitle?chat_id=-1001359487461&title=Моя мини-супер группа

#### Уровень 3.

- Найдите эту группу (она приватная, поэтому есть только инвайт ссылка) с помощью нужного метода по chat_id = -1001359487461 и зайдите в нее, и насладитесь результатом своей работы! (после этого можете сразу выходить)
- Используйте тот же токен бота.
- ПРИШЛИТЕ СЮДА СФОРМИРОВАННЫЙ ЗАПРОС

> getChat
>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/getChat?chat_id=-1001359487461
>>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/exportChatInviteLink?chat_id=-1001359487461

#### Уровень 3.

Определите username вышеуказанного бота с помощью любого метода.

ПРИШЛИТЕ СЮДА СФОРМИРОВАННЫЙ ЗАПРОС И USERNAME Бота
> sendPhoto
> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/sendPhoto?chat_id=-1001359487461&photo=https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png&caption=Ух, ты только посмотри на него!
>> Sberleadbot
>>> https://api.telegram.org/bot932722516:AAG2GqrwMxB2xfuEg7hg4Z8p9cOfBKceffs/getMe

## Раздел 3:IDE Pycharm

- theme - night owl
- ctrl + alt + l = optimize spase like pep8
- ctrl + alt + o = optimize loaders
- ctrl + d = dobled string
- crtl + x = cut string
- alt + enter = answer on error IDE
- ctrl + left mouse = go to item in another file
- ctrl + / = commented strings
- ctrl + "-" or "=" = (-:

<img src="img\причины.png"> 



