bind="0.0.0.0:8080"
pythonpath="/home/box/web"

def app(environ, start_response):
   query = environ.get('QUERY_STRING')
   body = query.replace('&','\n')
   status = '200 OK'
   headers = [
      ('Content-Type','text/plain')
   ]
start_response(status, headers)
return [body]