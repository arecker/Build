Build
=====

My little github webhooks endbpoint

### Setting up

'''bash
$ git clone http://github.com/arecker/Build.git
$ cd Build && virtualenv .env
$ ./.env/bin/pip install -r requirements
$ ./.env/bin/python main.py
```

### Config

Put all configuration in a local ```repos.json``` file in the same directory as the project.

```javascript
{
    "YourUserName/YourRepo": "/full/path/to/your/build/script"
}
```

### Debugging

I would have set this up a lot faster if I new this.  To execute a script as *Apache*, do

```bash
sudo su - www-data -c '/path/to/your/script'
```

Figuring out permissions is much easier this way.
