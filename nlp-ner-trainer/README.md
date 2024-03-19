# NLP-NER Trainer Setup

## Step 1. Bring up the 3 nlp-ner-trainer containers

```
govind@thinkpad:~/projects/ml-gallery/nlp-ner-trainer$ docker compose -f ./compose-dev.yaml up

```

## Step 2. Verify the `core app` readiness

#### 1. Open `nlp-ner-trainer` container in terminal from docker desktop.
1. Open `Docker Desktop` application.
2. Go to `Containers` screen
3. Expand `nlp-ner-trainer` group from containers list.
4. In `nlp-ner-trainer` container row, click on `...` icon, which is `Show container actions`, to view options.
5. Select `Open in terminal`.

#### 2. Ensure that the model is trained and .pkl file was created

```
# ls /app/model
en_core_web_fin_sm  nlp-ner-stck-recmndtns.pkl
```

> If .pkl file is not present then follow steps in [A. NLP-NER Trainer Development Environment Setup]

## Step 3. Start the `server`

#### 1. Open `server` container in terminal from docker desktop.
1. Open `Docker Desktop` application.
2. Go to `Containers` screen
3. Expand `nlp-ner-trainer` group from containers list.
4. In `server` container row, click on `...` icon, which is `Show container actions`, to view options.
5. Select `Open in terminal`.

#### 2. Ensure the server was built earlier

```
# cd /workspace
# ls
Dockerfile  model  nlp-processor.py  node_modules  package-lock.json  package.json  requirements.txt  server.js
# ls node_modules | wc -l
71
```

#### 3. Run server

```
# node ./server.js
listen
Server listening on port 5000
```

## Step 4. Start the `client`

#### 1. Open `client` container in terminal from docker desktop.
1. Open `Docker Desktop` application.
2. Go to `Containers` screen
3. Expand `nlp-ner-trainer` group from containers list.
4. In `client` container row, click on `...` icon, which is `Show container actions`, to view options.
5. Select `Open in terminal`.

#### 2. Ensure the client was built earlier

```
# cd /workspace
# ls
Dockerfile  README.md  node_modules  package-lock.json  package.json  public  src
# ls node_modules | wc -l
869
```

#### 3. Run client

```
# npm start
.
.
Compiled successfully!

You can now view workspace in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://172.18.0.3:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
```
