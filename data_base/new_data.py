from data_base.data_base_users import Database
db = Database("database.db")

# db.add_user(
#     user_id=1,
#     email="slavik@gmail.com",
#     password="hashed_password",
#     two_factor_ak="True",
#     two_factor_aa="True",
#     two_factor_an="False",
#     two_factor_ae="True",
#     name="John Doe",
#     date="2024-11-28",
#     Account="False",
#     Activating="False",
#     KYSREST="False",
#     KYSDATA="love"
# )
#
db.add_user(
    user_id=6,
    email="slavik1234111@gmail.com",
    password="lovebeer",
    two_factor_ak="True",
    two_factor_aa="True",
    two_factor_an="False",
    two_factor_ae="True",
    name="John Doe",
    date="2024-11-28",
    Account="False",
    Activating="False",
    KYSREST="False",
    KYSDATA="Sometext"
)

#db.add_column_to_table("database.db", "users", "PersonAdress", "TEXT")