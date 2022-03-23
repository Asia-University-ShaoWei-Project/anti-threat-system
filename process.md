## environment variables

- Server
  - DB_FILE_NAME
- Ras Pi
  - USER_ID
  - USER_PASSWORD
  - DOMAIN

## offers

- Server
  - select infos
  - insert infos
  - login users
- App(cordova)
  - GET
    - infos(/info)
- Rasp
  - POST(/login)
    - request server API(login)
    - return token

## Rasp Pi class

- USER
  - init
    - setup user-ID and user-password
    - Connect the server to login then take a token for certification
      - POST(/login)
        - request server API(login)
        - return token
      - save token(py)
      - setup headers auth field(py)
  - Offer the 'get token' method
- API
  - init
    - setup API url and headers
  - Record data
    - POST(/record)
      - create date and time
      - send data for server(date and time and bearer)
