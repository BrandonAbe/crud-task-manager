from app import create_app

# Creation of app entry point
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
