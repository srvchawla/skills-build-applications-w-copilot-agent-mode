from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thor", "age": 30, "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Tony Stark", "age": 35, "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Steve Rogers", "age": 32, "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff", "age": 28, "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "age": 40, "created_at": datetime.now()},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60, "date": "2025-04-07"},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120, "date": "2025-04-06"},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 90, "date": "2025-04-05"},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30, "date": "2025-04-04"},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 75, "date": "2025-04-03"},
        ]
        db.activity.insert_many(activities)

        # Insert leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "points": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "points": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "points": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "points": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon", "duration": 90},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength", "duration": 30},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
