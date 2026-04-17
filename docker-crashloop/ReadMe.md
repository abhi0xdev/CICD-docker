docker start --> then crash --> bcoz of restart policy --> it stuck in loop

---
A CrashLoop happens when a container starts, fails and restarts endlessly

use docker logs first

docker inspect

Ypou cant always exec

The fix depends on the root cause

---
next we will move back to docker compose