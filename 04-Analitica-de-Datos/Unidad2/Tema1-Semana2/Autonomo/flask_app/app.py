from __future__ import annotations

from flask import Flask, render_template

from analysis_pipeline import build_dashboard


app = Flask(__name__)
dashboard = None


def get_dashboard():
    global dashboard
    if dashboard is None:
        dashboard = build_dashboard()
    return dashboard


@app.route("/")
def index() -> str:
    return render_template("index.html", data=get_dashboard())


@app.route("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
