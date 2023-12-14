# Cherrypy Examples

I'm a fan of cherrypy for rapid development of UIs when exploring problem spaces which benefity from some UI to share tools or data.  In the course of working with cherrypy, I've put together some recipies which have prooven useful, and shared here. Docs are not inteneded to be exhaustive, these are examples only (also, no tests).

## Google Oauth2
Quick solution to get google oauth2 authentication working with cherrypy. The script requires some variables to be set at the head of the script (which would in the real world be set more pleasantly).

### Steps!
* Go to your google console, get your oauth credentials and register your app _importantly, your callback url_.
* Save your credentials in `client_secret.json`.
* Create your cert files and save in `certs/{server.crt,server.key}`.
* I set up the following conda env: `conda create -n CPGOA2 -c conda-forge cherrypy cherrypy==18.8.0 google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2`.
* Activate it: `conda activate CPGOA2`.
* run the server: `python goauth2_cpy.py . `. You'll see output blocking stdout like:
```text
 python goauth2_cpy.py .
[14/Dec/2023:04:52:31] ENGINE Listening for SIGTERM.
[14/Dec/2023:04:52:31] ENGINE Listening for SIGHUP.
[14/Dec/2023:04:52:31] ENGINE Listening for SIGUSR1.
[14/Dec/2023:04:52:31] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[14/Dec/2023:04:52:31] ENGINE Started monitor thread 'Autoreloader'.
[14/Dec/2023:04:52:31] ENGINE Serving on https://0.0.0.0:8912
[14/Dec/2023:04:52:31] ENGINE Bus STARTED* 
```

* Visit the URL `https://localhost:8912`.
  * Depending on how you've created your certs, you may be blocked here or warned about the security of the site.  You can either add an exception or create your own CA and sign your own certs.  

* You'll be prompted for a google login.  Depending on how you've setup your google app, users from outside your organization may not be able to login.  You can add users to your app, or create a new app for public use.

## Cherrypy Running [Cytoscape](https://cytoscape.org/) W/Jinja2 Templates
* ... see [Bloom Lims -soon-](...)
