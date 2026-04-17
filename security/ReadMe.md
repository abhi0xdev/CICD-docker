---

Don't run as root inside containers

Always create a dedicated app user

Use non-privilaged ports like 8080 or 5000

Drop linux capabilities unless u explicitly need them

and scan ur containers with tools like Docker Bench for security issues

---

next we will integrate Docker into CI/CD pipeline with jenkins or Github and simulate a broken deployment caused by wrong image tag