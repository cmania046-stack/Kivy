[app]
title = Manajemen Produk POS
package.name = manajemenpos
package.domain = org.manajemenpos

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,db,txt
source.exclude_dirs = .github,.buildozer,bin,__pycache__,.git

version = 0.1

# Tambahkan library lain di sini, pisahkan koma
requirements = python3,kivy,sqlite3,flask,werkzeug,jinja2,markupsafe,itsdangerous,click,blinker

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
