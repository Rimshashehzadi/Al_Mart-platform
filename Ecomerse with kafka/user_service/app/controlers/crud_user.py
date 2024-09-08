from sqlmodel import Session, select
from app.models.user_models import UserModel, User
from app.db.db_connection import DB_SESSION


def user_add(user_details:UserModel, session:DB_SESSION):
     db_statement = select(User).where(User.user_email == user_details.user_email).where(User.user_password == user_details.user_password)
     db_user_info = session.exec(db_statement).one_or_more()
     if db_user_info:
          print("User already ex")
          # TODO: add exception here
     else:
          User = select(User)
          session.add(User)
          session.comit()
          session.refresh(User)
          return user_details
               