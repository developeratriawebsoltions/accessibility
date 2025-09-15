# app.py
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Serve widget at root path so sites can embed: <script src="https://yourdomain.com/widget.js"></script>
@app.route('/widget.js')
def widget_js():
    return send_from_directory('static', 'widget.js', mimetype='application/javascript')

# Serve the stylesheet conveniently
@app.route('/style.css')
def style_css():
    return send_from_directory('static', 'style.css', mimetype='text/css')

# Serve fonts (optional - Flask already serves /static but explicit route is fine)
@app.route('/fonts/<path:filename>')
def fonts(filename):
    return send_from_directory('static/fonts', filename)

# Test page (optional)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
