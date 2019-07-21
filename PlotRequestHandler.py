import matplotlib.pyplot as plt
import pandas as pd
import io
from http.server import HTTPServer,BaseHTTPRequestHandler
import urllib
import inspect

# TODO: go through this code and adjust it -- add plots

class PlotRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        args = urllib.parse.parse_qs(self.path[2:])
        args = {i:args[i][0] for i in args}
        html = ''

        if 'mode' not in args:
            plots = ''
            for member in dir(self):
                if member[:5] == 'plot_':
                    plots += f'<a href="http://{self.server.server_name}:{self.server.server_port}/?mode=paramcheck&graph={member}">{member[5:].replace("_"," ").title()}</a><br/>\n'
            html = f'''<html><body><h1>Available Plots</h1>{plots}</body></html>'''

        elif args['mode'] == 'paramcheck':
            plotargs = inspect.getargspec(getattr(self,args['graph'])).args
            if len(plotargs) == 1 and plotargs[0].lower()=='self':
                args['mode'] = 'plotpage'
            else:
                for arg in plotargs:
                    if arg.lower() != 'self':
                        html += f"<input name='{arg}' placeholder='{arg}' value='' /><br />\n"
                html = f"<html><body><h1>Parameters:</h1><form method='GET'>{html}<input name='refresh_every' value='60' />(Refresh in sec)<br /><input type='hidden' name='mode' value='plotpage'/><input type='hidden' name='graph' value='{args['graph']}'/><input type='submit' value='Plot!'/></form></body></html>"

        elif args['mode'] == 'plotpage':
            html = f'''<html><head><meta http-equiv="refresh" content="{args['refresh_every']};URL=\'http://{self.server.server_name}:{self.server.server_port}{self.path}\'" /></head>
                       <body><img src="http://{self.server.server_name}:{self.server.server_port}{self.path.replace('plotpage','plot')}" /></body>'''

        elif args['mode'] == 'plot':
            try:
                plt = getattr(self,args['graph'])(*tuple((args[arg] for arg in inspect.getargspec(getattr(self,args['graph'])).args if arg in args)))
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                plt.savefig(self.wfile, format='png')
            except Exception as e:
                html = f"<html><body><h1>Error:</h1>{e}</body></html>"

        if html != '':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html,'utf-8'))

    def plot(self, file_path, sheet_name=None):
        # TODO Add plots
        pass


def main(server_port:"Port to serve on."=9999,server_address:"Local server name."=''):
    httpd = HTTPServer((server_address, server_port), PlotRequestHandler)
    print(f'Serving on http://{httpd.server_name}:{httpd.server_port} ...')
    httpd.serve_forever()


if __name__ == '__main__':
    import plac; plac.call(main)