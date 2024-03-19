# Development Environment (Server)

### Prerequisite

Ensure you have brought up the 3 nlp-ner-trainer containers
```
govind@thinkpad:~/projects/ml-gallery/nlp-ner-trainer$ docker compose -f ./compose-dev.yaml up
```

## Step 1. Open `./nlp-ner-trainer/server` folder in VS Code

## Step 2. Attach it to the running server container

1. Click on `Attach to Running Container...`
2. Select `nlp-ner-trainer-server` container from the list.

## Step 3. Open container's `/workspace` folder in VS Code

## Step 4. For the 1st container run, execute `npm install`

```
root@932b31439d84:/workspace# npm install

up to date, audited 73 packages in 521ms

12 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

## Step 5. Start the server

```
root@932b31439d84:/workspace# node ./server.js 
listen
Server listening on port 5000
```

