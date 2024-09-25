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

### Prerequisites:

- **[Docker](https://www.docker.com/)** => Will be used to spin-up and down the container.

> ffmpeg and all other required stuff required to run this webapp will be installed by docker.

### Steps to use this webapp

**First we Need to build this app using docker**

```

docker-compose up --build

```

**Spin up container**

```

docker-compose up

```

**After use you can spin down this container using this command**

```

docker-compose down


```

**Pro tip**: Use **Docker Desktop ** to visualize the containers and check the errors if any occurs. Sometime You may need to reload a particular container. Use Docker Desktop to reload that container instantly.

> Sometimes Django will not be able to connect to postgres when you first spin the backend container. Postgres may take a longer time to setup so, just reload /refresh that container after db setup is completed it will work.

---

### Working Demo

- ![Working Demo](/screenshots/Demo.mp4)
- [Online Video Player](https://drive.google.com/file/d/1oNCSB5NWWnYozE5lnfS937Wlq-XIOW9v/view?usp=sharing)

---

### Available paths

- /list-videos/
- /login/
- /logout/
- /register/
- /search-subtitles/
- /upload-video/

> Excluding admin paths. Login and register is not required to use this app. Run command **`python3 manage.py show_urls`** to check all paths.

<br>

#### Video Storage Paths

- assets/output-videos => Stores all encoded videos.
- assets/subtitles => Store all subtitle files of each video.
- assets/videos => location where input video will be stored.

---

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

---

#### Upload Video

![pic_1](/screenshots/Upload_Video_1.png)

![pic_2](/screenshots/Upload_video_2.png)

> Upload any video you want. Subtitles extraction and video encoding with closed captions task is given to celery.

---

#### List Input Video with subtitles

![pic_3](/screenshots/list_videos_1.png)

- It will list video with input file along with subtitles.[Refresh the page if subtitles is not available]

- Input filename may get change if a duplicate file with same name exists in system.It will assign some random string after that name. Check videos folder for that name.

---

#### Search Subtitles

![pic_1](/screenshots/Subtitles_search_1.png)
![pic_2](/screenshots/Subtitles_Search_2.png)
![pic_3](/screenshots/Subtitles_Search_3_1.png)
![pic_4](/screenshots/Subtitles_Search_3.png)
![pic_5](/screenshots/Subtitles_Search_4.png)

> We can use any word to search here. It will provide the timestamp of that word in all videos uploaded to website along with a button to play from that timestamp.

---

If you want to delete all models data at any moment of time you can't directly use admin panel as there will a lot of data it may take a longer time so you can use **shell** or **dbshell** to quickly delete model. Don't directly run delete command on postgres db.

![You can use this command on backend container or in vscode](/screenshots/Backend_Delete_all_models_data.png)

---

#### Bugs:

- Chrome Video Loading Issue :

  > Sometimes, when we click on js button it will not forward/back video to that particular timestamp because video is not loaded fully yet.[Issue only for larger Videos]

---

#### Upcoming Features:

- Website Design :

  > User Interface work is still in progress.

- Subtitle Language Selection option

  > As of now, logic is to select first subtitle stream and encode it on video as closed captions. Users doesn't have an option to choose an language out of available subtitles tracks.

---
