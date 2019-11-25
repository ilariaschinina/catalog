# Catalog App for a small coding book collection
This app has been built as project for the Udacity Full Stack Web Developer Nanodegree program.
It is a small catalog app that organizes books for learning programming languages.

You can visit my app here: http://catalog-app.schinina.eu/


## Table of Contents

- [Main Features](#main-features)
- [Server Configuration](#server-configuration)


## Main Features

* The basic CRUD functionalities have been implemented and only the authorized users can have access to them
* The app supports OAuth2 login with Google
* The project implements JSON endpoints that serve the same information as displayed in the HTML endpoints:
    * for arbitrary item in the catalog
    * for all categories
    * for a single category


## Server Configuration

The second part of the project for Udacity was the setup of a Linux server to host the app. The requirements were: 
* Updating all currently installed packages
* Changing the SSH port from 22 to 2200
* Configuring the UFW to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)
* Creating a new user for the project reviewer, `grader`, giving sudo permissions, configuring SSH authorisation access
* Configurimg the local timezone to UTC
* Installing and configuring Apache to serve a Python mod_wsgi application
* Installing and configuring PostgreSQL:
	* Creating a new database user named catalog with limited permissions to my catalog application database
