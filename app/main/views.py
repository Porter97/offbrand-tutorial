from . import main


# Index
@main.route('/')
def index():
    return "Hello World!", 200
