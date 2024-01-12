from .models import Review

def average_rate(movie):
    reviews = Review.objects.filter(movie=movie)

    reviews_sum=0
    reviews_count=reviews.count()
    
    for i in reviews:
        reviews_sum += i.rating
        
    avg = reviews_sum/reviews_count
    
    return avg
    