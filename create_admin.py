from apps import create_app
from ext import db
from models import User


app = create_app()


with app.app_context():

    admin = User(
        username="admin",
        is_admin=True
    )

    admin.set_password("admin123")


    db.session.add(admin)

    db.session.commit()


    print("Admin created")


# =========================
# შესვლა username: admin password: admin123
# =========================