# Running in Docker

In root directory of project:
```
docker compose build && docker compose up
```
wait for start up.

Navigate to http://localhost:8080 or http://host-ip:8080


## Open a shell in the running container

If you want to look around the container, get the running docker containers' ID: 

```
docker ps
```

then: 

```
docker exec -it CONTAINER-ID bin/bash
```

type exit to exit

## Certbot

[Follow this simple guide](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/) for SSL certificates.

Spin up the container first, then open a shell in it and follow the guide. So make sure not to kill the container as of 
this moment because changes will be lost. It's a bit of manual work for now, but that's alright, I'll find a better solution later.
