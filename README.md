# home-db
app running on my laptop for storing data about myself to analyze and run ad hoc automations. 

#### Features
- Store book highlights from kindle text file `My Clippings.txt` in sqlite
- Sync stored highlights with Anki for sentence mining

### Installation for OSX
1. Install [homebrew](https://brew.sh/)
2. Globally install pipenv with homebrew `brew install pipenv`
3. Have [anki](https://apps.ankiweb.net/) installed with [anki-connect](https://github.com/FooSoft/anki-connect) for any local anki integrations.
4. Install dependencies for home-db. Assumption for root directory of this project.
```
pipenv install
```
5. Run the shell `pipenv shell`
6. Run migrations if the db is not up to date `home/manage.py makemigrations kindle`
7. Start django server `home/manage.py runserver`.
