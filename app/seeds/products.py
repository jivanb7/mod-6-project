from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_products():
    product1 = Product(
        user_id=1,
        category="Ornaments",
        name="Angelic Snowfall Ornament",
        description="An awesome and amazing addition. This angelic ornament brings a blissful snowfall to your holiday scene with serene snowflakes and stunning details",
        price=25.67,
        stock=7,
        created_at=datetime.now()
    )
    product2 = Product(
        user_id=2,
        category="Apparel",
        name="Bellslayer Pants",
        description="Bold and beautiful, these Bellslayer pants are the perfect blend of comfort and Christmas cheer, with festive flair that jingles as you move",
        price=35.93,
        stock=2,
        created_at=datetime.now()
    )
    product3 = Product(
        user_id=3,
        category="Decor",
        name="Candlelit Village Scene",
        description="Cozy and captivating, this candlelit village scene casts a charming glow over your holiday gatherings with heartwarming winter wonder",
        price=23.25,
        stock=3,
        created_at=datetime.now()
    )
    product4 = Product(
        user_id=4,
        category="Gifts",
        name="Dreamcatcher Delight Snowglobe",
        description="Dazzling and dreamy, this snowglobe captures a delightful dance of dreams and snow, adding whimsical wonder to any winter decor",
        price=22.04,
        stock=4,
        created_at=datetime.now()
    )
    product5 = Product(
        user_id=5,
        category="Baking",
        name="Evergreen Cookie Cutters",
        description="Enjoy endless holiday excitement with these evergreen-shaped cookie cutters, adding a festive flair to your holiday baking",
        price=23.40,
        stock=5,
        created_at=datetime.now()
    )
    product6 = Product(
        user_id=6,
        category="Ornaments",
        name="Frosted Fir Cone Ornament",
        description="Festive and frosty, this fir cone ornament features fine frosted details that bring the beauty of the forest to your Christmas tree",
        price=11.12,
        stock=6,
        created_at=datetime.now()
    )
    product7 = Product(
        user_id=7,
        category="Apparel",
        name="Glistening Snowflake Sweater",
        description="Gorgeous and glittering, this sweater sparkles with glistening snowflake designs, perfect for glamorous holiday gatherings",
        price=26.53,
        stock=7,
        created_at=datetime.now()
    )
    product8 = Product(
        user_id=8,
        category="Decor",
        name="Holly Berry Centerpiece",
        description="Handcrafted and hearty, this holly berry centerpiece brightens your home with holiday hues and the happiness of nature",
        price=31.65,
        stock=8,
        created_at=datetime.now()
    )
    product9 = Product(
        user_id=9,
        category="Gifts",
        name="Icy Polar Bear Figurine",
        description="Intricately designed and icy cool, this polar bear figurine adds an irresistible touch of the Arctic to your holiday decor",
        price=35.88,
        stock=9,
        created_at=datetime.now()
    )
    product10 = Product(
        user_id=10,
        category="Baking",
        name="Jolly Gingerbread House Kit",
        description="Joyful and jolly, this gingerbread house kit lets you create a delicious display with your family, full of holiday happiness",
        price=4.54,
        stock=10,
        created_at=datetime.now()
    )
    product11 = Product(
        user_id=11,
        category="Ornaments",
        name="Keepsake Knit Snowman",
        description="Knit with kindness and care, this snowman brings a cozy charm to your Christmas decor, perfect for holiday memories",
        price=35.43,
        stock=11,
        created_at=datetime.now()
    )
    product12 = Product(
        user_id=12,
        category="Apparel",
        name="Lake Tahoe Sweater",
        description="Luxe and layered, the Lake Tahoe sweater captures the landscape of snowy mountains and lovely winter warmth",
        price=8.83,
        stock=12,
        created_at=datetime.now()
    )
    product13 = Product(
        user_id=13,
        category="Decor",
        name="Mistletoe Magic Garland",
        description="Marvelous and magical, this mistletoe garland spreads merriment and seasonal sparkle across your holiday home",
        price=19.52,
        stock=13,
        created_at=datetime.now()
    )
    product14 = Product(
        user_id=14,
        category="Gifts",
        name="Nutcracker Set",
        description="Nostalgic and noble, this nutcracker set adds a touch of timeless tradition to your holiday with finely crafted details",
        price=39.98,
        stock=14,
        created_at=datetime.now()
    )
    product15 = Product(
        user_id=15,
        category="Baking",
        name="Old-Fashioned Peppermint Bark Kit",
        description="Outstandingly old-fashioned, this peppermint bark kit brings a nostalgic nod to traditional holiday treats",
        price=19.49,
        stock=15,
        created_at=datetime.now()
    )
    product16 = Product(
        user_id=16,
        category="Ornaments",
        name="Pine Cone Charm Ornament",
        description="Perfectly pine-scented and picturesque, this ornament adds a peaceful, natural charm to your festive tree",
        price=22.84,
        stock=16,
        created_at=datetime.now()
    )
    product17 = Product(
        user_id=17,
        category="Apparel",
        name="Quirky Elf Cap",
        description="Quintessentially quirky, this elf cap brings quality cheer to every holiday outfit with a playful bell and festive feel",
        price=25.44,
        stock=17,
        created_at=datetime.now()
    )
    product18 = Product(
        user_id=18,
        category="Decor",
        name="Rustic Pine Cone Wreath",
        description="Rustic and refined, this pine cone wreath welcomes winter with rich, natural textures and radiant holiday accents",
        price=24.76,
        stock=18,
        created_at=datetime.now()
    )
    product19 = Product(
        user_id=19,
        category="Gifts",
        name="Snowflake Suncatcher",
        description="Sparkling and special, this snowflake suncatcher captures sunlight and spreads a shimmering sparkle across your space",
        price=26.67,
        stock=19,
        created_at=datetime.now()
    )
    product20 = Product(
        user_id=20,
        category="Baking",
        name="Twinkling Star Sprinkle Mix",
        description="Tantalizing and twinkling, this sprinkle mix adds a touch of tasty holiday magic to your treats with each festive star",
        price=37.16,
        stock=20,
        created_at=datetime.now()
    )
    product21 = Product(
        user_id=21,
        category="Ornaments",
        name="Ugly Sweater Cheer Ornament",
        description="Unique and unforgettable, this ugly sweater ornament brings a universal cheer with its vibrant colors and quirky design",
        price=4.71,
        stock=21,
        created_at=datetime.now()
    )
    product22 = Product(
        user_id=22,
        category="Apparel",
        name="Velvet Snowfall Cloak",
        description="Velvety and vibrant, this snowfall cloak wraps you in warmth with luxurious layers, ideal for chilly holiday outings",
        price=29.46,
        stock=22,
        created_at=datetime.now()
    )
    product23 = Product(
        user_id=23,
        category="Decor",
        name="Winter Wonderland Wall Art",
        description="Whimsical and wondrous, this wall art transforms any space into a winter wonderland with enchanting seasonal scenes",
        price=34.06,
        stock=23,
        created_at=datetime.now()
    )
    product24 = Product(
        user_id=24,
        category="Gifts",
        name="Xmas Tree Charm Bracelet",
        description="Xquisite and xtra special, this Xmas tree charm bracelet adds a festive touch to your holiday attire",
        price=25.95,
        stock=24,
        created_at=datetime.now()
    )
    product25 = Product(
        user_id=25,
        category="Baking",
        name="Yule Log Baking Kit",
        description="Yummy and youthful, this yule log baking kit is a delicious activity for family fun, creating seasonal sweets to share",
        price=18.79,
        stock=25,
        created_at=datetime.now()
    )
    product26 = Product(
        user_id=26,
        category="Ornaments",
        name="Zesty Candy Cane Ornament",
        description="Zesty and zippy, this candy cane ornament brings a sweet, vibrant touch to your holiday tree decor",
        price=4.90,
        stock=26,
        created_at=datetime.now()
    )
    product27 = Product(
        user_id=1,
        category="Ornaments",
        name="Aurora’s Glass Wings",
        description="A delicate and dazzling display, Aurora’s Glass Wings ornament catches the light and shines with ethereal beauty on your tree",
        price=39.92,
        stock=27,
        created_at=datetime.now()
    )
    product28 = Product(
        user_id=2,
        category="Apparel",
        name="Blizzard Scarf",
        description="Brave the winter chill with the Blizzard Scarf, a cozy, comfortable essential with frosty colors that capture the spirit of snowfall",
        price=32.20,
        stock=28,
        created_at=datetime.now()
    )
    product29 = Product(
        user_id=3,
        category="Decor",
        name="Crystal Snowflake Charm",
        description="Charming and crystalline, this snowflake charm brings the beauty of icy wonder to your holiday decor with intricate frosted details",
        price=8.03,
        stock=29,
        created_at=datetime.now()
    )
    product30 = Product(
        user_id=4,
        category="Gifts",
        name="Dancing Star Snowglobe",
        description="Delightfully dazzling, this Dancing Star Snowglobe creates a magical scene of swirling stars and glitter, perfect for a holiday mantel",
        price=33.08,
        stock=30,
        created_at=datetime.now()
    )
    product31 = Product(
        user_id=5,
        category="Baking",
        name="Enchanted Gingerbread Mix",
        description="Enchant your holiday kitchen with this gingerbread mix, a perfect blend of spices for creating cookies full of holiday cheer",
        price=28.26,
        stock=31,
        created_at=datetime.now()
    )
    product32 = Product(
        user_id=6,
        category="Ornaments",
        name="Festive Flurry Bauble",
        description="Festive and fun, the Festive Flurry Bauble adds a touch of whimsy to your tree with its playful design and wintery color palette",
        price=7.82,
        stock=32,
        created_at=datetime.now()
    )
    product33 = Product(
        user_id=7,
        category="Apparel",
        name="Grandmas Socks",
        description="Generous and warm, Grandma’s Socks bring you back to classic holiday comfort with cozy wool and timeless design",
        price=23.95,
        stock=33,
        created_at=datetime.now()
    )
    product34 = Product(
        user_id=8,
        category="Decor",
        name="Heavenly Winter Lantern",
        description="Heavenly and heartwarming, this winter lantern illuminates your home with a soft, comforting glow for those chilly nights",
        price=27.76,
        stock=34,
        created_at=datetime.now()
    )
    product35 = Product(
        user_id=9,
        category="Gifts",
        name="Illuminated Snowman Keepsake",
        description="Intricate and inspiring, this snowman keepsake is illuminated from within, bringing a gentle glow to any holiday decor",
        price=38.57,
        stock=35,
        created_at=datetime.now()
    )
    product36 = Product(
        user_id=10,
        category="Baking",
        name="Joyful Cookie Cutter Collection",
        description="Joyful and jubilant, this cookie cutter collection offers festive shapes to create holiday treats for family and friends",
        price=32.56,
        stock=36,
        created_at=datetime.now()
    )
    product37 = Product(
        user_id=11,
        category="Ornaments",
        name="Keepsake Knit Angel",
        description="Kindhearted and crafted with care, this knit angel ornament is a keepsake that brings a touch of peace to your tree",
        price=9.93,
        stock=37,
        created_at=datetime.now()
    )
    product38 = Product(
        user_id=12,
        category="Apparel",
        name="Lodge Lovers Flannel",
        description="Lounge in style with the Lodge Lovers Flannel, a soft and cozy favorite that’s perfect for fireside evenings and winter warmth",
        price=30.73,
        stock=38,
        created_at=datetime.now()
    )
    product39 = Product(
        user_id=13,
        category="Decor",
        name="Merry Music Lights",
        description="Musical and merry, these lights bring a festive sound and sparkle to your home, combining cheer with every twinkle",
        price=36.10,
        stock=39,
        created_at=datetime.now()
    )
    product40 = Product(
        user_id=14,
        category="Gifts",
        name="Northern Lights Candle",
        description="Northern Lights Candle adds a touch of the Arctic with its blend of wintery scents and softly glowing colors",
        price=15.65,
        stock=40,
        created_at=datetime.now()
    )
    product41 = Product(
        user_id=15,
        category="Baking",
        name="Old-Fashioned Sugar Cookie Kit",
        description="Old-fashioned and flavorful, this sugar cookie kit lets you bake classic holiday treats that taste just like home",
        price=26.55,
        stock=41,
        created_at=datetime.now()
    )
    product42 = Product(
        user_id=16,
        category="Ornaments",
        name="Polar Bear Bauble",
        description="Playful and pure, this Polar Bear Bauble brings arctic charm to your tree with a frosty finish and delightful details",
        price=29.45,
        stock=42,
        created_at=datetime.now()
    )
    product43 = Product(
        user_id=17,
        category="Apparel",
        name="Quirky Elf Shoes",
        description="Quirky and whimsical, these elf shoes add a dash of holiday magic to your attire, with a playful curve and festive jingles",
        price=16.73,
        stock=43,
        created_at=datetime.now()
    )
    product44 = Product(
        user_id=18,
        category="Decor",
        name="Reindeer Forest Figurines",
        description="Rustic and realistic, Reindeer Forest Figurines capture the essence of nature and make a charming addition to your decor",
        price=36.29,
        stock=44,
        created_at=datetime.now()
    )
    product45 = Product(
        user_id=19,
        category="Gifts",
        name="Seras Snowglobe",
        description="Seras Snowglobe sparkles with soft snow and warm scenes, a serene decoration that brings wintery bliss to any space",
        price=6.27,
        stock=45,
        created_at=datetime.now()
    )
    product46 = Product(
        user_id=20,
        category="Baking",
        name="Tinsel Dusting Sugar",
        description="Tiny and twinkling, this Tinsel Dusting Sugar adds festive sparkle to all your treats, with each crystal capturing holiday light",
        price=20.26,
        stock=46,
        created_at=datetime.now()
    )
    product47 = Product(
        user_id=21,
        category="Ornaments",
        name="Under the Mistletoe Charm",
        description="Under the Mistletoe Charm is a subtle yet sweet accessory that brings festive romance with a touch of winter magic",
        price=27.96,
        stock=47,
        created_at=datetime.now()
    )
    product48 = Product(
        user_id=22,
        category="Apparel",
        name="Vintage Reindeer Vest",
        description="Vintage and vibrant, the Reindeer Vest combines classic holiday patterns with a modern fit for a timeless seasonal style",
        price=15.96,
        stock=48,
        created_at=datetime.now()
    )
    product49 = Product(
        user_id=23,
        category="Decor",
        name="Warm Glow Candle Trio",
        description="Warm and welcoming, the Glow Candle Trio brings soft hues of red, green, and white to any space for festive ambiance",
        price=26.94,
        stock=49,
        created_at=datetime.now()
    )
    product50 = Product(
        user_id=24,
        category="Gifts",
        name="Xmas Tree Charm Necklace",
        description="Xtra special, this Xmas Tree Charm Necklace captures holiday spirit in every miniature tree, making a perfect gift for loved ones",
        price=8.70,
        stock=50,
        created_at=datetime.now()
    )
    product51 = Product(
        user_id=25,
        category="Baking",
        name="Yuletide Cupcake Toppers",
        description="Yummy and unique, the Yuletide Cupcake Toppers add a festive finish to baked goods, perfect for parties and gatherings",
        price=6.11,
        stock=51,
        created_at=datetime.now()
    )
    product52 = Product(
        user_id=26,
        category="Ornaments",
        name="Zesty Eggnog Ornament",
        description="Zesty and delightful, this Eggnog Ornament brings seasonal charm with a bright, cheerful design for your holiday decor",
        price=22.88,
        stock=52,
        created_at=datetime.now()
    )

    db.session.bulk_save_objects([
        product1, product2, product3, product4, product5, product6, product7, product8, product9, product10,
        product11, product12, product13, product14, product15, product16, product17, product18, product19, product20,
        product21, product22, product23, product24, product25, product26, product27, product28, product29, product30,
        product31, product32, product33, product34, product35, product36, product37, product38, product39, product40,
        product41, product42, product43, product44, product45, product46, product47, product48, product49, product50,
        product51, product52
    ])
    db.session.commit()

def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
    db.session.commit()
