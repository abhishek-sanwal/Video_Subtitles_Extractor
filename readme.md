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

Pro tip: Use **Docker Debug** to visualize the containers and check the errors if any occurs. Sometime You may need to reload a particular container. Use Docker Desktop to reload that container instantly.

Sometimes Django will not be able to connect to postgres when you first spin the backend container. Postgres may take a longer time to setup so, just reload /refresh that container after db setup is completed it will work.

---

### Screenshots of working app

#### Docker View

[](/screenshots/Backend_Docker_View.png)

#### Backend Container

[](/screenshots/Backend_Container.png)

#### Celery

[](/screenshots/Backend_Celery_View.png)

#### Redis

[](/screenshots/Redis.png)

If you want to delete all models data at any moment of time you can't directly use admin panel as there will a lot of data so you can use **shell** or **dbshell** to quickly delete model.

[You can use this command on backend container or in vscode](/screenshots/Backend_Delete_all_models_data.png)
