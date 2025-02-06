import os
from os.path import dirname, join

from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")
SECRET_KEY = os.environ.get("SECRET_KEY")

app.secret_key = SECRET_KEY



# ROUTE HALAMAN HOME
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# ROUTE HALAMAN SEJARAH
@app.route("/profil/sejarah", methods=["GET"])
def sejarah():
    return render_template("sejarah.html")

# ROUTE HALAMAN VISI MISI
@app.route("/profil/visi-misi", methods=["GET"])
def visi_misi():
    return render_template("visi_misi.html")

# ROUTE HALAMAN ALAMAT DAN LOKASI
@app.route("/profil/alamat", methods=["GET"])
def alamat():
    return render_template("alamat.html")

# ROUTE HALAMAN STRUKTUR ORGANISASI
@app.route("/pejabat", methods=["GET"])
def struktur():
    return render_template("struktur.html")

# ROUTE HALAMAN PEJABAT
@app.route("/organisasi/pejabat", methods=["GET"])
def pejabat():
    return render_template("pejabat.html")

# ROUTE HALAMAN GALERI
@app.route("/galeri", methods=["GET"])
def galeri():
    return render_template("galeri.html")

# Rute untuk halaman Program Pendidikan
@app.route("/fasilitas/pendidikan")
def program_pendidikan():
    return render_template("program_pendidikan.html")

# Rute untuk halaman Program Kesehatan
@app.route("/fasilitas/kesehatan")
def program_kesehatan():
    return render_template("program_kesehatan.html")

# Rute untuk halaman Program Infrastruktur
@app.route("/fasilitas/kegiatan")
def program_kegiatan():
    return render_template("program_kegiatan.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)