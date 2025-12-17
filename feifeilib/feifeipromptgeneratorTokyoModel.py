import random

# --- V2.0 - Massively Expanded Keyword Categories (Tokyo Edition) ---

# Category 1: The Vibe & Personality
vibes = [
    "Alluring", "Captivating", "Charismatic", "Dynamic", "Electric", "Enigmatic", 
    "Magnetic", "Hypnotic", "A whole vibe", "Ethereal", "Unforgettable", "Mysterious", 
    "Radiant", "Confident", "Serene", "Cool", "Effortless", "Poised", "Sophisticated", "Glamorous"
]
menaces = [
    "Fierce", "Dangerous", "Edgy", "Rebellious", "Provocative", "Intense", "Unapologetic", 
    "Audacious", "Smoldering", "Defiant", "Untamable", "Wild", "Formidable", "Menacing", 
    "Seductive", "Commanding", "Dominant", "Lethal", "Icy", "Aloof"
]
firecrackers = [
    "Energetic", "Explosive", "Fiery", "Spirited", "Spunky", "Vibrant", "Volatile", 
    "Bold", "Feisty", "Vivacious", "Passionate", "Dynamic", "Impulsive", "Unpredictable", 
    "Charismatic", "Bubbly", "Lively", "Radiant", "Dazzling", "Playful"
]
dime_pieces = [
    "Stunning", "Gorgeous", "Flawless", "Exquisite", "Breathtaking", "Divine", "Head-turner", 
    "Showstopper", "A perfect 10", "Angelic", "God-tier visuals", "Otherworldly", "Ethereal beauty", 
    "Mesmerizing", "Picture-perfect", "Drop-dead gorgeous", "Irresistible", "Jaw-dropping", "Flawless", "Aphrodite"
]
bricks = [
    "Powerful", "Strong", "Athletic", "Sculpted", "Toned", "Solid", "Statuesque", "Well-built", 
    "Formidable physique", "Lean muscle", "Defined", "Fit", "Healthy", "Powerful stance", 
    "Confident posture", "Imposing", "Resilient", "Robust", "Amazonian", "Unbreakable"
]

# Clothing, Accessories & Swimwear (Tokyo Style)

clothing = [
    "an oversized blazer paired with wide-leg trousers",
    "a minimalist linen dress from a boutique in Daikanyama",
    "a layered outfit with a mix of vintage and designer pieces from Harajuku",
    "a sleek, all-black Yohji Yamamoto-inspired ensemble",
    "a graphic tee from a Shibuya 109 brand with a plaid skirt",
    "a modern, deconstructed kimono jacket over a simple top",
    "a Gothic Lolita dress with intricate lace and ribbons",
    "a techwear jacket with multiple straps and pockets",
    "a vintage sukajan (souvenir jacket) with detailed embroidery",
    "a pair of baggy, wide-leg hakama-style pants",
    "a 'Mori Kei' (forest style) outfit with earthy tones and natural fabrics",
    "a vibrant Decora Kei outfit covered in colorful accessories",
    "a chic, tailored coat from a Ginza department store",
    "a punk-inspired outfit with ripped fabrics and safety pins",
    "a pair of high-waisted, pleated trousers with a tucked-in blouse",
    "a playful 'Gyaru' style outfit with a mini-skirt and platform boots",
    "an oversized hoodie from a popular Japanese streetwear brand",
    "a simple, elegant Issey Miyake Pleats Please dress",
    "a layered look featuring a mesh top under a band t-shirt",
    "a vintage kimono worn as a stylish outer layer",
    "a schoolgirl-inspired uniform with a modern twist",
    "a sophisticated trench coat perfect for walking in Marunouchi",
    "a pair of expertly tailored, straight-leg raw denim jeans",
    "a cozy, oversized sweater from a Shimokitazawa thrift store",
    "a futuristic, cyberpunk-inspired vinyl outfit",
    "a simple Uniqlo t-shirt paired with avant-garde bottoms",
    "a flowy, patterned maxi skirt with a simple camisole",
    "a 'Visual Kei' inspired outfit with dramatic silhouettes and dark colors",
    "a light, airy yukata worn for a summer festival",
    "a sporty-chic look with a track jacket and a pleated skirt",
    # --- Bikini Additions (Maintained) ---
    "a classic triangle string bikini in a solid bright color",
    "a high-waisted retro bikini with a polka dot print",
    "a strapless bandeau bikini top with matching bottoms",
    "a sporty, racerback bikini designed for activity",
    "a crochet, bohemian-style bikini",
    "a one-shoulder bikini with an asymmetrical design",
    "an animal print (leopard or snake) bikini",
    "a bikini with ruffled straps and edges",
    "a metallic, high-shine bikini for a glamorous look",
    "a thong bikini bottom with minimal coverage",
    "a cut-out one-piece that resembles a bikini",
    "a halter top bikini that ties around the neck",
    "a neon-colored bikini that stands out",
    "a floral print bikini with a tropical vibe",
    "a ribbed-fabric bikini for added texture",
    "a tie-front bikini top with a small knot",
    "a color-block bikini with contrasting panels",
    "a longline bikini top that extends further down the torso",
    "a micro-bikini with extremely small fabric panels",
    "a velvet bikini for a luxurious, unconventional feel"
]

# Category 2: Subject & Appearance
subjects = [
    "J-pop Idol", "Japanese model", "Pop star", "East Asian woman", "Solo artist", "J-pop dancer", 
    "Lead vocalist", "Japanese actress", "Asian influencer", "Fashion icon", "It-girl", 
    "Tokyo fashion model", "Tokyoite", "Rising star", "Music sensation", "Urban muse", "Night crawler", "Style maven"
]
features = [
    "Sharp jawline", "Intense gaze", "Piercing eyes", "Confident expression", "Symmetrical face", 
    "Flawless complexion", "Smirking", "Glass skin", "Plump lips", "High cheekbones", 
    "Mona Lisa smile", "Mysterious look", "Sultry stare", "Defined brows", "Elegant nose", "A knowing glance", "Heart-shaped lips"
]
hair = [
    "Sleek ponytail", "Vibrant crimson hair", "Electric blue hair", "Hime cut", "Messy bun", 
    "Long flowing hair", "Styled baby hairs", "Platinum blonde wolf cut", "Pastel pink bob", 
    "Jet black straight hair", "Braided space buns", "Wet look hair", "Face-framing tendrils", 
    "Two-tone hair (skunk stripe)", "Shaggy mullet", "Curtain bangs", "Intricate updo", "Glossy dark hair"
]
makeup = [
    "Smokey eye makeup", "Bold red lipstick", "Graphic eyeliner", "Glowing skin", "Contoured cheekbones", 
    "Dewy makeup look", "Glitter eyeshadow", "'Igari' (hangover) blush style", "Aegyo-sal makeup", "Gradient lips", 
    "Sharp winged liner", "Gemstone face accents", "Glossy eyelids", "Monochromatic makeup", 
    "Natural 'no-makeup' makeup", "Bleached brows", "Metallic lipstick"
]

# Category 4: The Setting (Tokyo)
locations = [
    "in the middle of Shibuya Scramble Crossing at night",
    "in a narrow, lantern-lit alley in Shinjuku's Golden Gai",
    "in front of the neon signs and electronic stores of Akihabara",
    "on a quiet, traditional street in the Yanaka district",
    "on a rooftop overlooking the Tokyo Tower",
    "beneath the cherry blossom trees in Ueno Park",
    "inside a futuristic, minimalist cafe in Omotesando",
    "wandering through the vibrant Takeshita Street in Harajuku",
    "with the Tokyo Skytree dominating the background",
    "in a serene, green oasis like Shinjuku Gyoen National Garden",
    "inside a packed train on the Yamanote Line",
    "in front of a wall of colorful gachapon machines",
    "at the entrance of the serene Meiji Jingu Shrine",
    "in a gritty, rain-slicked alleyway in Kabukicho",
    "exploring the art installations at teamLab Borderless",
    "on a bridge with a view of the Rainbow Bridge and Odaiba skyline",
    "in a cozy, vinyl-filled jazz kissa (cafe)",
    "surrounded by the luxury storefronts of Ginza",
    "at a traditional red torii gate of a local shrine",
    "in the bustling Tsukiji Outer Market",
    "inside an old-school arcade, with the sounds of games all around",
    "on the glass observation deck of Shibuya Sky",
    "in a themed cafe, like a cat cafe or a maid cafe",
    "in the middle of Omoide Yokocho (Memory Lane), with yakitori smoke in the air",
    "posing with the giant Godzilla head in Shinjuku",
    "on a boat in the Chidorigafuchi moat during sakura season",
    "inside the architecturally stunning Tokyo International Forum",
    "in front of the colorful buildings of the Nakano Broadway shopping complex",
    "waiting at a classic Tokyo train crossing as the barriers come down",
    "in a quiet, minimalist art gallery in the Roppongi Art Triangle",
    "at a vibrant summer festival (matsuri) with food stalls and lanterns",
    "on an empty subway platform late at night",
    "exploring the vintage clothing stores of Shimokitazawa",
    "at the base of the massive Gundam statue in Odaiba",
    "in a lush bamboo forest at Nezu Shrine",
    "surrounded by the organized chaos of Tokyo Station",
    "in a secret, tiny bar in a back alley of Ebisu",
    "looking out over the city from a high-rise hotel window",
    "at the Senso-ji Temple in Asakusa, with the large red lantern",
    "in a stylish, high-end cocktail bar in Ginza",
    "amidst the vibrant, youthful energy of Center Gai in Shibuya",
    "walking along the Meguro River, lined with cherry trees",
    "inside a crowded, neon-lit pachinko parlor",
    "at the quirky Gōtokuji Temple, filled with thousands of maneki-neko (beckoning cats)",
    "on a pedestrian bridge overlooking busy city streets",
    "in the trendy, bohemian neighborhood of Koenji",
    "inside a capsule hotel, peering out from a pod",
    "at the tranquil Japanese garden of the Nezu Museum",
    "in a bustling, multi-story electronics store like Yodobashi Camera",
    "on a quiet side street in Kagurazaka, with its old-world charm"
]

footwear = [
    "Chunky platform boots", "High-top sneakers", "Elegant stilettos", "Tabi boots", "Knee-high leather boots", 
    "Strappy heels", "Classic combat boots", "Designer trainers", "Stylish loafers", "Mary Janes", 
    "Geta or Zori sandals with a modern outfit", "Mules", "Over-the-knee boots", "Clear heels", "Onitsuka Tiger sneakers", "Wedge sneakers"
]

accessories = [
    "Layered silver chains", "Statement hoop earrings", "Futuristic designer sunglasses", "A trendy beanie", "A delicate choker", "A luxury brand handbag", 
    "A body chain over a simple top", "A single, bold statement earring", "A leather harness for an edgy look", "A stylish beret", "A newsboy cap", 
    "Fingerless gloves", "A leg garter", "Arm cuffs", "Dainty layered necklaces", "A vintage watch", "A bandana tied in the hair", "A chain belt"
]

atmospheres = [
    "Urban grit", "Neon-drenched cityscape", "Cyberpunk aesthetic", "Moody atmosphere", "Cinematic", "Industrial setting", 
    "Raw and unfiltered", "Nostalgic and dreamlike", "Futuristic and clean", "High-energy and electric", 
    "Solitary and melancholic", "Hazy and mysterious", "Gritty realism", "Sophisticated urban vibe",
    "Vibrant street life", "Tranquility amidst chaos", "Retro cinematic feel", "Wabi-sabi imperfection"
]

# Category 5: Photography & Artistic Style
shot_types = [
    "Full-body shot", "Dynamic pose", "Action shot", "Candid street style photo", "Close-up portrait", 
    "Editorial style photoshoot", "Low-angle shot emphasizing power", "High-angle shot", "Mid-shot", 
    "Over-the-shoulder shot", "Motion blur effect", "Dutch angle for unease", "Silhouette against the skyline", 
    "Profile shot", "Environmental portrait", "Black and white photo", "Wide-angle shot"
]
lighting = [
    "Dramatic lighting", "Hard shadows", "Lens flare", "Reflecting neon glow", "Soft diffused light", 
    "Golden hour lighting", "Blue hour lighting", "Rim lighting", "Split lighting", "Backlight", 
    "Chiaroscuro (strong light/dark contrast)", "Volumetric lighting", "Light leaks", "Bokeh background lights", 
    "Studio flash lighting on location", "Natural window light", "Muted tones", "Harsh direct flash"
]
quality = [
    "Photorealistic", "Hyper-detailed", "8K resolution", "Sharp focus", "Cinematic quality", 
    "Ultra realistic", "Insanely detailed", "Intricate details", "Professional photography", 
    "Hasselblad photo", "Shot on Portra 400 film", "Film grain", "Crystal clear", "High dynamic range (HDR)", 
    "Masterpiece quality", "Award-winning photography", "Unreal Engine 5 render", "Magazine cover quality"
]
styles = [
    "Fashion magazine aesthetic (like Vogue or FRUiTS)", "Music video still", "Movie poster style", "Street photography (like Daido Moriyama)", 
    "Neo-noir film aesthetic", "Cyberpunk vibe", "Indie movie still", "90s fashion photography", 
    "Gritty documentary style", "High-fashion campaign", "Lo-fi aesthetic", "Surrealist photography",
    "Cinematic still from a Wong Kar-wai film", "Gritty realism", "Hyper-maximalism", "Urban fantasy"
]


def feifeigenerateprompt():
    """Generates a random, massively detailed prompt for an AI art generator with a Tokyo theme."""

    # --- Let's build the prompt piece by piece ---

    # 1. Start with the core subject and their defining traits
    personality_trait1 = random.choice(vibes + menaces)
    personality_trait2 = random.choice(firecrackers + dime_pieces)
    subject_core = f"{personality_trait1} and {personality_trait2} {random.choice(subjects)}"

    # 2. Add specific appearance details
    appearance_details = f"with {random.choice(features)}, {random.choice(hair)}, and {random.choice(makeup)}"

    # 3. Describe the outfit
    # outfit = f"wearing {random.choice(clothing)}, {random.choice(footwear)}, accessorized with {random.choice(accessories)}"
    outfit = f"wearing {random.choice(clothing)}"
    # 4. Set the scene in Tokyo
    setting = f"posing {random.choice(locations)}, embodying the {random.choice(atmospheres)} of the city"

    # 5. Define the photographic style
    photo_style = f"A {random.choice(shot_types)}, captured in a {random.choice(styles)}. The image features {random.choice(lighting)} and is {random.choice(quality)}."

    # --- Combine everything into a final prompt ---
    final_prompt = f"{subject_core}, {appearance_details}. She's {outfit}. {setting}. {photo_style}"

    return final_prompt

# --- Example Usage ---
# new_tokyo_prompt = feifeigenerateprompt()
# print(new_tokyo_prompt)