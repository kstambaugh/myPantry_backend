# from flask import Flask, redirect, url_for, render_template

from pantry_api import create_app

app = create_app()


if __name__ == '__main__':
    app.run()