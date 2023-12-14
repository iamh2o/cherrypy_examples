import cherrypy
import os
import sys
import json

from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests


YOUR_CALLBACK_URL = 'https://localhost:8912/login_callback'
SERVER_CRT_FILE  = 'certs/server.crt'
SERVER_KEY_FILE = 'certs/server.key'
GOOG_CREDENTIALS = os.environ.get('HOME','/home/ubuntu')+'/.config/google_oauth/google_oauth.json'


def credentials_to_dict(credentials):
    return {'token': credentials.token,
	    'refresh_token': credentials.refresh_token,
	    'token_uri': credentials.token_uri,
	    'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


def require_login():
    """Decorator to require login for certain pages."""
    def decorator(func):
        def wrapper(instance, *args, **kwargs):
            if 'credentials' not in cherrypy.session or not cherrypy.session['credentials']:
                raise cherrypy.HTTPRedirect('/login')
            return func(instance, *args, **kwargs)
        return wrapper
    return decorator

class Goauth2(object):
    def __init__(self, rdir=None, site=None, skip='simple'):
        with open(GOOG_CREDENTIALS, 'r') as f:
            client_config = json.load(f)

        self.flow = Flow.from_client_config(
            client_config,
            scopes=['openid','https://www.googleapis.com/auth/userinfo.email','https://www.googleapis.com/auth/userinfo.profile'],
            redirect_uri=YOUR_CALLBACK_URL
	    )


    @cherrypy.expose
    @require_login()
    def index(self):
        return "You're in."

    @cherrypy.expose
    def login(self,username=None, password=None,referer='/'):
        authorization_url, state = self.flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        cherrypy.session['state'] = state
        raise cherrypy.HTTPRedirect(authorization_url)




    @cherrypy.expose
    def login_callback(self, state, code, scope,authuser, hd, prompt):

        self.flow.fetch_token(code=code)
        credentials = self.flow.credentials
        cherrypy.session['credentials'] = credentials_to_dict(credentials)

        access_token = credentials.token
        userinfo_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {'Authorization': f'Bearer {access_token}'}
            
        try:
            response = requests.get(userinfo_url, headers=headers)
            if response.status_code == 200:
                user_info = response.json()
                user_email = user_info.get('email', 'Email not found')
                cherrypy.session['user_email'] = user_email  # Store the email in the session

                print(f"SUCCESSFULLY fetched user info. Status code: {response.status_code} .. {user_email}", file=sys.stderr)
            else:
                raise Exception(f"Failed to fetch user info. Status code: {response.status_code}", file=sys.stderr)

        except Exception as e:
            print(f"Failed to fetch user info. Deets: {e}", file=sys.stderr)

        raise cherrypy.HTTPRedirect('/')
    

if __name__ == '__main__':
    
    if len(sys.argv[1]) != 1 or not os.path.exists(sys.argv[1]):
        raise Exception(f"The first argument to invoke the server is the path to the root run dir. From the same dir as the script, '.' is sufficent.")
    
    root_server_dir = os.path.abspath(sys.argv[1])
    
    
    cherrypy.config.update(  {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': root_server_dir,
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8912,
        'tools.sessions.on': True,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate':  SERVER_CRT_FILE,
        'server.ssl_private_key': SERVER_KEY_FILE
    })

    cherrypy.quickstart(Goauth2(), '/')