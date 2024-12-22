def positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0
    else:
        return (sum(r >= 4 for r in ratings) / len(ratings) * 100) 

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback_percentage(ratings):.2f}%")
