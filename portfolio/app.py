#!/usr/bin/python3
""" The portfolio factory """

from portfolio import createapp
from flask_mail import Mail
from flask import render_template


app = createapp('development')
mail = Mail(app)


# Register blueprint
from portfolio.views.main import main_bp
app.register_blueprint(main_bp)

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return render_template("errors/404.html"), 404





"""
if __name__ == "__main__":
    print('ready and close to debug')
    app.run(port=8500)
"""