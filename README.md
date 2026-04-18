# 🚀 Docker End-to-End Learning (Flask + Postgres + CI/CD + Production Setup)

This repository documents my hands-on learning journey with Docker, covering everything from basic containerization to production-ready deployments with CI/CD.

---

# 🧱 1. Simple Flask App (Docker Basics)

### ✅ Key Learnings

* Always copy `requirements.txt` first → **Docker layer caching optimization**
* Use `.dockerignore` → avoid unnecessary files in image
* Use `EXPOSE` → for clarity and orchestration tools
* Always run with:

  ```bash
  docker run -p 5000:5000
  ```
* Never rely on `latest` tag in production

---

# 🐘 2. Flask + Postgres (Multi-Container Problem)

### ❌ Issue

* Flask couldn't connect to Postgres using `localhost`

### 🧠 Why?

* Each container has its own **network namespace**
* `localhost` = same container, not others

### ✅ Fix

* Create Docker network
* Use **container name as hostname**

  ```python
  host='flask-db'
  ```

---

# ⚙️ 3. Docker Compose (Simplification)

### 💡 Why Compose?

* Replaces multiple `docker run` commands
* Handles:

  * Networking automatically
  * Service discovery
  * Multi-container orchestration

### ⚠️ Common Mistakes

* YAML indentation errors
* Wrong service names
* Missing volumes

---

# 💾 4. Docker Volumes (Persistence)

### 🧠 Key Concept

* Containers are **ephemeral**
* Volumes provide **persistent storage**

### ✅ Best Practice

```yaml
volumes:
  dbdata:
```

Used as:

```yaml
- dbdata:/var/lib/postgresql/data
```

### ⚠️ Notes

* Named volumes → safe and manageable ✅
* Bind mounts → powerful but risky ❌

---

# 🔁 5. CrashLoop Debugging

### 💥 What is CrashLoop?

Container:

```
start → crash → restart → repeat
```

### 🔍 Debugging Steps

1. Check logs:

   ```bash
   docker logs <container>
   ```
2. Inspect container:

   ```bash
   docker inspect <container>
   ```
3. Try exec (if possible):

   ```bash
   docker exec -it <container> sh
   ```

### 🧠 Insight

* You **can’t always exec into crashing containers**
* Fix depends on root cause (code, config, env, ports)

---

# ⚙️ 6. Docker Compose Debugging

### 🔧 Tools

* `docker-compose logs`
* `docker-compose exec`

### ⚠️ Common Issues

* Service dependency failures
* Wrong environment variables
* Port conflicts

---

# 🧊 7. Image Optimization (Multi-Stage Builds)

### ❌ Problem

* Large images (3GB+) = slow + insecure

### ✅ Solution

* Multi-stage builds
* Use slim base images
* Copy only required files

### 🎯 Benefits

* Faster CI/CD
* Lower bandwidth cost
* Smaller attack surface

---

# 🔐 8. Docker Security Best Practices

### 🔒 Rules

* ❌ Don’t run as root
* ✅ Create non-root user
* ✅ Use ports like 5000 / 8080
* ✅ Drop unnecessary Linux capabilities
* ✅ Scan images (Docker Bench)

---

# 🔄 9. CI/CD with GitHub Actions

### 🚀 What I Built

* Automated pipeline:

  * Build Docker image
  * Tag image correctly
  * Push to Docker Hub

### ❌ Common Mistake

```bash
docker push flask-app:latest ❌
```

### ✅ Fix

```bash
docker push username/flask-app:latest
```

### 🔐 Used Secrets

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

---

# 🏗️ 10. Production-Style Setup

### 🧱 Architecture

```
User → Nginx → Flask App → Postgres
                      ↓
                  cAdvisor
```

### 🔧 Components

* Flask → App layer
* Postgres → Database
* Nginx → Load balancer
* cAdvisor → Monitoring

---

# 📈 11. Scaling & Load Handling

### 🔥 Simulation

* Generated high traffic
* Observed bottlenecks

### ✅ Fix

* Scaled app layer
* Used monitoring to validate improvement

---

# 🧠 Key Concepts Summary

| Concept      | Key Takeaway                  |
| ------------ | ----------------------------- |
| Containers   | Ephemeral                     |
| Volumes      | Persistence                   |
| Networking   | Use service names             |
| Compose      | Multi-container orchestration |
| CI/CD        | Automate build & deploy       |
| Optimization | Smaller = faster + secure     |
| Debugging    | logs → inspect → exec         |

---

# 🎯 Interview Quick Answers

### 🔹 Why not use localhost in Docker?

Each container has its own network → use service name.

### 🔹 Why volumes?

To persist data beyond container lifecycle.

### 🔹 Why multi-stage builds?

Reduce image size and improve security.

### 🔹 How to debug container crash?

* `docker logs`
* `docker inspect`
* check env/config

### 🔹 Why avoid latest tag?

Unpredictable deployments.

---

# 👨‍💻 Author

**Abhinandan Gayaki**
DevOps Engineer | CI/CD | Kubernetes | Cloud

GitHub: https://github.com/abhi0xdev/CICD-docker
