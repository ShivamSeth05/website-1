from app import create_app

app = create_app('config.heroku_config')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
