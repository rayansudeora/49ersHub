from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import requests
import json
import depth_chart_scraper
import injuries_scraper
import madden_tournament


app = Flask(__name__)



@app.route('/')
def index():
	return render_template("home.html")

@app.route("/depthchart")
def form():
	return render_template("dc_form.html")

@app.route("/depthchart",methods=["POST"])
def retrieve_data():
	text = request.form["selectpositions"]
	if text.lower() == "wr":
		return render_template("wr_postform.html", text=text, data=depth_chart_scraper.main(text))
	else:
		return render_template("dc_postform.html", text=text, data=depth_chart_scraper.main(text))


@app.route("/injuries")
def injuries():
	return render_template("injuries.html", data=injuries_scraper.main())


@app.route("/madden-tournament-generator")
def madden():
	return render_template("madden_form.html")

@app.route("/madden-tournament-generator",methods=["POST"])
def madden_data():
	text = request.form["selectgames"]
	if text.lower() == "1 game (conference)":
		return render_template("madden_generator_onegameconf.html", text=text, data=madden_tournament.main())
	if text.lower() == "1 game (out of conference)":
		return render_template("madden_generator_onegameout.html", text=text, data=madden_tournament.main())
	if text.lower() == "2 games (one division, one conference)":
		return render_template("madden_generator_twogamesconf.html", text=text, data=madden_tournament.main())
	if text.lower() == "2 games (one division, one out-of-conference)":
		return render_template("madden_generator_twogamesout.html", text=text, data=madden_tournament.main())
	if text.lower() == "3 games":
		return render_template("madden_generator_threegames.html", text=text, data=madden_tournament.main())
	if text.lower() == "4 games":
		return render_template("madden_generator_four.html", text=text, data=madden_tournament.main())


if __name__ == '__main__':
	app.run(debug=True)
