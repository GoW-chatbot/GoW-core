## Grapes of Wrath

A web chatbot using django

### Installation guide:

Clone the repository and make a virtual environment:
```
git clone https://github.com/aliPMPAINT/GoW.git
cd GoW
virtualenv GoW_venv
```

For Linux/Mac:
```
source GoW_venv/bin/activate
```

For Windows:
```
.\GoW_venv\Scripts\activate
```

Then install the dependencies:
```
pip install -r requirements.txt
```

Start the server:
```
python manage.py runserver
```

### To do

- [ ] Nice UI and works on the front-end
- [ ] Instructions on how to use any desired chatbot model and add a default one
- [ ] Add a database and store the chats
- [ ] Having the ability to train the chatbot based on the new data
- [ ] Deploying it
