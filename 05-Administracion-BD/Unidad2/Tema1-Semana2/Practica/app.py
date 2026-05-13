from datetime import datetime
import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
from apscheduler.schedulers.background import BackgroundScheduler

from database import BACKUP_DIR, DATABASE, SERVER, ensure_schema, get_backup_history, get_connection, get_dashboard_stats, seed_random_sale

app = Flask(__name__)
scheduler = BackgroundScheduler(daemon=True)


def format_money(value):
    return f"${value:,.2f}"


app.jinja_env.filters['money'] = format_money


def seed_job():
    connection = get_connection()
    try:
        ensure_schema(connection)
        return seed_random_sale(connection)
    finally:
        connection.close()


def backup_status():
    connection = get_connection()
    try:
        history = get_backup_history(connection, limit=25)
        stats = get_dashboard_stats(connection)
        return history, stats
    finally:
        connection.close()


def boot():
    connection = get_connection()
    try:
        ensure_schema(connection)
    finally:
        connection.close()

    if os.getenv('DISABLE_SCHEDULER', '0') not in {'1', 'true', 'yes'} and not scheduler.running:
        scheduler.add_job(seed_job, 'interval', minutes=3, id='seed_sale_job', replace_existing=True)
        scheduler.start()


boot()


@app.route('/')
def index():
    connection = get_connection()
    try:
        stats = get_dashboard_stats(connection)
        backups = get_backup_history(connection, limit=25)
    finally:
        connection.close()

    return render_template(
        'index.html',
        server=SERVER,
        database=DATABASE,
        backup_dir=BACKUP_DIR,
        stats=stats,
        backups=backups,
        now=datetime.now(),
    )


@app.route('/seed', methods=['POST'])
def seed_now():
    seed_job()
    return redirect(url_for('index'))


@app.route('/backups')
def backups_json():
    connection = get_connection()
    try:
        backups = get_backup_history(connection, limit=100)
    finally:
        connection.close()
    return jsonify(backups)


@app.route('/refresh')
def refresh():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
