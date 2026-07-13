from apps import create_app
from ext import db
from models import News

app = create_app()

with app.app_context():

    # Clear old data
    db.session.query(News).delete()

    news_list = [
        News(
            title="AI is Changing the Future of Work",
            category="AI",
            author="Tech Insider",
            image="https://images.unsplash.com/photo-1677442136019-21780ecad995",
            description="Artificial Intelligence is reshaping jobs, automation, and productivity across all industries."
        ),
        News(
            title="Apple Unveils Next-Gen Smart Devices",
            category="Technology",
            author="John Carter",
            image="https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5",
            description="Apple introduces new devices powered by advanced AI and seamless ecosystem integration."
        ),
        News(
            title="Cybersecurity Becomes Top Global Priority",
            category="Security",
            author="Cyber News",
            image="https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
            description="Companies worldwide are investing heavily to protect against rising cyber threats."
        ),
        News(
            title="Gaming Industry Enters Virtual Reality Era",
            category="Gaming",
            author="Game Hub",
            image="https://images.unsplash.com/photo-1593305841991-05c297ba4575",
            description="VR and immersive gaming technologies are redefining entertainment experiences."
        ),
        News(
            title="Smart Cities Are Becoming Reality",
            category="Innovation",
            author="Urban Tech",
            image="https://images.unsplash.com/photo-1496307653780-42ee777d4833",
            description="Cities are adopting IoT and AI systems to improve transportation and energy usage."
        ),
        News(
            title="Space Exploration Reaches New Milestones",
            category="Science",
            author="Space Daily",
            image="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",
            description="Private companies and NASA continue pushing the boundaries of space exploration."
        ),
    ]

    db.session.add_all(news_list)
    db.session.commit()