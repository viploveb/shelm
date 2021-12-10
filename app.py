from flask import Flask, jsonify, send_from_directory, render_template, redirect
import os

UPLOAD_DIRECTORY = "./charts/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

api = Flask(__name__)

@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/files/<path:path>",methods=['GET'])
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/get/shelm")
def get_shelm():
    return redirect("https://raw.githubusercontent.com/viploveb/civo_hackathon/master/user/install.sh?token=AKYGPR52K32KNLV4JS7GEQDBTIQIO")

@api.route("/install/shelm")
def download_shelm():
    """Download shelm"""
    return send_from_directory('./user','shelm.py', as_attachment=True)