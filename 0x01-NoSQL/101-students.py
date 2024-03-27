#!/usr/bin/env python3
"""Module returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns average scores of students with the top ordered"""
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
		}
        }
    ])
