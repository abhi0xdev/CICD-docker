---

Why Image Size Matters?

bcoz smaller images = faster CI/CD Pipelines
less netwrok transfer = cheaper bandwidth
smaller attack surface = better security

---

A bloated Dockerfile with fat base image + unneccesary tools = 3.41 GB monster

Multi-stage builds let u separate build dependecies from runtime

Slim base images + .dockerignore + copying only what you need = prod ready images

---
next we will see conatiner security and permissions