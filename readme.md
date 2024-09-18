# Video Subtitles Extractor and Search app

---

## Features

- Seamless Subtitle Integration: Effortlessly extract subtitle streams from videos and hard-code them directly into the video as closed captions.

- Multilingual Support: Enjoy robust support for multiple languages, making your content accessible to a global audience.

- Precise Subtitle Search: Locate subtitles with pinpoint accuracy, including exact timestamps where each line is spoken.

---

## Technologies Used:

- Python3
- Django Framework
- Celery
- Redis
- Postgres
- Docker

---

### Prerequistes:

**[Docker](https://www.docker.com/)** => Will be used to spin-up and down the container.

### Steps to use this app

1. First we Need to build this app using docker

```

docker-compose up --build

```

2. Spin up container in detached mode

```

docker-compose up -d

```

3. After use you can spin down this container using this command

```

docker-compose down


```

**Pro tip**: Use **Docker Desktop Debug** to visualize the containers and check the errors if any occurs. Sometime You may need to reload a particular container. Use Docker Desktop to reload that container instantly.

> Sometimes Django will not be able to connect to postgres when you first spin the backend container. Postgres may take a longer time to setup so, just reload /refresh that container after db setup is completed it will work.

---

### Working Demo

![Working Demo](/screenshots/Demo.mp4)


___

### Screenshots of working app


#### Docker View

![Picture](/screenshots/Backend_Docker_View.png)

#### Backend Container

![Picture](/screenshots/Backend_Container.png)

#### Celery

![Picture](/screenshots/Backend_Celery_View.png)

#### Redis

![Picture](/screenshots/Redis.png)

#### Postgres

![Picture](/screenshots/Backend_Postgres_View.png)

If you want to delete all models data at any moment of time you can't directly use admin panel as there will a lot of data it may take a longer time so you can use **shell** or **dbshell** to quickly delete model. Don't directly run delete command on postgres db.

![You can use this command on backend container or in vscode](/screenshots/Backend_Delete_all_models_data.png)

---

#### Bugs:

- Chrome Video Loading Issue :

  > Sometimes, when we click on js button it will not forward/back video to that particular timestamp because video is not loaded fully yet.[Issue only for larger Videos]

- Font tag appearing in subtitles:

  > I have tried to use regular expressions to remove all html opening and closing tags from subtitles still it is messing up here and there. So, Used a workaround by using replace function. Will fix it sooner.

---

#### Upcoming Features:

- CSS Design :

  > User Interface work is still in progress.

- Subtitle Language Selection option

  > As of now, logic is to select first subtitle stream and encode it on video as closed captions. Users doesn't have an option to choose an language out of available subtitles tracks.

---
