from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_reviews():
    reviews = [
        Review(
            user_id=19,
            product_id=1,
            comment="Absolutely beautiful. It adds the perfect amount of sparkle to the tree, catching the light in the most magical way. Great quality materials that feel well crafted.",
            item_quality=5,
            shipping=4,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=18,
            product_id=1,
            comment="Loved this ornament. The snowflake design feels detailed and intricate, very elegant. Shipping was quick, and it arrived in excellent condition. A must-have.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=12,
            product_id=1,
            comment="High-quality ornament that adds a classic wintry touch. Looks fantastic on my tree, and the craftsmanship is amazing. Customer service also very friendly.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=1,
            product_id=2,
            comment="Perfect fit and incredible comfort. The fabric feels very high-quality, and the design is both stylish and practical. Definitely worth every penny. Very satisfied.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=3,
            product_id=3,
            comment="Brings a heartwarming nostalgic feel to the holidays. The details in the tiny buildings are stunning. I love how it lights up in the evenings and creates ambiance.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=8,
            product_id=3,
            comment="The village scene is simply enchanting. Every piece is made with care, and the lighting really adds warmth. It brings magic to my living room during the holidays.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=14,
            product_id=3,
            comment="Beautifully made. Love the glowing windows. It captures the essence of winter perfectly, and all my guests comment on it. It is now a centerpiece of my decor.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=12,
            product_id=3,
            comment="Lovely addition to our decorations. Details could be a bit more refined, but overall it brings a delightful old-world charm that fills the room with warmth.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=25,
            product_id=4,
            comment="Gorgeous snowglobe with a mesmerizing snowfall effect. The quality is impeccable, and it looks fantastic with my other holiday decor. Shipping was fast as well.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=17,
            product_id=5,
            comment="Perfect for holiday baking. The cutters are sturdy, and the shapes come out beautifully. My family enjoyed using them for cookies. Very festive and good quality.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=14,
            product_id=6,
            comment="Very beautiful ornament. The frosted effect adds a perfect rustic touch to my tree. High-quality craftsmanship. It arrived well packaged and looks wonderful.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=20,
            product_id=6,
            comment="Love how this ornament looks on the tree. It has such an authentic, outdoorsy feel. The frosted tips make it look almost real. Highly recommend for rustic decor.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=1,
            product_id=6,
            comment="Cute ornament, although it could be a bit more vibrant. Still adds a lovely woodland touch to our holiday tree. Quality is good, and shipping was quick.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=13,
            product_id=6,
            comment="The frosted details are lovely and really add that wintery vibe. Quality is good, though it arrived a day late. Still very happy with this ornament.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=5,
            product_id=7,
            comment="Soft, cozy, and perfect for winter! The snowflake pattern looks very elegant. I love wearing it on chilly evenings. Highly recommend it for a festive winter look.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=4,
            product_id=7,
            comment="One of the best sweaters I own. Keeps me warm, fits perfectly, and the snowflake design stands out. Very soft material, feels luxurious, and great for the holidays.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=11,
            product_id=8,
            comment="Nice centerpiece but could be more vibrant. Some of the berries seem dull. Good quality otherwise, and it complements my table setting well.",
            item_quality=3,
            shipping=5,
            customer_service=5,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=2,
            product_id=8,
            comment="The berries are beautiful, but I was disappointed with the packaging. Some pieces were loose when it arrived. Quality is good but did not meet my full expectations.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=10,
            product_id=9,
            comment="Cute polar bear figurine, but slightly smaller than I expected. Good quality overall, but customer service could improve in answering queries.",
            item_quality=4,
            shipping=5,
            customer_service=3,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=18,
            product_id=9,
            comment="Adorable bear figurine with a frosty look. It fits perfectly with my holiday decor. Shipping was fast, and it arrived safely without any damage. Very happy.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=16,
            product_id=10,
            comment="Fun family activity, though it was a bit difficult to assemble. The gingerbread is tasty, and the decorations are adorable. Overall, a great holiday experience.",
            item_quality=4,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=4,
            product_id=11,
            comment="Absolutely love this little snowman. The knitted texture gives it such a cozy homemade feel. It looks great on my tree and adds to the holiday charm.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=21,
            product_id=12,
            comment="Comfortable, warm, and fits well. The wintery design is beautiful without being overwhelming. Perfect for casual outings in the cold. Will be wearing it a lot.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=26,
            product_id=12,
            comment="This sweater exceeded my expectations. It is incredibly soft, warm, and has a great festive design that is subtle yet stylish. Customer service was also excellent.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=25,
            product_id=13,
            comment="This garland is stunning! The mistletoe leaves look incredibly realistic, and it adds such a lovely holiday touch to my decor. Really well made and a perfect length.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=24,
            product_id=15,
            comment="Delicious peppermint bark, super easy to make. The instructions were clear, and the result was perfect. Great for holiday gatherings and makes a lovely treat.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=2,
            product_id=17,
            comment="Fun and whimsical. The elf cap was a great addition to my holiday party outfit. It is well made and comfortable to wear. Added lots of laughs and cheer.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=5,
            product_id=18,
            comment="Beautiful wreath, perfect for my front door. The rustic design looks great, and the pine cones add a lovely natural touch. Quality is excellent, though shipping was a bit slow.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=11,
            product_id=18,
            comment="Love this wreath! It is the perfect addition to our holiday decor. The pine cones and frosted touches look beautiful, and it arrived in great condition.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=16,
            product_id=18,
            comment="Excellent quality wreath. The natural pine cones make it feel authentic, and it is the perfect size for my door. Adds a welcoming holiday touch.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=3,
            product_id=19,
            comment="Cute suncatcher, but not as impressive as I thought. It does catch light beautifully though. Adds a subtle sparkle to my window. Overall, nice but not outstanding.",
            item_quality=3,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=8,
            product_id=19,
            comment="Very delicate and pretty. The suncatcher arrived slightly late, but the piece itself looks wonderful hanging near my window. It adds a soft wintery glow.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=4,
            product_id=20,
            comment="The stars are adorable, but the mix was not well packaged. Some sprinkles had spilled. They do look festive though, and my kids enjoyed decorating with them.",
            item_quality=5,
            shipping=5,
            customer_service=3,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=2,
            product_id=22,
            comment="This cloak is luxurious and warm. The velvet fabric feels rich, and it is perfect for holiday events. The length and fit are just right. Great addition to my wardrobe.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=19,
            product_id=22,
            comment="Lovely cloak, though it could be a little more fitted. The fabric is beautiful, and it adds a magical touch to my winter attire. Very happy with my purchase.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=6,
            product_id=22,
            comment="The velvet cloak is cozy and elegant. It was slightly delayed in shipping, but overall I am pleased with the quality. It really stands out at gatherings.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=25,
            product_id=22,
            comment="Rich, warm fabric with a fantastic design. This cloak is perfect for winter and makes any outfit feel festive. Great quality, though customer service could be better.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=1,
            product_id=23,
            comment="Nice piece of artwork, though I wish the colors were a bit more vibrant. It does create a serene atmosphere in my living room. Overall a good addition to my decor.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=12,
            product_id=23,
            comment="Pretty wintery scene, but arrived a bit scuffed. It still looks good hanging on my wall. The design is calming and brings a seasonal touch to the room.",
            item_quality=3,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=23,
            product_id=24,
            comment="Cute charm bracelet, though I wish the charms were slightly larger. It still adds a lovely festive touch to my holiday outfit. Good for a casual accessory.",
            item_quality=5,
            shipping=3,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=8,
            product_id=24,
            comment="The bracelet is festive, but the packaging could have been better. One charm was loose when it arrived. Still cute, but could be better quality control.",
            item_quality=5,
            shipping=5,
            customer_service=3,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=23,
            product_id=24,
            comment="This bracelet is perfect for the holiday season. The charms are adorable, and the quality exceeded my expectations. Great accessory for festive gatherings.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=21,
            product_id=24,
            comment="I absolutely love this charm bracelet. The quality is top-notch, and the festive charms are delightful. It has been a hit at every holiday party I have attended.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=13,
            product_id=25,
            comment="The instructions were a bit confusing, but the final product tasted amazing. It was a fun baking project, and everyone enjoyed the yule log at our holiday dinner.",
            item_quality=3,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=7,
            product_id=25,
            comment="The kit is fun, but the instructions could be clearer. Also, some ingredients were missing. Customer service tried to help, but still not fully satisfied.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=8,
            product_id=26,
            comment="Cute ornament, adds a nice festive touch to my tree. Could be a bit more detailed, but overall I am happy with it. It is definitely eye-catching among the lights.",
            item_quality=4,
            shipping=5,
            customer_service=3,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=20,
            product_id=27,
            comment="Lovely piece. The wings are delicate and elegant, though the glass feels a bit fragile. Shipping was smooth, and it arrived safely. Adds a unique touch to my decor.",
            item_quality=4,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=5,
            product_id=27,
            comment="Stunning wings. The craftsmanship is wonderful, but they are more delicate than I expected. Be careful when handling. Still, they are an elegant addition to my room.",
            item_quality=5,
            shipping=4,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=3,
            product_id=28,
            comment="Soft and warm, this scarf is perfect for winter. The festive colors make it a lovely holiday accessory, and it feels luxurious around the neck. Very pleased with it.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=7,
            product_id=28,
            comment="Excellent quality. This scarf is both cozy and stylish, making it perfect for winter walks. The fabric is soft, and I love the holiday pattern. Could not ask for more.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=14,
            product_id=28,
            comment="Love this scarf. It is incredibly soft, warm, and has a wonderful festive design. The quality is superb, and it keeps me cozy throughout the chilly season.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=17,
            product_id=29,
            comment="Beautiful and intricate snowflake charm. It adds a lovely touch to my holiday jewelry collection. Well made, with a delicate sparkle that stands out.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=22,
            product_id=29,
            comment="The snowflake charm is exquisite. It sparkles beautifully in the light, and the craftsmanship is of excellent quality. Looks stunning on my bracelet.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=22,
            product_id=30,
            comment="This snowglobe is absolutely stunning. The dancing stars inside create a magical effect, and it has become a centerpiece in my holiday decorations. High quality.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=1,
            product_id=32,
            comment="Wonderful bauble with a gorgeous festive design. It looks amazing on my tree and has become one of my favorites. Excellent quality, and shipping was very prompt.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=15,
            product_id=33,
            comment="These socks are so warm and cozy. Perfect for lounging around the house during the holidays. They have a lovely traditional pattern and feel high quality.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
         Review(
            user_id=17,
            product_id=34,
            comment="Beautiful lantern with a soft, warm glow. I love how it creates a cozy holiday ambiance. The only downside is that the glass could be a bit sturdier.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=11,
            product_id=34,
            comment="Very pleased with this lantern. The light it gives off is perfect for creating a cozy winter atmosphere. It arrived in great condition, and the design is charming.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
         Review(
            user_id=6,
            product_id=35,
            comment="Cute snowman with a lovely warm glow. It looks adorable among my other decorations. Quality is great, though I would have liked a bit more brightness.",
            item_quality=5,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=20,
            product_id=36,
            comment="Fantastic cookie cutters with great holiday shapes. Very sturdy and easy to use. The cookies came out perfectly, and the kids loved using them to bake.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=6,
            product_id=36,
            comment="Not very happy with this set. Some shapes are not cut well, and it is difficult to get the dough out. The kids got frustrated, and it did not meet our expectations.",
            item_quality=3,
            shipping=5,
            customer_service=5,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=9,
            product_id=37,
            comment="Lovely little angel ornament, though smaller than I expected. It has a beautiful knit design and looks charming on my tree. Could be slightly bigger.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=18,
            product_id=38,
            comment="Cozy flannel with a great winter design. Very comfortable to wear around the house. However, shipping took longer than expected, but the product is worth it.",
            item_quality=5,
            shipping=5,
            customer_service=3,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=7,
            product_id=39,
            comment="Fun addition to my holiday decor. The lights are bright, and the music adds a cheerful touch. Could be a bit louder, but overall I am happy with the purchase.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=5,
            product_id=40,
            comment="The scent of this candle is fantastic. It fills my entire room with a holiday fragrance. The soft glow adds a calming atmosphere. Would recommend for winter nights.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=2,
            product_id=41,
            comment="Instructions were hard to follow, and the mix was a bit dry. The final cookies tasted okay but not great. Packaging was decent, and shipping was quick.",
            item_quality=3,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=15,
            product_id=41,
            comment="Fun to bake, but the instructions were not clear. The final result was tasty though. It could be better organized. Customer service tried to assist, which was nice.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=19,
            product_id=42,
            comment="Cute bauble, but not as well crafted as I hoped. The paintwork could be improved. Looks nice on the tree, but overall, I am slightly disappointed with the quality.",
            item_quality=5,
            shipping=5,
            customer_service=3,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=7,
            product_id=43,
            comment="These elf shoes are so much fun! They were a hit at my holiday party. Comfortable, easy to wear, and they added lots of festive spirit. Really well made.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=12,
            product_id=45,
            comment="Beautiful snowglobe with intricate details. The snowy scene inside is peaceful and brings a lot of joy. Looks amazing with my other holiday decorations.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=14,
            product_id=46,
            comment="This tinsel sugar is a perfect finishing touch for my holiday treats. It adds just the right amount of sparkle and makes desserts look beautiful. Highly recommend.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=26,
            product_id=48,
            comment="Love the vintage design of this vest. It fits comfortably, and the reindeer pattern is festive and nostalgic. The quality is good, and it is perfect for winter.",
            item_quality=4,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=13,
            product_id=49,
            comment="The candles give off a lovely warm glow. The scent is pleasant but could be a bit stronger. Overall, a great addition to my holiday decor. Looks beautiful when lit.",
            item_quality=5,
            shipping=4,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=19,
            product_id=49,
            comment="Nice set of candles, though they arrived a little damaged. Customer service was helpful, but the packaging could have been better. Still, they smell good and look nice.",
            item_quality=3,
            shipping=5,
            customer_service=4,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=3,
            product_id=50,
            comment="Necklace looks cute, but the chain feels a bit flimsy. The charm is festive, but it does not seem very durable. Could improve the overall quality for the price.",
            item_quality=5,
            shipping=3,
            customer_service=5,
            recommended=False,
            created_at=datetime.now()
        ),
        Review(
            user_id=15,
            product_id=50,
            comment="Adorable charm necklace that adds a festive touch to my winter outfits. The quality is decent, though customer service could have been more responsive.",
            item_quality=5,
            shipping=5,
            customer_service=3,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=4,
            product_id=51,
            comment="These cupcake toppers are adorable! They made our holiday desserts look festive and fun. Very easy to use and added that extra holiday cheer to our party table.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=15,
            product_id=52,
            comment="Cheerful ornament that brings a lot of fun to my tree. The eggnog design is unique, and it stands out among the other decorations. Excellent quality craftsmanship.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=28,
            product_id=52,
            comment="This eggnog ornament is adorable and festive. It looks fantastic on my tree, and the colors are vibrant. The quality is great, and it adds a playful touch.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        ),
        Review(
            user_id=28,
            product_id=52,
            comment="Love this ornament. It adds a pop of color to my tree, and the craftsmanship is really good. It is one of my favorite new additions this holiday season.",
            item_quality=5,
            shipping=5,
            customer_service=5,
            recommended=True,
            created_at=datetime.now()
        )
    ]

    db.session.add_all(reviews)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
    db.session.commit()
