# TFD-POO
Repositório para armazenar os códigos referentes ao Trabalho Final de Disciplina de Programação Orientada a Objetos

### Requirements and Dependencies

Open your terminal and go to solution/ dir

Install all missing dependencies at once:

`pip install -r requirements.txt`

Or type in your terminal:

`make install_requirements`

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
