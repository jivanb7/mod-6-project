from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_product_images():
    product_images = [

        ProductImage(product_id=1, preview_image=True, image_url="https://m.media-amazon.com/images/I/A1zwzDM2PEL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=1, preview_image=False, image_url="https://m.media-amazon.com/images/I/A1FfvMFlfxL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=1, preview_image=False, image_url="https://m.media-amazon.com/images/I/71bUW6n1eJL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=1, preview_image=False, image_url="https://m.media-amazon.com/images/I/813mKlVnFIL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=1, preview_image=False, image_url="https://m.media-amazon.com/images/I/81wtKQxL9cL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=2, preview_image=True, image_url="https://m.media-amazon.com/images/I/61LrWh6JTML._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=2, preview_image=False, image_url="https://m.media-amazon.com/images/I/61Zyf7qG1pL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=2, preview_image=False, image_url="https://m.media-amazon.com/images/I/61UUVdR-5uL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=2, preview_image=False, image_url="https://m.media-amazon.com/images/I/61X7VpEWdLL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=2, preview_image=False, image_url="https://m.media-amazon.com/images/I/61aOvU7i4hL._AC_SX679_.jpg", created_at=datetime.now()),

  
        ProductImage(product_id=3, preview_image=True, image_url="https://m.media-amazon.com/images/I/71XApUwUlzL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=3, preview_image=False, image_url="https://m.media-amazon.com/images/I/71N2l4hwayL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=3, preview_image=False, image_url="https://m.media-amazon.com/images/I/71HFKSVm32L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=3, preview_image=False, image_url="https://m.media-amazon.com/images/I/71yIvHzZrDL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=3, preview_image=False, image_url="https://m.media-amazon.com/images/I/7197aK4uZpL._AC_SX679_.jpg", created_at=datetime.now()),

     
        ProductImage(product_id=4, preview_image=True, image_url="https://m.media-amazon.com/images/I/71RlfX7YEhL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=4, preview_image=False, image_url="https://m.media-amazon.com/images/I/81FWWZiX5GL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=4, preview_image=False, image_url="https://m.media-amazon.com/images/I/81AxQJvNUvL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=4, preview_image=False, image_url="https://m.media-amazon.com/images/I/81rh-Dz0nEL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=4, preview_image=False, image_url="https://m.media-amazon.com/images/I/71LHUSd36lL._AC_SX679_.jpg", created_at=datetime.now()),

    
        ProductImage(product_id=5, preview_image=True, image_url="https://m.media-amazon.com/images/I/61iHxc-3BhL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=5, preview_image=False, image_url="https://m.media-amazon.com/images/I/51yn-UHB38L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=5, preview_image=False, image_url="https://m.media-amazon.com/images/I/61jmnK6bc9L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=5, preview_image=False, image_url="https://m.media-amazon.com/images/I/71PheG-fqnL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=5, preview_image=False, image_url="https://m.media-amazon.com/images/I/51sCZ+qq4NS._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=6, preview_image=True, image_url="https://m.media-amazon.com/images/I/81hMqa5t+KL._AC_SY300_SX300_.jpg", created_at=datetime.now()),
        ProductImage(product_id=6, preview_image=False, image_url="https://m.media-amazon.com/images/I/81AzwsrVZcL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=6, preview_image=False, image_url="https://m.media-amazon.com/images/I/81o9YLWEG7L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=6, preview_image=False, image_url="https://m.media-amazon.com/images/I/81i7P3JbXVL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=6, preview_image=False, image_url="https://m.media-amazon.com/images/I/71tldvar+hL._AC_SX679_.jpg", created_at=datetime.now()),

 
        ProductImage(product_id=7, preview_image=True, image_url="https://m.media-amazon.com/images/I/81BC6eEeG6L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=7, preview_image=False, image_url="https://m.media-amazon.com/images/I/81aFrisI5yL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=7, preview_image=False, image_url="https://m.media-amazon.com/images/I/814HhBdIiOL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=7, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Gv1E3ZQxL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=7, preview_image=False, image_url="https://m.media-amazon.com/images/I/81BuoQdiunL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=8, preview_image=True, image_url="https://m.media-amazon.com/images/I/81NfXRfOp4L.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=8, preview_image=False, image_url="https://m.media-amazon.com/images/I/71At9PncrlL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=8, preview_image=False, image_url="https://m.media-amazon.com/images/I/81-wosmthUL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=8, preview_image=False, image_url="https://m.media-amazon.com/images/I/81Cz9rEyBnL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=8, preview_image=False, image_url="https://m.media-amazon.com/images/I/81SIRfI85sL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=9, preview_image=True, image_url="https://m.media-amazon.com/images/I/41+TTZfwxCL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=9, preview_image=False, image_url="https://m.media-amazon.com/images/I/41Cdh4rybPL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=9, preview_image=False, image_url="https://m.media-amazon.com/images/I/41F9j-2QoYL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=9, preview_image=False, image_url="https://m.media-amazon.com/images/I/61kKkrzGiyL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=9, preview_image=False, image_url="https://m.media-amazon.com/images/I/61AoEMZqiSL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=10, preview_image=True, image_url="https://m.media-amazon.com/images/I/514ZwNRZ5zL._SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=10, preview_image=False, image_url="https://m.media-amazon.com/images/I/81Ukb+MDQwL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=10, preview_image=False, image_url="https://m.media-amazon.com/images/I/71dMIJYdfoL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=10, preview_image=False, image_url="https://m.media-amazon.com/images/I/81R0fhZEQsL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=10, preview_image=False, image_url="https://m.media-amazon.com/images/I/81GhW8wzpnL._SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=11, preview_image=True, image_url="https://m.media-amazon.com/images/I/71htnPK8C7L.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=11, preview_image=False, image_url="https://m.media-amazon.com/images/I/71JLGvGcqHL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=11, preview_image=False, image_url="https://m.media-amazon.com/images/I/71-Jh5Hc1HL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=11, preview_image=False, image_url="https://m.media-amazon.com/images/I/71htnPK8C7L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=11, preview_image=False, image_url="https://m.media-amazon.com/images/I/71kDKxiQb0L._AC_SX679_.jpg", created_at=datetime.now()),

     
        ProductImage(product_id=12, preview_image=True, image_url="https://m.media-amazon.com/images/I/B1WGlLC+iaL._CLa%7C2140%2C2000%7CB1XsfyTaM-L.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png", created_at=datetime.now()),
        ProductImage(product_id=12, preview_image=False, image_url="https://m.media-amazon.com/images/I/B1mEhjGJ2nL._CLa%7C2140%2C2000%7CB1RIiRqXEXL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png", created_at=datetime.now()),
        ProductImage(product_id=12, preview_image=False, image_url="https://m.media-amazon.com/images/I/B1mEhjGJ2nL._CLa%7C2140%2C2000%7CB1wWbMUNS8L.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png", created_at=datetime.now()),
        ProductImage(product_id=12, preview_image=False, image_url="https://m.media-amazon.com/images/I/B1WGlLC+iaL._CLa%7C2140%2C2000%7CB1v7T5ypVKS.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png", created_at=datetime.now()),
        ProductImage(product_id=12, preview_image=False, image_url="https://m.media-amazon.com/images/I/A1mN82gBRyL._CLa%7C2140%2C2000%7CA1oxXdhwvaL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png", created_at=datetime.now()),


        ProductImage(product_id=13, preview_image=True, image_url="https://m.media-amazon.com/images/I/81lodLWZobL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=13, preview_image=False, image_url="https://m.media-amazon.com/images/I/81lnUCwWopL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=13, preview_image=False, image_url="https://m.media-amazon.com/images/I/814EIyG-GSL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=13, preview_image=False, image_url="https://m.media-amazon.com/images/I/81yhrUbCyLL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=13, preview_image=False, image_url="https://m.media-amazon.com/images/I/81lHqU9Y7fL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=14, preview_image=True, image_url="https://m.media-amazon.com/images/I/71U5jiJmyGL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=14, preview_image=False, image_url="https://m.media-amazon.com/images/I/71-RCk+GzdL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=14, preview_image=False, image_url="https://m.media-amazon.com/images/I/81IZmHDhGVL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=14, preview_image=False, image_url="https://m.media-amazon.com/images/I/81CvZQi4qdL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=14, preview_image=False, image_url="https://m.media-amazon.com/images/I/81JyxjfpcDL._AC_SX679_.jpg", created_at=datetime.now()),

   
        ProductImage(product_id=15, preview_image=True, image_url="https://m.media-amazon.com/images/I/51A3SG-+5lL._SY300_SX300_.jpg", created_at=datetime.now()),
        ProductImage(product_id=15, preview_image=False, image_url="https://m.media-amazon.com/images/I/61PP+Aa8uQL.jpg", created_at=datetime.now()),
        ProductImage(product_id=15, preview_image=False, image_url="https://m.media-amazon.com/images/I/71fKnUeqBoL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=15, preview_image=False, image_url="https://m.media-amazon.com/images/I/71YNZ24iRFL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=15, preview_image=False, image_url="https://m.media-amazon.com/images/I/71G3jXkv+zL._SX679_.jpg", created_at=datetime.now()),



        ProductImage(product_id=16, preview_image=True, image_url="https://m.media-amazon.com/images/I/71wTEonFOVL.__AC_SY300_SX300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=16, preview_image=False, image_url="https://m.media-amazon.com/images/I/71JPk8HfWcL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=16, preview_image=False, image_url="https://m.media-amazon.com/images/I/71FhQ5uK8BL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=16, preview_image=False, image_url="https://m.media-amazon.com/images/I/81THodl5wXL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=16, preview_image=False, image_url="https://m.media-amazon.com/images/I/71iwk401TxL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=17, preview_image=True, image_url="https://m.media-amazon.com/images/I/71sNxmWduNL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=17, preview_image=False, image_url="https://m.media-amazon.com/images/I/71DJ+mJVPfL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=17, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Njkt+gJyL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=17, preview_image=False, image_url="https://m.media-amazon.com/images/I/81T-mKuJ8jL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=17, preview_image=False, image_url="https://m.media-amazon.com/images/I/71s8QfBDPqL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=18, preview_image=True, image_url="https://m.media-amazon.com/images/I/91zlIObVj3L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=18, preview_image=False, image_url="https://m.media-amazon.com/images/I/81XUUlozAVL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=18, preview_image=False, image_url="https://m.media-amazon.com/images/I/81Ssm1sHv0L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=18, preview_image=False, image_url="https://m.media-amazon.com/images/I/91yV5OuwYrL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=18, preview_image=False, image_url="https://m.media-amazon.com/images/I/91OmS9djm3L._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=19, preview_image=True, image_url="https://m.media-amazon.com/images/I/71eM8iDmyAL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=19, preview_image=False, image_url="https://m.media-amazon.com/images/I/81v0aoAEw9L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=19, preview_image=False, image_url="https://m.media-amazon.com/images/I/714lHbRqbbL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=19, preview_image=False, image_url="https://m.media-amazon.com/images/I/7183XCXJgHL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=19, preview_image=False, image_url="https://m.media-amazon.com/images/I/71xUCTOcAcL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=20, preview_image=True, image_url="https://m.media-amazon.com/images/I/61I69y29otL._SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=20, preview_image=False, image_url="https://m.media-amazon.com/images/I/A14JJQFxW5L._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=20, preview_image=False, image_url="https://m.media-amazon.com/images/I/81yV03AtF3L._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=20, preview_image=False, image_url="https://m.media-amazon.com/images/I/71szLOZFwhL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=20, preview_image=False, image_url="https://m.media-amazon.com/images/I/71a1PHSoFfL._SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=21, preview_image=True, image_url="https://m.media-amazon.com/images/I/81NVVX8rOPL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=21, preview_image=False, image_url="https://m.media-amazon.com/images/I/81qtdqXFXwL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=21, preview_image=False, image_url="https://m.media-amazon.com/images/I/81Isy6aXzyL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=21, preview_image=False, image_url="https://m.media-amazon.com/images/I/91F-vgjcP0L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=21, preview_image=False, image_url="https://m.media-amazon.com/images/I/91eCt8vOBpL._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=22, preview_image=True, image_url="https://m.media-amazon.com/images/I/61giL6bxhWL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=22, preview_image=False, image_url="https://m.media-amazon.com/images/I/71NUZIZCZuL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=22, preview_image=False, image_url="https://m.media-amazon.com/images/I/71q3+sg5tqL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=22, preview_image=False, image_url="https://m.media-amazon.com/images/I/71l48NaX2PL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=22, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Ke4qgWZwL._AC_SX679_.jpg", created_at=datetime.now()),

  
        ProductImage(product_id=23, preview_image=True, image_url="https://m.media-amazon.com/images/I/81S6V1DnLtL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=23, preview_image=False, image_url="https://m.media-amazon.com/images/I/81sTQHkx+FL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=23, preview_image=False, image_url="https://m.media-amazon.com/images/I/61pz8-zglpL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=23, preview_image=False, image_url="https://m.media-amazon.com/images/I/61KgK2q320L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=23, preview_image=False, image_url="https://m.media-amazon.com/images/I/9131fmpOe4L._AC_SX679_.jpg", created_at=datetime.now()),


        ProductImage(product_id=24, preview_image=True, image_url="https://m.media-amazon.com/images/I/71nAL3GVFNL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=24, preview_image=False, image_url="https://m.media-amazon.com/images/I/61XUDUpsHRL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=24, preview_image=False, image_url="https://m.media-amazon.com/images/I/61oogRIdsQL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=24, preview_image=False, image_url="https://m.media-amazon.com/images/I/61SjFrU8e4L._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=24, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Em0eC9cIL._AC_SY695_.jpg", created_at=datetime.now()),

        ProductImage(product_id=25, preview_image=True, image_url="https://m.media-amazon.com/images/I/61B2vzib5TL.__AC_SY300_SX300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=25, preview_image=False, image_url="https://m.media-amazon.com/images/I/71+JskHfRLL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=25, preview_image=False, image_url="https://m.media-amazon.com/images/I/71QNlvI+dSL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=25, preview_image=False, image_url="https://m.media-amazon.com/images/I/81fzyLq+n9L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=25, preview_image=False, image_url="https://m.media-amazon.com/images/I/913BNIfTcjL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=26, preview_image=True, image_url="https://m.media-amazon.com/images/I/81hlWKr23xL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=26, preview_image=False, image_url="https://m.media-amazon.com/images/I/81FVVxpa7nL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=26, preview_image=False, image_url="https://m.media-amazon.com/images/I/7118Kv5JpjL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=26, preview_image=False, image_url="https://m.media-amazon.com/images/I/91+9fxGK6+L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=26, preview_image=False, image_url="https://m.media-amazon.com/images/I/81cORRqzt0L._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=27, preview_image=True, image_url="https://m.media-amazon.com/images/I/51ScY9wKwwS._AC_.jpg", created_at=datetime.now()),
        ProductImage(product_id=27, preview_image=False, image_url="https://m.media-amazon.com/images/I/41Tk-B8ajTS._AC_.jpg", created_at=datetime.now()),
        ProductImage(product_id=27, preview_image=False, image_url="https://m.media-amazon.com/images/I/51QabaeMqqS._AC_.jpg", created_at=datetime.now()),
        ProductImage(product_id=27, preview_image=False, image_url="https://m.media-amazon.com/images/I/512hEgsDeUS._AC_.jpg", created_at=datetime.now()),
        ProductImage(product_id=27, preview_image=False, image_url="https://m.media-amazon.com/images/I/615tEu8SC4L._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=28, preview_image=True, image_url="https://m.media-amazon.com/images/I/71dB-sL7duL._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=28, preview_image=False, image_url="https://m.media-amazon.com/images/I/71zndGKtvGL._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=28, preview_image=False, image_url="https://m.media-amazon.com/images/I/61QX8U7m0XL._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=28, preview_image=False, image_url="https://m.media-amazon.com/images/I/61VENpH6eTL._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=28, preview_image=False, image_url="https://m.media-amazon.com/images/I/61JgoD+zj2L._AC_SY879_.jpg", created_at=datetime.now()),

        ProductImage(product_id=29, preview_image=True, image_url="https://m.media-amazon.com/images/I/61eTNgx5NEL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=29, preview_image=False, image_url="https://m.media-amazon.com/images/I/81kl8e7r6iL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=29, preview_image=False, image_url="https://m.media-amazon.com/images/I/71R4gNYNssL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=29, preview_image=False, image_url="https://m.media-amazon.com/images/I/81jIAjsx3zL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=29, preview_image=False, image_url="https://m.media-amazon.com/images/I/71oz9p5geAL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=30, preview_image=True, image_url="https://m.media-amazon.com/images/I/71qWPUqP37L.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=30, preview_image=False, image_url="https://m.media-amazon.com/images/I/71qawXSsJ2L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=30, preview_image=False, image_url="https://m.media-amazon.com/images/I/81N0gkgJxqL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=30, preview_image=False, image_url="https://m.media-amazon.com/images/I/71QrlyOTdjL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=30, preview_image=False, image_url="https://m.media-amazon.com/images/I/71XgB3eThwL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=31, preview_image=True, image_url="https://m.media-amazon.com/images/I/41klYXMxBhL._SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=31, preview_image=False, image_url="https://m.media-amazon.com/images/I/91IWALyvhXL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=31, preview_image=False, image_url="https://m.media-amazon.com/images/I/41-oGH9UNPL.jpg", created_at=datetime.now()),
        ProductImage(product_id=31, preview_image=False, image_url="https://m.media-amazon.com/images/I/51eSHs6-+9L._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=31, preview_image=False, image_url="https://m.media-amazon.com/images/I/41J3B+I8xRL.jpg", created_at=datetime.now()),

        ProductImage(product_id=32, preview_image=True, image_url="https://m.media-amazon.com/images/I/6130htuIPaL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=32, preview_image=False, image_url="https://m.media-amazon.com/images/I/715thdafkYL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=32, preview_image=False, image_url="https://m.media-amazon.com/images/I/71nMnOO6h7L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=32, preview_image=False, image_url="https://m.media-amazon.com/images/I/91uYyycwzZL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=32, preview_image=False, image_url="https://m.media-amazon.com/images/I/81fjYPrcVTL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=33, preview_image=True, image_url="https://m.media-amazon.com/images/I/81+G-jooxjL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=33, preview_image=False, image_url="https://m.media-amazon.com/images/I/81WbikpI78L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=33, preview_image=False, image_url="https://m.media-amazon.com/images/I/81ngH4OTLHL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=33, preview_image=False, image_url="https://m.media-amazon.com/images/I/81duxnCIRNL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=33, preview_image=False, image_url="https://m.media-amazon.com/images/I/71RxT8mBJ5L._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=34, preview_image=True, image_url="https://m.media-amazon.com/images/I/81LDwWwJ+AL._AC_SY300_SX300_.jpg", created_at=datetime.now()),
        ProductImage(product_id=34, preview_image=False, image_url="https://m.media-amazon.com/images/I/81bub7icEZL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=34, preview_image=False, image_url="https://m.media-amazon.com/images/I/81G6FeEJc3L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=34, preview_image=False, image_url="https://m.media-amazon.com/images/I/81QnhU+lkeL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=34, preview_image=False, image_url="https://m.media-amazon.com/images/I/81A0PxnAQwL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=35, preview_image=True, image_url="https://m.media-amazon.com/images/I/71qUSHA38EL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=35, preview_image=False, image_url="https://m.media-amazon.com/images/I/712z0dH+SvL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=35, preview_image=False, image_url="https://m.media-amazon.com/images/I/81tVPWX8ZrL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=35, preview_image=False, image_url="https://m.media-amazon.com/images/I/81oCHsC6CiL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=35, preview_image=False, image_url="https://m.media-amazon.com/images/I/81aJQiRgKAL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=36, preview_image=True, image_url="https://m.media-amazon.com/images/I/61m-dR8k5TL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=36, preview_image=False, image_url="https://m.media-amazon.com/images/I/71epgezA0hL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=36, preview_image=False, image_url="https://m.media-amazon.com/images/I/71wz8aBaifL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=36, preview_image=False, image_url="https://m.media-amazon.com/images/I/71qH7lqpUTL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=36, preview_image=False, image_url="https://m.media-amazon.com/images/I/714SboBDlYL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=37, preview_image=True, image_url="https://m.media-amazon.com/images/I/618q+a6xRwL._AC_SY300_SX300_.jpg", created_at=datetime.now()),
        ProductImage(product_id=37, preview_image=False, image_url="https://m.media-amazon.com/images/I/61lJ6RjIATL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=37, preview_image=False, image_url="https://m.media-amazon.com/images/I/615GOtrcdwL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=37, preview_image=False, image_url="https://m.media-amazon.com/images/I/61516WKBKqL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=37, preview_image=False, image_url="https://m.media-amazon.com/images/I/61olQh4A-LL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=38, preview_image=True, image_url="https://m.media-amazon.com/images/I/91-oXuVuF6L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=38, preview_image=False, image_url="https://m.media-amazon.com/images/I/91DNmDxBtfL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=38, preview_image=False, image_url="https://m.media-amazon.com/images/I/91nZdbF5qtL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=38, preview_image=False, image_url="https://m.media-amazon.com/images/I/91rfqlIFpZL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=38, preview_image=False, image_url="https://m.media-amazon.com/images/I/71S3jyi1+WL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=39, preview_image=True, image_url="https://m.media-amazon.com/images/I/81pKoxJLh3L.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=39, preview_image=False, image_url="https://m.media-amazon.com/images/I/91VShLs47CL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=39, preview_image=False, image_url="https://m.media-amazon.com/images/I/816tIQy7M4L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=39, preview_image=False, image_url="https://m.media-amazon.com/images/I/91Hwu6s96pL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=39, preview_image=False, image_url="https://m.media-amazon.com/images/I/91bR9dzVz9L._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=40, preview_image=True, image_url="https://m.media-amazon.com/images/I/71rN4faNvzL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=40, preview_image=False, image_url="https://m.media-amazon.com/images/I/717a4mPkEAL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=40, preview_image=False, image_url="https://m.media-amazon.com/images/I/71TALTse-YL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=40, preview_image=False, image_url="https://m.media-amazon.com/images/I/61bbognYURL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=40, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Dyw+NR77L._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=41, preview_image=True, image_url="https://m.media-amazon.com/images/I/812n58lZzZL._SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=41, preview_image=False, image_url="https://m.media-amazon.com/images/I/81SAOqLcCAS._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=41, preview_image=False, image_url="https://m.media-amazon.com/images/I/91m1r-k4xZL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=41, preview_image=False, image_url="https://m.media-amazon.com/images/I/91XyW1MtSiL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=41, preview_image=False, image_url="https://m.media-amazon.com/images/I/81jU54R0MGS._SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=42, preview_image=True, image_url="https://m.media-amazon.com/images/I/71cigKTDZOL.__AC_SY300_SX300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=42, preview_image=False, image_url="https://m.media-amazon.com/images/I/31gdkaNU+iL._AC_.jpg", created_at=datetime.now()),
        ProductImage(product_id=42, preview_image=False, image_url="https://m.media-amazon.com/images/I/81awj4ux1bL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=42, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Cy2JM-I3L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=42, preview_image=False, image_url="https://m.media-amazon.com/images/I/71oPmObkMlL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=43, preview_image=True, image_url="https://m.media-amazon.com/images/I/71KXPhJB0mL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=43, preview_image=False, image_url="https://m.media-amazon.com/images/I/71kOpm+vIJL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=43, preview_image=False, image_url="https://m.media-amazon.com/images/I/715P+SzWhcL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=43, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Ki6Bbn+oL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=43, preview_image=False, image_url="https://m.media-amazon.com/images/I/71JNvo2NfyL._AC_SY695_.jpg", created_at=datetime.now()),

        ProductImage(product_id=44, preview_image=True, image_url="https://m.media-amazon.com/images/I/81DKYayYuGL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=44, preview_image=False, image_url="https://m.media-amazon.com/images/I/619K1Yed3FL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=44, preview_image=False, image_url="https://m.media-amazon.com/images/I/71w9vb2yzFL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=44, preview_image=False, image_url="https://m.media-amazon.com/images/I/51Ram-vfsaL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=44, preview_image=False, image_url="https://m.media-amazon.com/images/I/619gWTVF2XL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=45, preview_image=True, image_url="https://m.media-amazon.com/images/I/71yys1vtuSL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=45, preview_image=False, image_url="https://m.media-amazon.com/images/I/71hi3I3H4vL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=45, preview_image=False, image_url="https://m.media-amazon.com/images/I/81DbGKr++gL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=45, preview_image=False, image_url="https://m.media-amazon.com/images/I/71Xr8ibs8uL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=45, preview_image=False, image_url="https://m.media-amazon.com/images/I/7103qf0ZYYL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=46, preview_image=True, image_url="https://m.media-amazon.com/images/I/81FOIzwPCwL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=46, preview_image=False, image_url="https://m.media-amazon.com/images/I/915O8s7WouL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=46, preview_image=False, image_url="https://m.media-amazon.com/images/I/81xVWTuOQWL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=46, preview_image=False, image_url="https://m.media-amazon.com/images/I/91COjeolMRL._SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=46, preview_image=False, image_url="https://m.media-amazon.com/images/I/81w6LvVOC+L._SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=47, preview_image=True, image_url="https://m.media-amazon.com/images/I/81GjxVHw+6L._AC_SY300_SX300_.jpg", created_at=datetime.now()),
        ProductImage(product_id=47, preview_image=False, image_url="https://m.media-amazon.com/images/I/81KM+Tvov+L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=47, preview_image=False, image_url="https://m.media-amazon.com/images/I/81pV5S05kUL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=47, preview_image=False, image_url="https://m.media-amazon.com/images/I/71jMJTXtWRL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=47, preview_image=False, image_url="https://m.media-amazon.com/images/I/71TXpt9K2DL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=48, preview_image=True, image_url="https://m.media-amazon.com/images/I/81TYQ2qrsdL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=48, preview_image=False, image_url="https://m.media-amazon.com/images/I/81tUexOaKLL._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=48, preview_image=False, image_url="https://m.media-amazon.com/images/I/81Gf10BOR7L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=48, preview_image=False, image_url="https://m.media-amazon.com/images/I/91AU-9aflZL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=48, preview_image=False, image_url="https://m.media-amazon.com/images/I/81uRUr-sGRL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=49, preview_image=True, image_url="https://m.media-amazon.com/images/I/611-trjtFKL._AC_SX679_PIbundle-3,TopRight,0,0_SH20_.jpg", created_at=datetime.now()),
        ProductImage(product_id=49, preview_image=False, image_url="https://m.media-amazon.com/images/I/810AAqR7I8L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=49, preview_image=False, image_url="https://m.media-amazon.com/images/I/917fXC+FZxL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=49, preview_image=False, image_url="https://m.media-amazon.com/images/I/71ZeBEioO6L._AC_SY879_.jpg", created_at=datetime.now()),
        ProductImage(product_id=49, preview_image=False, image_url="https://m.media-amazon.com/images/I/71el7BKo3GL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=50, preview_image=True, image_url="https://m.media-amazon.com/images/I/81ZqKepTOcL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=50, preview_image=False, image_url="https://m.media-amazon.com/images/I/81oL4QMCs9L._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=50, preview_image=False, image_url="https://m.media-amazon.com/images/I/815Z9Q07jGL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=50, preview_image=False, image_url="https://m.media-amazon.com/images/I/71M9yCKGTzL._AC_SY695_.jpg", created_at=datetime.now()),
        ProductImage(product_id=50, preview_image=False, image_url="https://m.media-amazon.com/images/I/511P6VymorL._AC_SY695_.jpg", created_at=datetime.now()),

        ProductImage(product_id=51, preview_image=True, image_url="https://m.media-amazon.com/images/I/71SdELcY9NL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=51, preview_image=False, image_url="https://m.media-amazon.com/images/I/71bj2eQGB6L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=51, preview_image=False, image_url="https://m.media-amazon.com/images/I/81P4EV0gNzL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=51, preview_image=False, image_url="https://m.media-amazon.com/images/I/81KzTDTBj1L._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=51, preview_image=False, image_url="https://m.media-amazon.com/images/I/710XC4u19UL._AC_SX679_.jpg", created_at=datetime.now()),

        ProductImage(product_id=52, preview_image=True, image_url="https://m.media-amazon.com/images/I/51dTMkZitCL.__AC_SX300_SY300_QL70_FMwebp_.jpg", created_at=datetime.now()),
        ProductImage(product_id=52, preview_image=False, image_url="https://m.media-amazon.com/images/I/51XH3-FVnvL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=52, preview_image=False, image_url="https://m.media-amazon.com/images/I/51jq51HuRjL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=52, preview_image=False, image_url="https://m.media-amazon.com/images/I/41t6g9DzWlL._AC_SX679_.jpg", created_at=datetime.now()),
        ProductImage(product_id=52, preview_image=False, image_url="https://m.media-amazon.com/images/I/41BRWt90guL._AC_SX679_.jpg", created_at=datetime.now())
    ]
    db.session.add_all(product_images)
    db.session.commit()

def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM product_images"))
    db.session.commit()
