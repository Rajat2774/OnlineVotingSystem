# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elections.db'
# db = SQLAlchemy(app)

# # Define models for Election and Candidate
# class Election(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

# class Candidate(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     votes = db.Column(db.Integer, default=0)  # Vote count for the candidate
#     election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)

# # Route to display election results
# @app.route('/election_results/<int:election_id>')
# def election_results(election_id):
#     # Query candidates and their vote counts for the given election ID
#     candidates = Candidate.query.filter_by(election_id=election_id).all()

#     # Sort candidates by vote count (descending order)
#     sorted_candidates = sorted(candidates, key=lambda x: x.votes, reverse=True)

#     # Render the election results template and pass candidates data
#     return render_template('election_results.html', candidates=sorted_candidates)

# if __name__ == '__main__':
#     app.run(debug=True)
