# models.py
from app.utils import db

class CompletedMatches(db.Model):
    __tablename__ = 'completed_matches'
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(100))
    away = db.Column(db.String(100))
    date_and_time = db.Column(db.String(50))
    home_win_probability = db.Column(db.Float)
    draw_probability = db.Column(db.Float)
    away_win_probability = db.Column(db.Float)
    team_to_win_prediction = db.Column(db.Integer)
    average_goals_prediction = db.Column(db.Float)
    weather_in_degrees = db.Column(db.String(50))
    odds = db.Column(db.Float)
    full_time_score = db.Column(db.String(50))
    score_at_halftime = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    time = db.Column(db.String(50))
    home_team_score_prediction = db.Column(db.Integer)
    away_team_score_prediction = db.Column(db.Integer)
    home_team_full_time_score = db.Column(db.Integer)
    away_team_full_time_score = db.Column(db.Integer)
    home_team_halftime_score = db.Column(db.Integer)
    away_team_halftime_score = db.Column(db.Integer)
    prediction_result = db.Column(db.String(50))
    day_of_week = db.Column(db.Integer)
    month = db.Column(db.Integer)
    weekly_round = db.Column(db.BigInteger)


class UpcomingMatches(db.Model):
    __tablename__ = 'upcoming_matches'
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.Integer)
    away = db.Column(db.Integer)
    date_and_time = db.Column(db.String(50))
    home_win_probability = db.Column(db.Float)
    draw_probability = db.Column(db.Float)
    away_win_probability = db.Column(db.Float)
    team_to_win_prediction = db.Column(db.Integer)
    scoreline_prediction = db.Column(db.String(100))
    average_goals_prediction = db.Column(db.Float)
    weather_in_degrees = db.Column(db.String(50))
    odds = db.Column(db.Float)
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    home_team_score_prediction = db.Column(db.Integer)
    away_team_score_prediction = db.Column(db.Integer)
    day_of_week = db.Column(db.Integer)
    month = db.Column(db.Integer)
    weekly_round = db.Column(db.Integer)


class CurrentWeekLeagueStandings(db.Model):
    __tablename__ = 'current_week_league_standings'
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer)
    team = db.Column(db.Integer)
    pld = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    gf = db.Column(db.Integer)
    ga = db.Column(db.Integer)
    ppg_last_5_matches = db.Column(db.Float)
    points = db.Column(db.Integer)


class PreviousWeekLeagueStandings(db.Model):
    __tablename__ = 'previous_week_league_standings'
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer)
    team = db.Column(db.Integer)
    pld = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    gf = db.Column(db.Integer)
    ga = db.Column(db.Integer)
    ppg_last_5_matches = db.Column(db.Float)
    points = db.Column(db.Integer)


class TestingData(db.Model):
    __tablename__ = 'testing_data'
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.Integer)
    away = db.Column(db.Integer)
    date_and_time = db.Column(db.String(50))
    home_win_probability = db.Column(db.Float)
    draw_probability = db.Column(db.Float)
    away_win_probability = db.Column(db.Float)
    team_to_win_prediction = db.Column(db.Integer)
    scoreline_prediction = db.Column(db.String(100))
    average_goals_prediction = db.Column(db.Float)
    weather_in_degrees = db.Column(db.String(50))
    odds = db.Column(db.Float)
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    home_team_score_prediction = db.Column(db.Integer)
    away_team_score_prediction = db.Column(db.Integer)
    day_of_week = db.Column(db.Integer)
    month = db.Column(db.Integer)
    weekly_round = db.Column(db.Integer)
    home_team_pos = db.Column(db.Integer)
    home_team_matches_played = db.Column(db.Integer)
    home_team_wins = db.Column(db.Integer)
    home_team_draws = db.Column(db.Integer)
    home_team_losses = db.Column(db.Integer)
    home_team_gf = db.Column(db.Integer)
    home_team_ga = db.Column(db.Integer)
    home_team_ppg_last_5_matches = db.Column(db.Float)
    home_team_points = db.Column(db.Integer)
    away_team_pos = db.Column(db.Integer)
    away_team_matches_played = db.Column(db.Integer)
    away_team_wins = db.Column(db.Integer)
    away_team_draws = db.Column(db.Integer)
    away_team_losses = db.Column(db.Integer)
    away_team_gf = db.Column(db.Integer)
    away_team_ga = db.Column(db.Integer)
    away_team_ppg_last_5_matches = db.Column(db.Float)
    away_team_points = db.Column(db.Integer)


class TrainingData(db.Model):
    __tablename__ = 'training_data'
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.Integer)
    away = db.Column(db.Integer)
    home_win_probability = db.Column(db.Float)
    draw_probability = db.Column(db.Float)
    away_win_probability = db.Column(db.Float)
    team_to_win_prediction = db.Column(db.Integer)
    average_goals_prediction = db.Column(db.Float)
    weather_in_degrees = db.Column(db.String(50))
    odds = db.Column(db.Float)
    full_time_score = db.Column(db.String(100))
    score_at_halftime = db.Column(db.String(100))
    date_and_time = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    home_team_score_prediction = db.Column(db.Integer)
    away_team_score_prediction = db.Column(db.Integer)
    home_team_full_time_score = db.Column(db.Integer)
    away_team_full_time_score = db.Column(db.Integer)
    home_team_halftime_score = db.Column(db.Integer)
    away_team_halftime_score = db.Column(db.Integer)
    prediction_result = db.Column(db.Integer)
    day_of_week = db.Column(db.Integer)
    month = db.Column(db.Integer)
    weekly_round = db.Column(db.Integer)
    home_team_pos = db.Column(db.Integer)
    home_team_matches_played = db.Column(db.Integer)
    home_team_wins = db.Column(db.Integer)
    home_team_draws = db.Column(db.Integer)
    home_team_losses = db.Column(db.Integer)
    home_team_gf = db.Column(db.Integer)
    home_team_ga = db.Column(db.Integer)
    home_team_ppg_last_5_matches = db.Column(db.Float)
    home_team_points = db.Column(db.Integer)
    away_team_pos = db.Column(db.Integer)
    away_team_matches_played = db.Column(db.Integer)
    away_team_wins = db.Column(db.Integer)
    away_team_draws = db.Column(db.Integer)
    away_team_losses = db.Column(db.Integer)
    away_team_gf = db.Column(db.Integer)
    away_team_ga = db.Column(db.Integer)
    away_team_ppg_last_5_matches = db.Column(db.Float)
    away_team_points = db.Column(db.Integer)


