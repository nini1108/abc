# DevOps Engineer Technical Quiz
## 1. Programming/Scripting
**Using your preferred programming or scripting language, write a function that takes a number as an argument and returns the string “aunty” if that number is divisible by 3 and returns “uncle” otherwise.**

Please check the python file with the link below. <br />
[python file](./main.py)

## 2. Unix/Linux
**Write a command to send the signal SIGTERM to the “mongo” process.**<br />
`kill PID`

**Write a command to recursively delete all files named “virus” in the /usr directory.**<br />
`find ./usr  -type f --name "*virus*" -delete`

## 3. Containers
**Write a Dockerfile that installs the program “curl”.**

Please check the Dockerfile with the link below.<br />
[Dockerfile](./Dockerfile)

## 4. Web
**How would you make an HTTP “GET” request with the HTTP “Pragma” request header set to “no- cache”?**<br />

In NodeJs use <br />
`response.setHeader("Pragma", "no-cache"); // HTTP 1.0.`<br />

As HTTP 1.1 uses 'Cache-Control' and backwards compatible with Pragma<br />
`response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); // HTTP 1.1.`