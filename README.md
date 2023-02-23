# Cashier System
Repositório para armazenar os códigos referentes ao Trabalho Final de Disciplina de Programação Orientada a Objetos

### Requirements and Dependencies

Open your terminal and go to solution/ dir

`cd solution`

Install all missing dependencies at once:

`pip install -r requirements.txt`

Or type in your terminal:

`make install_requirements`

If it is the first time you run de project:

`make start_database`

Then:

`make runall`

### The two api's can be access at:
- localhost:4200/docs
- localhost:4300/docs

## To see log output, type in another terminal:

- `make log`

## If you want a new and fresh database:

- `make restart_database`

---

### Recommended git workflow

#### Sync with origin
- `git checkout main`
- `git fetch origin -p`
- `git rebase origin/main`

#### To start a new work/task
- After executed the sync
- `git checkout -b main_{work description}`
	- exemple: `git checkout -b main_clients_api`

### Define postgres default password

- best tutorial [here] (https://chartio.com/resources/tutorials/how-to-set-the-default-user-password-in-postgresql/)
