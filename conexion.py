from flask import Flask, redirect, render_template
import mysql.connector

my_db = mysql.connector.connect(host = "localhost",
                                port = "3306",
                                user = "root",
                                password = "",
                                database = "cavas")

if __name__=="__main__":
    my_db.run(debug=True, port=5080)
