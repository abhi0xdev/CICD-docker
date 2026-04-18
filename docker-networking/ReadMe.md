---
Flask and Postgres were running in seperate containers

Each container has its own localhost so Flask couldn't see postgres

The fix was creating docker network and using the container name flask-db instead of localhost

we'll simplify everything with Docker Compose managing multiple containers with just one file

---

Persist Volume 

Containers are ephemeral

Named volumes are the best way to persist db in Docker

Bind mounts are powerful but dangerous if u mount the wrong path

---

now we will deal with very different failure: a container that refuses to stay alive. You'll see how to debug a container stuckin CrashLoop using docker logs and docker exec