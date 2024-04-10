# Development Environment (Client)

### Prerequisite

1. Ensure you have brought up the 3 nlp-ner-trainer containers
    ```
    govind@thinkpad:~/projects/ml-gallery/nlp-ner-trainer$ docker compose -f ./compose-dev.yaml up
    ```
2. Ensure that the AI model was trained and .pkl file was generated. Click [here](../app/README.md) to follow instructions.
3. Ensure the server is up and running. Click [here](../server/README.md) to follow instructions.

## Step 1. Open `./nlp-ner-trainer/client` folder in VS Code

## Step 2. Attach it to the running client container

1. Click on `Attach to Running Container...`
2. Select `nlp-ner-trainer-client` container from the list.

## Step 3. Open container's `/workspace` folder in VS Code

## Step 4. For the 1st container run, execute `npm install`

```
root@27b5414f11b7:/workspace# npm install
```

## Step 5. Test client to server connectivity

```
root@27b5414f11b7:/workspace# curl http://server:5000/ping
{"status":200,"message":"Successful ping test"}
```

## Step 6. Start the client

```
root@27b5414f11b7:/workspace# npm start
```

Upon start following log will appear

```
Compiled successfully!

You can now view workspace in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://172.19.0.3:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
```

## Step 7. Test the application

Open http://localhost:3000 in your browser.
